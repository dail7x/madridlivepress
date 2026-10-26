import type { TranslationProvider, ArticleToTranslate, TranslatedArticleResult, SupportedTargetLang } from '../types';
import { buildSystemPrompt, buildUserPrompt } from '../prompt';

export interface CloudflareProviderOptions {
  accountId?: string;
  apiToken?: string;
  model?: string;
  workerUrl?: string; // Optional custom deployed worker endpoint
}

export class CloudflareWorkersAIProvider implements TranslationProvider {
  readonly name = 'cloudflare';
  private accountId: string;
  private apiToken: string;
  private model: string;
  private workerUrl?: string;

  constructor(options?: CloudflareProviderOptions) {
    const metaEnv = (import.meta as any).env || {};
    this.accountId = options?.accountId || process.env.CLOUDFLARE_ACCOUNT_ID || metaEnv.CLOUDFLARE_ACCOUNT_ID || '';
    this.apiToken = options?.apiToken || process.env.CLOUDFLARE_AI_TOKEN || metaEnv.CLOUDFLARE_AI_TOKEN || process.env.CLOUDFLARE_API_TOKEN || metaEnv.CLOUDFLARE_API_TOKEN || '';
    this.model = options?.model || process.env.CLOUDFLARE_AI_MODEL || metaEnv.CLOUDFLARE_AI_MODEL || '@cf/meta/llama-3.1-8b-instruct';
    this.workerUrl = options?.workerUrl || process.env.CLOUDFLARE_WORKER_URL || metaEnv.CLOUDFLARE_WORKER_URL || '';
  }

  async translateArticle(
    article: ArticleToTranslate,
    targetLang: SupportedTargetLang
  ): Promise<TranslatedArticleResult> {
    const systemPrompt = buildSystemPrompt(targetLang);
    const userPrompt = buildUserPrompt(article, targetLang);

    let rawResponse = '';

    // Strategy 1: If a dedicated Cloudflare Worker URL is configured
    if (this.workerUrl) {
      const res = await fetch(this.workerUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(this.apiToken ? { Authorization: `Bearer ${this.apiToken}` } : {})
        },
        body: JSON.stringify({
          article,
          targetLang
        })
      });

      if (!res.ok) {
        throw new Error(`Cloudflare Worker returned error ${res.status}: ${await res.text()}`);
      }

      const json = await res.json();
      if (json.data && json.data.titulo) {
        return {
          ...json.data,
          targetLang
        };
      }
      rawResponse = typeof json.result === 'string' ? json.result : JSON.stringify(json.result || json);
    } 
    // Strategy 2: Direct REST call to Cloudflare Workers AI API
    else if (this.accountId && this.apiToken) {
      const endpoint = `https://api.cloudflare.com/client/v4/accounts/${this.accountId}/ai/run/${this.model}`;
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${this.apiToken}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          messages: [
            { role: 'system', content: systemPrompt },
            { role: 'user', content: userPrompt }
          ],
          max_tokens: 3000,
          temperature: 0.15,
          response_format: { type: 'json_object' }
        })
      });

      if (!res.ok) {
        throw new Error(`Cloudflare Workers AI API error ${res.status}: ${await res.text()}`);
      }

      const cfData = await res.json();
      rawResponse = cfData.result?.response || cfData.result || '';
    } else {
      throw new Error(
        'Cloudflare Workers AI credentials missing. Set CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN, or CLOUDFLARE_WORKER_URL in your environment variables.'
      );
    }

    return this.parseJsonResponse(rawResponse, targetLang);
  }

  private parseJsonResponse(raw: string | object, targetLang: SupportedTargetLang): TranslatedArticleResult {
    let parsed: any;
    if (typeof raw === 'object' && raw !== null) {
      parsed = raw;
    } else {
      const str = String(raw).trim();
      const match = str.match(/\{[\s\S]*\}/);
      const cleanJson = match ? match[0] : str.replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/```$/i, '').trim();
      try {
        parsed = JSON.parse(cleanJson);
      } catch (err) {
        throw new Error(`Failed to parse JSON response from Cloudflare AI: ${cleanJson.slice(0, 300)}`);
      }
    }

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
