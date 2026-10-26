import type { TranslationProvider, ArticleToTranslate, TranslatedArticleResult, SupportedTargetLang } from './types';
import { CloudflareWorkersAIProvider } from './providers/cloudflare';
import { OpenAIProvider } from './providers/openai';

export * from './types';
export * from './providers/cloudflare';
export * from './providers/openai';

/**
 * Returns the active translation provider according to environment variable
 * TRANSLATION_PROVIDER ('cloudflare' | 'openai'). Default: 'cloudflare'.
 */
export function getTranslationProvider(providerName?: string): TranslationProvider {
  const selected = providerName || (typeof process !== 'undefined' ? process.env.TRANSLATION_PROVIDER : '') || 'cloudflare';

  switch (selected.toLowerCase()) {
    case 'openai':
      return new OpenAIProvider();
    case 'cloudflare':
    default:
      return new CloudflareWorkersAIProvider();
  }
}

/**
 * High-level orchestration function to translate an article to Italian, French, or English
 */
export async function translateArticle(
  article: ArticleToTranslate,
  targetLang: SupportedTargetLang,
  preferredProvider?: string
): Promise<TranslatedArticleResult> {
  const provider = getTranslationProvider(preferredProvider);
  return provider.translateArticle(article, targetLang);
}
