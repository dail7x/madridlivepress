import { getAssetUrl, type DirectusFile } from '@/lib/directus';

/**
 * PDF de una nota de prensa.
 *
 * 1. Principal: campo ya existente en Directus `comunicados.archivo_pdf`
 *    (archivo publicado). No hace falta crear campo ni colección.
 * 2. Alternativa, sin tocar Directus: dejar el PDF en
 *    `src/assets/notas-prensa/2026/<slug>.pdf` y volver a desplegar.
 *    El nombre del archivo (sin .pdf) tiene que coincidir con el slug
 *    de la nota. El campo de Directus tiene prioridad si los dos existen.
 */
type PressPdfItem = {
  slug?: string | null;
  archivo_pdf?: string | DirectusFile | null;
};

const localPdfModules = import.meta.glob('../assets/notas-prensa/**/*.pdf', {
  eager: true,
  query: '?url',
  import: 'default',
}) as Record<string, string>;

const localPdfBySlug: Record<string, string> = {};
for (const [path, url] of Object.entries(localPdfModules)) {
  const file = path.split('/').pop() || '';
  const slug = decodeURIComponent(file.replace(/\.pdf$/i, ''));
  if (slug && typeof url === 'string') localPdfBySlug[slug] = url;
}

export function resolvePressPdfUrl(item: PressPdfItem): string | null {
  if (item.archivo_pdf) {
    const fromDirectus = getAssetUrl(item.archivo_pdf);
    if (fromDirectus) return fromDirectus;
  }
  if (item.slug && localPdfBySlug[item.slug]) return localPdfBySlug[item.slug];
  return null;
}

/** Hay PDF descargable, en Directus o en src/assets/notas-prensa. */
export function hasPressPdf(item: PressPdfItem): boolean {
  return resolvePressPdfUrl(item) != null;
}
