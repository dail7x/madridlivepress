import { directus, readItems, type Comunicado } from '@/lib/directus';

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
