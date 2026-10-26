export type SupportedTargetLang = 'it' | 'fr' | 'en';

export interface ArticleToTranslate {
  titulo: string;
  bajada?: string;
  cuerpo?: string;
  puntos_clave?: string[];
  audio_script?: string;
}

export interface TranslatedArticleResult {
  titulo: string;
  slug: string;
  bajada: string;
  cuerpo: string;
  puntos_clave: string[];
  audio_script: string;
  targetLang: SupportedTargetLang;
}

export interface TranslationProvider {
  readonly name: string;
  translateArticle(
    article: ArticleToTranslate,
    targetLang: SupportedTargetLang,
    sourceLang?: string
  ): Promise<TranslatedArticleResult>;
}
