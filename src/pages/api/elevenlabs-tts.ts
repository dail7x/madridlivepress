import type { APIRoute } from 'astro';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

export const prerender = false;

// Default high-quality neural voices in ElevenLabs
const DEFAULT_VOICES = {
  es: 'pNInz6obpgDQGcFmaJgB', // Adam (Multilingual)
  en: '21m00Tcm4TlvDq8ikWAM', // Rachel (Multilingual)
};

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
        // ignore json parse error
      }
    }

    if (!text) {
      text = url.searchParams.get('text') || '';
      lang = url.searchParams.get('lang') || 'es';
      slug = url.searchParams.get('slug') || '';
      voiceId = url.searchParams.get('voiceId') || '';
    }

    if (!text) {
      return new Response(JSON.stringify({ error: 'Missing text parameter' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const selectedLang = lang.startsWith('en') ? 'en' : 'es';
    const selectedVoiceId = voiceId || DEFAULT_VOICES[selectedLang];

    // Determine cache key
    const textHash = crypto.createHash('md5').update(`${selectedVoiceId}-${text}`).digest('hex').slice(0, 16);
    const cleanSlug = slug ? slug.replace(/[^a-zA-Z0-9-_]/g, '').slice(0, 60) : 'brief';
    const filename = `${cleanSlug}-${selectedLang}-${textHash}.mp3`;
    const audioDir = path.resolve(process.cwd(), 'public/audio/briefs');
    const filePath = path.join(audioDir, filename);

    // 1. Check if cached on disk
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

    // 2. Call ElevenLabs API
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
        text,
        model_id: 'eleven_multilingual_v2',
        voice_settings: {
          stability: 0.55,
          similarity_boost: 0.8,
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

    // Save to disk cache
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
