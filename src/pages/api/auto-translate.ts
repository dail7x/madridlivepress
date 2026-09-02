import type { APIRoute } from 'astro';

export const prerender = false;

const DIRECTUS_URL = process.env.DIRECTUS_URL || 'https://mlpdirectus.116.203.118.1.sslip.io';
const DIRECTUS_TOKEN = process.env.DIRECTUS_STATIC_TOKEN || 'mlp_secret_directus_token_2026';
const CF_ACCOUNT_ID = process.env.CLOUDFLARE_ACCOUNT_ID || (import.meta as any).env?.CLOUDFLARE_ACCOUNT_ID;
const CF_AI_TOKEN = process.env.CLOUDFLARE_AI_TOKEN || (import.meta as any).env?.CLOUDFLARE_AI_TOKEN;

function extractJson(raw: any): any {
  if (typeof raw === 'object' && raw !== null) return raw;
  if (typeof raw !== 'string') return null;
  const match = raw.match(/\{[\s\S]*\}/);
  if (match) {
    try {
      return JSON.parse(match[0]);
    } catch (e) {
      console.warn('Error parsing JSON from Workers AI:', e);
    }
  }
  return null;
}

function slugify(text: string): string {
  return text
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/[\s-]+/g, '-');
}

export const ALL: APIRoute = async ({ request, url }) => {
  try {
    let body: any = {};
    if (request.method === 'POST') {
      try {
        body = await request.json();
      } catch (e) {
        // empty body
      }
    }

    // Determine article ID from various possible Directus Flow / webhook structures
    let articleId =
      body.key ||
      (Array.isArray(body.keys) && body.keys[0]) ||
      body.payload?.id ||
      body.id ||
      url.searchParams.get('id');

    if (!articleId) {
      return new Response(JSON.stringify({ error: 'Missing article id or key' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Prevent infinite loop if the webhook event is an update that only updated English fields
    if (body.payload && typeof body.payload === 'object') {
      const updatedKeys = Object.keys(body.payload);
      const isOnlyEnUpdate = updatedKeys.length > 0 && updatedKeys.every((k) => k.endsWith('_en'));
      if (isOnlyEnUpdate) {
        return new Response(
          JSON.stringify({ message: 'Skipped: update only contains generated English fields to prevent loop' }),
          { status: 200, headers: { 'Content-Type': 'application/json' } }
        );
      }
    }

    // 1. Fetch current article from Directus
    const directusRes = await fetch(`${DIRECTUS_URL}/items/comunicados/${articleId}?fields=*`, {
      headers: {
        Authorization: `Bearer ${DIRECTUS_TOKEN}`,
      },
    });

    if (!directusRes.ok) {
      return new Response(
        JSON.stringify({ error: `Article ${articleId} not found in Directus`, status: directusRes.status }),
        { status: directusRes.status, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const { data: item } = await directusRes.json();
    if (!item) {
      return new Response(JSON.stringify({ error: 'Article record is null' }), {
        status: 404,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const tituloEs = item.titulo || '';
    const bajadaEs = item.bajada || '';
    const cuerpoEs = item.cuerpo || '';
    const audioScriptEs = item.audio_script_es || bajadaEs || tituloEs;
    const puntosClaveEs = item.puntos_clave || [];

    if (!tituloEs) {
      return new Response(JSON.stringify({ message: 'Article has no Spanish title to translate' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // 2. Call Cloudflare Workers AI (Llama 3.1 8B Instruct)
    const systemPrompt = `You are a world-class bilingual journalist and editor for Madrid Live Press / Reuters.
Translate the provided Spanish press release fields to English with journalistic precision and elegance.
You MUST output ONLY a valid JSON object with EXACTLY these keys:
{
  "titulo_en": "Professional English news headline",
  "slug_en": "kebab-case-slug-in-english",
  "bajada_en": "Journalistic English subheading or lead excerpt",
  "cuerpo_en": "Full English article body preserving all HTML tags like <p>, <blockquote>, <strong>, <a>",
  "audio_script_en": "Clear, natural spoken news brief in English for ElevenLabs narration (100-140 words)",
  "puntos_clave_en": ["Key Takeaway 1: with verified numbers", "Key Takeaway 2: with verified metrics"]
}
Output raw JSON only. Do not include markdown codeblocks or conversational text.`;

    const userPrompt = JSON.stringify({
      titulo: tituloEs,
      bajada: bajadaEs,
      cuerpo: cuerpoEs,
      audio_script_es: audioScriptEs,
      puntos_clave: puntosClaveEs,
    });

    const cfUrl = `https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct`;
    const cfRes = await fetch(cfUrl, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${CF_AI_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userPrompt },
        ],
        max_tokens: 2500,
        temperature: 0.15,
      }),
    });

    if (!cfRes.ok) {
      const errText = await cfRes.text();
      console.error('Cloudflare Workers AI translation failed:', cfRes.status, errText);
      return new Response(JSON.stringify({ error: 'Cloudflare AI error', detail: errText }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const cfData = await cfRes.json();
    const rawAiOutput = cfData.result?.response || cfData.result?.choices?.[0]?.message?.content || '';
    const parsed = extractJson(rawAiOutput);

    if (!parsed || !parsed.titulo_en) {
      console.error('Failed to parse JSON from AI output:', rawAiOutput);
      return new Response(JSON.stringify({ error: 'AI output format invalid', raw: rawAiOutput }), {
        status: 502,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const generatedSlugEn = parsed.slug_en ? slugify(parsed.slug_en) : slugify(parsed.titulo_en);

    const updatePayload: Record<string, any> = {
      titulo_en: parsed.titulo_en,
      slug_en: generatedSlugEn,
      bajada_en: parsed.bajada_en || '',
      cuerpo_en: parsed.cuerpo_en || cuerpoEs,
      audio_script_en: parsed.audio_script_en || '',
      puntos_clave_en: Array.isArray(parsed.puntos_clave_en) ? parsed.puntos_clave_en : [],
    };

    // 3. Update Directus article with translated fields
    const patchRes = await fetch(`${DIRECTUS_URL}/items/comunicados/${articleId}`, {
      method: 'PATCH',
      headers: {
        Authorization: `Bearer ${DIRECTUS_TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updatePayload),
    });

    if (!patchRes.ok) {
      const patchErr = await patchRes.text();
      console.error('Directus update failed:', patchRes.status, patchErr);
      return new Response(JSON.stringify({ error: 'Directus patch failed', detail: patchErr }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    return new Response(
      JSON.stringify({
        success: true,
        id: articleId,
        translated: updatePayload,
      }),
      {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  } catch (err: any) {
    console.error('Unexpected error in auto-translate endpoint:', err);
    return new Response(JSON.stringify({ error: 'Internal Server Error', message: err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
