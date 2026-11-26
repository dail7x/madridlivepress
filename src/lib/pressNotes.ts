import { directus, readItems, type Comunicado } from '@/lib/directus';
import { hasPressPdf, pdfFilenameHasNdp, pressPdfFilename } from '@/lib/pressPdf';

/** Categoría principal de nota de prensa oficial. */
export const OFFICIAL_PRESS_CATEGORY_ID = '1';
/** «Proyectos y Campañas» (slug proyectos-y-campanas). */
export const PROJECTS_CAMPAIGNS_CATEGORY_ID = '7';

type CategoryRef = number | string | { id?: number | string | null } | null | undefined;

function categoryId(value: CategoryRef): string | null {
  if (value == null) return null;
  if (typeof value === 'number' || typeof value === 'string') {
    const text = String(value).trim();
    return text || null;
  }
  if (typeof value === 'object' && value.id != null) {
    const text = String(value.id).trim();
    return text || null;
  }
  return null;
}

/**
 * Una nota publicada entra en /notasdeprensa y /en/news si tiene PDF y, además,
 * cumple al menos una de: categoría 1, categoría 7 en categorias_adicionales,
 * o «NDP» en el nombre del PDF.
 */
export function isListedPressNote(item: Comunicado): boolean {
  if (!hasPressPdf(item)) return false;
  if (categoryId(item.categoria) === OFFICIAL_PRESS_CATEGORY_ID) return true;
  const extras = item.categorias_adicionales ?? [];
  if (extras.some((row) => categoryId(row?.categorias_id) === PROJECTS_CAMPAIGNS_CATEGORY_ID)) return true;
  return pdfFilenameHasNdp(pressPdfFilename(item));
}

const PAGE_SIZE = 100;
const MAX_NOTES = 5000;

const FIELDS = [
  'id',
  'status',
  'fecha_publicacion',
  'slug',
  'slug_en',
  'titulo',
  'titulo_en',
  'archivo_pdf.*',
];

/** Todas las notas de prensa publicadas (categoría oficial), sin el tope de una sola página de Directus. */
export async function fetchOfficialPressNotes(): Promise<Comunicado[]> {
  const all: Comunicado[] = [];
  let offset = 0;

  try {
    for (;;) {
      const batch = await directus.request(
        readItems('comunicados' as any, {
          filter: {
            status: { _eq: 'published' },
            categoria: { _eq: 1 },
          },
          sort: ['-fecha_publicacion', '-id'],
          limit: PAGE_SIZE,
          offset,
          fields: FIELDS,
        })
      );
      const items = (batch as Comunicado[]) || [];
      all.push(...items);
      if (items.length < PAGE_SIZE || all.length >= MAX_NOTES) break;
      offset += PAGE_SIZE;
    }
  } catch (error) {
    console.error('Error loading official press notes:', error);
  }

  return all;
}

/**
 * Notas de /notasdeprensa y /en/news.
 * PDF obligatorio y, además, categoría 1, la 7 en `categorias_adicionales`,
 * o «NDP» en el nombre del archivo. Esos campos ya tienen lectura pública.
 */
const LIST_FIELDS = [
  'id',
  'status',
  'fecha_publicacion',
  'slug',
  'slug_en',
  'titulo',
  'titulo_en',
  'categoria',
  'archivo_pdf.id',
  'archivo_pdf.filename_download',
  'categorias_adicionales.categorias_id',
];

export async function fetchOfficialPressNotesWithPdf(): Promise<Comunicado[]> {
  const matched: Comunicado[] = [];
  let offset = 0;

  try {
    for (;;) {
      const batch = await directus.request(
        readItems('comunicados' as any, {
          filter: { status: { _eq: 'published' } },
          sort: ['-fecha_publicacion', '-id'],
          limit: PAGE_SIZE,
          offset,
          fields: LIST_FIELDS,
        })
      );
      const items = (batch as Comunicado[]) || [];
      for (const item of items) {
        if (isListedPressNote(item)) matched.push(item);
      }
      if (items.length < PAGE_SIZE || offset + items.length >= MAX_NOTES) break;
      offset += PAGE_SIZE;
    }
  } catch (error) {
    console.error('Error loading published notes with PDF:', error);
  }

  return matched;
}

/** Los `limit` comunicados más recientes que ya tienen PDF. */
export async function fetchLatestWithPressPdf(
  limit: number,
  options?: { filter?: Record<string, unknown>; fields?: any[] }
): Promise<Comunicado[]> {
  const wanted = Math.max(0, limit);
  if (wanted === 0) return [];

  const fields = [...(options?.fields ?? FIELDS)].map((field) =>
    field === 'archivo_pdf.*' ? 'archivo_pdf' : field
  );
  if (!fields.includes('slug')) fields.push('slug');
  if (!fields.includes('archivo_pdf')) fields.push('archivo_pdf');
  const matched: Comunicado[] = [];
  let offset = 0;

  try {
    while (matched.length < wanted && offset < MAX_NOTES) {
      const batch = await directus.request(
        readItems('comunicados' as any, {
          filter: {
            status: { _eq: 'published' },
            ...(options?.filter ?? {}),
          },
          sort: ['-fecha_publicacion', '-id'],
          limit: PAGE_SIZE,
          offset,
          fields,
        })
      );
      const items = (batch as Comunicado[]) || [];
      for (const item of items) {
        if (!hasPressPdf(item)) continue;
        matched.push(item);
        if (matched.length >= wanted) break;
      }
      if (items.length < PAGE_SIZE) break;
      offset += PAGE_SIZE;
    }
  } catch (error) {
    console.error('Error loading comunicados with PDF:', error);
  }

  return matched;
}
