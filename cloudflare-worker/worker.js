/**
 * Cloudflare Worker: Madrid Live Press Translation Agent
 * Powered by Cloudflare Workers AI (@cf/meta/llama-3.3-70b-instruct)
 */

const SYSTEM_PROMPTS = {
  it: `Sei un giornalista professionista per Madrid Live Press. Traduci questo comunicato stampa ufficiale in italiano. Mantieni intatti tutti i tag HTML (<p>, <blockquote>, <strong>, ecc.). Non tradurre nomi propri ("NocheMadrid", nomi di sale, persone). Genera uno slug URL valido in italiano. Restituisci ESCLUSIVAMENTE un JSON valido con: titulo, slug, bajada, cuerpo, puntos_clave (array di stringhe) e audio_script.`,
  fr: `Vous êtes un journaliste professionnel pour Madrid Live Press. Traduisez ce communiqué de presse officiel en français. Préservez intacts tous les tags HTML (<p>, <blockquote>, <strong>, etc.). Ne traduisez pas les noms propres ("NocheMadrid", noms de salles, personnes). Générez un slug d'URL valide en français. Renvoyez EXCLUSIVEMENT un JSON valide avec: titulo, slug, bajada, cuerpo, puntos_clave (tableau de chaînes) et audio_script.`,
  en: `You are a professional press journalist for Madrid Live Press. Translate this official press release into English. Preserve all HTML tags (<p>, <blockquote>, <strong>, etc.). Do not translate proper names ("NocheMadrid", venue names, people). Generate a clean URL slug in English. Return ONLY valid JSON with: titulo, slug, bajada, cuerpo, puntos_clave (array of strings) and audio_script.`
};

export default {
  async fetch(request, env, ctx) {
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
      });
    }

    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'Method not allowed. Use POST.' }), {
        status: 405,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Optional shared secret authentication
    if (env.TRANSLATION_SECRET) {
      const authHeader = request.headers.get('Authorization') || '';
      const token = authHeader.replace(/^Bearer\s+/i, '');
      if (token !== env.TRANSLATION_SECRET) {
        return new Response(JSON.stringify({ error: 'Unauthorized.' }), {
          status: 401,
          headers: { 'Content-Type': 'application/json' }
        });
      }
    }

    try {
      const { article, targetLang = 'it' } = await request.json();

      if (!article || !article.titulo) {
        return new Response(JSON.stringify({ error: 'Missing article data.' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json' }
        });
      }

      const systemPrompt = SYSTEM_PROMPTS[targetLang] || SYSTEM_PROMPTS.en;
      const userPrompt = `Tradurre:
Title: ${article.titulo}
Subtitle: ${article.bajada || ''}
TL;DR / Points: ${JSON.stringify(article.puntos_clave || [])}
HTML Body: ${article.cuerpo || ''}
Audio Script: ${article.audio_script || ''}

Restituisci SOLO un oggetto JSON valido:
{
  "titulo": "...",
  "slug": "...",
  "bajada": "...",
  "cuerpo": "...",
  "puntos_clave": ["..."],
  "audio_script": "..."
}`;

      const model = env.AI_MODEL || '@cf/meta/llama-3.3-70b-instruct';
      const aiResponse = await env.AI.run(model, {
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userPrompt }
        ],
        response_format: { type: 'json_object' }
      });

      let raw = aiResponse.response || aiResponse;
      if (typeof raw === 'string') {
        raw = raw.replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/```$/i, '').trim();
        raw = JSON.parse(raw);
      }

      return new Response(JSON.stringify({ success: true, data: raw }), {
        status: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};
