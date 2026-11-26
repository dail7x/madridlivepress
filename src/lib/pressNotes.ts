import { directus, readItems, type Comunicado } from '@/lib/directus';
import { hasPressPdf } from '@/lib/pressPdf';

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
 * Comunicados publicados con PDF, de cualquier categoría.
 * La lista de notas no puede quedarse en la categoría 1: en Directus hay
 * archivos también en estudios, festivales y el resto. Se pide el id de
 * `archivo_pdf` (no `archivo_pdf.*`) para no depender del permiso de lectura
 * de `directus_files`.
 */
export async function fetchOfficialPressNotesWithPdf(): Promise<Comunicado[]> {
  const fields = FIELDS.map((field) => (field === 'archivo_pdf.*' ? 'archivo_pdf' : field));
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
          fields,
        })
      );
      const items = (batch as Comunicado[]) || [];
      for (const item of items) {
        if (hasPressPdf(item)) matched.push(item);
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
