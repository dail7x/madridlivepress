import type { APIRoute } from 'astro';
import { directus, readItem, createItem, updateItem, readItems, DIRECTUS_URL, DIRECTUS_TOKEN } from '@/lib/directus';
import { translateArticle } from '@/lib/translation';
import type { SupportedTargetLang } from '@/lib/translation';

export const prerender = false;

const INTERNAL_SECRET = import.meta.env.TRANSLATION_WEBHOOK_SECRET || 'mlp_translation_secret_2026';

export const POST: APIRoute = async ({ request }) => {
  try {
    const authHeader = request.headers.get('Authorization');
    const token = authHeader?.replace(/^Bearer\s+/i, '');

    // Protect endpoint
    if (token !== INTERNAL_SECRET && token !== DIRECTUS_TOKEN) {
      return new Response(JSON.stringify({ error: 'Unauthorized' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const body = await request.json();
    const articleId = body.articleId || body.id || body.key;
    const targetLangs: SupportedTargetLang[] = body.targetLangs || ['it', 'fr'];

    if (!articleId) {
      return new Response(JSON.stringify({ error: 'Missing articleId' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // 1. Fetch original Spanish release from Directus
    const article = await directus.request(
      readItem('comunicados' as any, articleId, {
        fields: ['id', 'titulo', 'bajada', 'cuerpo', 'puntos_clave', 'audio_script_es', 'slug']
      })
    );

    if (!article) {
      return new Response(JSON.stringify({ error: 'Article not found' }), {
        status: 404,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const results: Record<string, any> = {};

    // 2. Translate for each requested language
    for (const lang of targetLangs) {
      const langCode = lang === 'it' ? 'it-IT' : lang === 'fr' ? 'fr-FR' : 'en-US';

      try {
        const translated = await translateArticle(
          {
            titulo: article.titulo,
            bajada: article.bajada,
            cuerpo: article.cuerpo,
            puntos_clave: article.puntos_clave,
            audio_script: article.audio_script_es
          },
          lang
        );

        // Check if translation already exists for this article and language
        const existingTrans = await directus.request(
          readItems('comunicados_translations' as any, {
            filter: {
              comunicados_id: { _eq: articleId },
              languages_code: { _eq: langCode }
            },
            limit: 1
          })
        );

        const transData = {
          comunicados_id: articleId,
          languages_code: langCode,
          titulo: translated.titulo,
          slug: translated.slug,
          bajada: translated.bajada,
          cuerpo: translated.cuerpo,
          puntos_clave: translated.puntos_clave,
          audio_script: translated.audio_script
        };

        if (existingTrans && (existingTrans as any[]).length > 0) {
          const transId = (existingTrans as any[])[0].id;
          await directus.request(updateItem('comunicados_translations' as any, transId, transData));
          results[lang] = { status: 'updated', id: transId, slug: translated.slug };
        } else {
          const created = await directus.request(createItem('comunicados_translations' as any, transData));
          results[lang] = { status: 'created', id: (created as any)?.id, slug: translated.slug };
        }
      } catch (err: any) {
        console.error(`Error translating article ${articleId} to ${lang}:`, err);
        results[lang] = { status: 'error', error: err.message };
      }
    }

    return new Response(JSON.stringify({ success: true, articleId, results }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error: any) {
    console.error('Translation webhook error:', error);
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};
