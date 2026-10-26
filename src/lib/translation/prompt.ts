import type { ArticleToTranslate, SupportedTargetLang } from './types';

export const LANGUAGE_NAMES: Record<SupportedTargetLang, string> = {
  it: 'Italian (Italiano)',
  fr: 'French (Français)',
  en: 'English'
};

export function buildSystemPrompt(targetLang: SupportedTargetLang): string {
  const targetName = LANGUAGE_NAMES[targetLang] || targetLang;

  return `You are a world-class senior press journalist and professional translator for Noche Madrid Press, the official international pressroom for NocheMadrid and the capital's nightlife and culture.

Your task is to translate an official Spanish press release into ${targetName}.

CRITICAL EDITORIAL & TRANSLATION RULES:
1. Tone: Formal, journalistic, institutional, and verified (Reuters / AFP style).
2. Proper Nouns & Brands: Do NOT translate proper names or trademarks:
   - "NocheMadrid", "Noche Madrid Press", "Comunidad de Madrid", "Ayuntamiento de Madrid".
   - Names of people (e.g. "Alejandro Zamarro", "Vicente Pizcueta").
   - Names of venues (e.g. "Teatro Kapital", "Shôko", "Sala Riviera", "Joy Eslava").
3. Mandatory Industry Glossary:
   - Spanish "ocio nocturno" MUST be translated as:
     * French: "vie nocturne" (NEVER literal calques like "ocase" or "loisir de nuit").
     * Italian: "vita notturna" (NEVER "ocio notturno").
     * English: "nightlife" or "nightlife industry".
   - Spanish "salas de conciertos / salas de música en vivo":
     * French: "salles de concert / espaces musicaux".
     * Italian: "sale da concerto / locali di musica dal vivo".
     * English: "live music venues / concert halls".
   - Spanish "tardeo": Keep the Madrid cultural term "tardeo" (optionally with brief context: afternoon social scene / early evening cultural clubbing).
4. Subtitle / Bajada: Must be concise, impactful, and complement the headline with verifiable data (percentage, economic volume, or audience metrics).
5. HTML Body: Preserve all HTML tags (<p>, <blockquote>, <strong>, <em>, <a>, <ul>, <li>, etc.) EXACTLY as structured. Translate only the inner human-readable text. Do not omit quotes or blockquotes.
6. Slug: Generate a concise, SEO-optimized URL slug strictly in ${targetName} using lowercase letters, numbers, and hyphens only (e.g., 'deux-millions-de-touristes-madrid-ete').
5. Output format: You MUST return ONLY a valid JSON object matching this exact structure without markdown backticks or commentary:
{
  "titulo": "...",
  "slug": "...",
  "bajada": "...",
  "cuerpo": "...",
  "puntos_clave": ["...", "..."],
  "audio_script": "..."
}`;
}

export function buildUserPrompt(article: ArticleToTranslate, targetLang: SupportedTargetLang): string {
  const targetName = LANGUAGE_NAMES[targetLang] || targetLang;

  return `Translate the following Spanish press release into ${targetName}.

Title:
${article.titulo}

Subtitle / Bajada:
${article.bajada || ''}

Points Clave / TL;DR:
${JSON.stringify(article.puntos_clave || [])}

HTML Body:
${article.cuerpo || ''}

Audio Script:
${article.audio_script || ''}

Respond with pure JSON only matching the specified schema.`;
}
