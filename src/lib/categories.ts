import type { Categoria } from '@/lib/directus';

/** Categoría «Artes Escénicas» (Directus id 4). No se borra del CMS: solo se oculta. */
export const HIDDEN_CATEGORY_IDS = new Set(['4']);

export const HIDDEN_CATEGORY_SLUGS = new Set([
  'artes-escenicas',
  'artes-escénicas',
  'performing-arts',
]);

export function isHiddenCategory(cat?: Partial<Categoria> | string | null): boolean {
  if (!cat) return false;
  if (typeof cat === 'string') {
    const value = cat.trim().toLowerCase();
    return HIDDEN_CATEGORY_IDS.has(value) || HIDDEN_CATEGORY_SLUGS.has(value) || value.includes('artes escén') || value.includes('artes escen') || value.includes('performing art');
  }
  const id = cat.id != null ? String(cat.id) : '';
  if (HIDDEN_CATEGORY_IDS.has(id)) return true;
  const slugs = [cat.slug, cat.slug_en].filter(Boolean).map((slug) => String(slug).toLowerCase());
  if (slugs.some((slug) => HIDDEN_CATEGORY_SLUGS.has(slug))) return true;
  const names = [cat.nombre, cat.nombre_en].filter(Boolean).join(' ').toLowerCase();
  return names.includes('artes escén') || names.includes('artes escen') || names.includes('performing art');
}

export function filterVisibleCategories<T extends Partial<Categoria>>(categories: T[]): T[] {
  return categories.filter((category) => !isHiddenCategory(category));
}

/** Quita la etiqueta de una categoría oculta sin eliminar la publicación. */
export function scrubHiddenCategory<T extends { categoria?: unknown }>(item: T): T {
  const cat = item.categoria as Partial<Categoria> | string | null | undefined;
  if (cat && isHiddenCategory(cat)) {
    return { ...item, categoria: undefined };
  }
  return item;
}
