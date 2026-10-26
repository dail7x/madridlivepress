import type { TranslationProvider, ArticleToTranslate, TranslatedArticleResult, SupportedTargetLang } from '../types';
import { buildSystemPrompt, buildUserPrompt } from '../prompt';

export interface OpenAIProviderOptions {
  apiKey?: string;
  model?: string;
}

export class OpenAIProvider implements TranslationProvider {
  readonly name = 'openai';
  private apiKey: string;
  private model: string;

  constructor(options?: OpenAIProviderOptions) {
    this.apiKey = options?.apiKey || (typeof process !== 'undefined' ? process.env.OPENAI_API_KEY : '') || '';
    this.model = options?.model || (typeof process !== 'undefined' ? process.env.OPENAI_TRANSLATION_MODEL : '') || 'gpt-4o-mini';
  }

  async translateArticle(
    article: ArticleToTranslate,
    targetLang: SupportedTargetLang
  ): Promise<TranslatedArticleResult> {
    if (!this.apiKey) {
      throw new Error('OPENAI_API_KEY environment variable is not set.');
    }

    const systemPrompt = buildSystemPrompt(targetLang);
    const userPrompt = buildUserPrompt(article, targetLang);

    const res = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.apiKey}`
      },
      body: JSON.stringify({
        model: this.model,
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userPrompt }
        ],
        response_format: { type: 'json_object' },
        temperature: 0.2
      })
    });

    if (!res.ok) {
      throw new Error(`OpenAI API error ${res.status}: ${await res.text()}`);
    }

    const json = await res.json();
    const content = json.choices?.[0]?.message?.content;
    if (!content) {
      throw new Error('Empty response received from OpenAI API.');
    }

    const parsed = JSON.parse(content);
    return {
      titulo: parsed.titulo || '',
      slug: parsed.slug || '',
      bajada: parsed.bajada || '',
      cuerpo: parsed.cuerpo || '',
      puntos_clave: Array.isArray(parsed.puntos_clave) ? parsed.puntos_clave : [],
      audio_script: parsed.audio_script || parsed.bajada || parsed.titulo || '',
      targetLang
    };
  }
}
