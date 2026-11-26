import type { APIRoute } from 'astro';
import { fetchOfficialPressNotes } from '@/lib/pressNotes';

export const prerender = false;

const STATIC_PAIRS: Array<[string, string]> = [
  ['/', '/en'],
  ['/notasdeprensa', '/en/news'],
  ['/articulos', '/en/articles'],
  ['/estudios', '/en/studies'],
  ['/cobertura', '/en/coverage'],
  ['/archivo', '/en/archive'],
  ['/press-kits', '/en/press-kits'],
  ['/eventos', '/en/events'],
  ['/acreditaciones', '/en/accreditation'],
  ['/sobre-el-sector', '/en/about'],
];

function xmlEscape(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function absolute(origin: string, path: string): string {
  return `${origin}${path.startsWith('/') ? path : `/${path}`}`;
}

export const GET: APIRoute = async ({ site }) => {
  const origin = (site?.toString() || 'https://nochemadridpress.com').replace(/\/$/, '');
  const notes = await fetchOfficialPressNotes();

  const pairs: Array<{ es: string; en: string; lastmod?: string }> = STATIC_PAIRS.map(([es, en]) => ({ es, en }));

  for (const note of notes) {
    if (!note.slug) continue;
    const es = `/notasdeprensa/${encodeURIComponent(note.slug)}`;
    const enSlug = note.slug_en || note.slug;
    const en = `/en/news/${encodeURIComponent(enSlug)}`;
    const lastmod = note.fecha_publicacion ? note.fecha_publicacion.slice(0, 10) : undefined;
    pairs.push({ es, en, lastmod });
  }

  const urls = pairs.flatMap(({ es, en, lastmod }) => {
    const esUrl = absolute(origin, es);
    const enUrl = absolute(origin, en);
    const alternates = `
    <xhtml:link rel="alternate" hreflang="es" href="${xmlEscape(esUrl)}" />
    <xhtml:link rel="alternate" hreflang="en" href="${xmlEscape(enUrl)}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="${xmlEscape(esUrl)}" />`;
    const lastmodTag = lastmod ? `\n    <lastmod>${xmlEscape(lastmod)}</lastmod>` : '';
    return [esUrl, enUrl].map((loc) => `  <url>
    <loc>${xmlEscape(loc)}</loc>${lastmodTag}${alternates}
  </url>`);
  });

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${urls.join('\n')}
</urlset>
`;

  return new Response(body, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
