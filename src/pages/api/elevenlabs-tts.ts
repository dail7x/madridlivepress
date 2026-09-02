import type { APIRoute } from 'astro';
import fs from 'node:fs';
import path from 'node:path';

export const prerender = false;

const DIRECTUS_URL = process.env.DIRECTUS_URL || 'https://mlpdirectus.116.203.118.1.sslip.io';
const DIRECTUS_TOKEN = process.env.DIRECTUS_STATIC_TOKEN || 'mlp_secret_directus_token_2026';

// George (JBFqnCBsd6RMkjVDRZzb) for English (verified 200 OK on user account)
// Adam (pNInz6obpgDQGcFmaJgB) for Spanish (verified 200 OK on user account)
const DEFAULT_VOICES = {
  es: 'pNInz6obpgDQGcFmaJgB', // Adam
  en: 'JBFqnCBsd6RMkjVDRZzb', // George
};

function cleanHtml(html: string): string {
  if (!html) return '';
  return html
    .replace(/<\/(?:p|div|h[1-6]|li|blockquote)[^>]*>/gi, '. ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .replace(/\.+/g, '.')
    .trim();
}

export const ALL: APIRoute = async ({ request, url }) => {
  try {
    let text = '';
    let lang = 'es';
    let slug = '';
    let voiceId = '';

    if (request.method === 'POST') {
      try {
        const body = await request.json();
        text = body.text || '';
        lang = body.lang || 'es';
        slug = body.slug || '';
        voiceId = body.voiceId || '';
      } catch (e) {
        // ignore
      }
    }

    if (!text) {
      text = url.searchParams.get('text') || '';
      lang = url.searchParams.get('lang') || 'es';
      slug = url.searchParams.get('slug') || '';
      voiceId = url.searchParams.get('voiceId') || '';
    }

    const selectedLang = lang.startsWith('en') ? 'en' : 'es';
    const cleanSlug = slug ? slug.replace(/[^a-zA-Z0-9-_]/g, '').slice(0, 80) : 'brief';
    const audioDir = path.resolve(process.cwd(), 'public/audio/briefs');
    const filename = `${cleanSlug}-${selectedLang}.mp3`;
    const filePath = path.join(audioDir, filename);

    // 1. Check if audio is already cached on disk (0ms latency, zero API cost)
    if (fs.existsSync(filePath)) {
      const cachedBuffer = fs.readFileSync(filePath);
      return new Response(cachedBuffer, {
        status: 200,
        headers: {
          'Content-Type': 'audio/mpeg',
          'Cache-Control': 'public, max-age=604800, immutable',
          'X-Cache': 'HIT',
        },
      });
    }

    // 2. If text was not passed in query (to prevent 414 URI Too Long), fetch full article from Directus
    if (!text && slug) {
      try {
        const filterQuery = encodeURIComponent(
          JSON.stringify({
            _or: [{ slug: { _eq: slug } }, { slug_en: { _eq: slug } }],
            status: { _eq: 'published' },
          })
        );
        const directusRes = await fetch(`${DIRECTUS_URL}/items/comunicados?filter=${filterQuery}&limit=1`, {
          headers: { Authorization: `Bearer ${DIRECTUS_TOKEN}` },
        });
        if (directusRes.ok) {
          const json = await directusRes.json();
          const art = json.data?.[0];
          if (art) {
            if (selectedLang === 'en') {
              const t = art.titulo_en || art.titulo || '';
              const b = art.bajada_en || art.bajada || '';
              const c = cleanHtml(art.cuerpo_en || art.cuerpo || '');
              text = art.audio_script_en || `${t}. ${b}. ${c}`;
            } else {
              const t = art.titulo || '';
              const b = art.bajada || '';
              const c = cleanHtml(art.cuerpo || '');
              text = art.audio_script_es || `${t}. ${b}. ${c}`;
            }
          }
        }
      } catch (fetchErr) {
        console.warn('Could not load text from Directus for audio:', fetchErr);
      }
    }

    if (!text) {
      return new Response(JSON.stringify({ error: 'Missing text or slug parameter' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // ElevenLabs safety cutoff for free tier single request: 4,800 characters
    const trimmedText = text.slice(0, 4800);
    const selectedVoiceId = voiceId || DEFAULT_VOICES[selectedLang];

    // 3. Call ElevenLabs Text-to-Speech API
    const apiKey = process.env.ELEVENLABS_API_KEY || (import.meta as any).env?.ELEVENLABS_API_KEY;
    if (!apiKey) {
      return new Response(JSON.stringify({ error: 'ELEVENLABS_API_KEY not configured' }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const elevenRes = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${selectedVoiceId}`, {
      method: 'POST',
      headers: {
        'xi-api-key': apiKey,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
      },
      body: JSON.stringify({
        text: trimmedText,
        model_id: 'eleven_multilingual_v2',
        voice_settings: {
          stability: 0.5,
          similarity_boost: 0.75,
          style: 0.0,
          use_speaker_boost: true,
        },
      }),
    });

    if (!elevenRes.ok) {
      const errText = await elevenRes.text();
      console.error('ElevenLabs API error:', elevenRes.status, errText);
      return new Response(JSON.stringify({ error: 'ElevenLabs TTS generation failed', detail: errText }), {
        status: elevenRes.status,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const audioArrayBuffer = await elevenRes.arrayBuffer();
    const audioBuffer = Buffer.from(audioArrayBuffer);

    // 4. Save to disk cache
    try {
      if (!fs.existsSync(audioDir)) {
        fs.mkdirSync(audioDir, { recursive: true });
      }
      fs.writeFileSync(filePath, audioBuffer);
    } catch (saveErr) {
      console.warn('Could not cache ElevenLabs audio to disk:', saveErr);
    }

    return new Response(audioBuffer, {
      status: 200,
      headers: {
        'Content-Type': 'audio/mpeg',
        'Cache-Control': 'public, max-age=604800, immutable',
        'X-Cache': 'MISS',
      },
    });
  } catch (error: any) {
    console.error('Error in ElevenLabs TTS handler:', error);
    return new Response(JSON.stringify({ error: 'Internal server error', message: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
