import { createDirectus, rest, staticToken, readItems } from '@directus/sdk';

export const DIRECTUS_URL = import.meta.env.DIRECTUS_URL || import.meta.env.PUBLIC_DIRECTUS_URL || 'https://mlpdirectus.116.203.118.1.sslip.io';
export const DIRECTUS_TOKEN = import.meta.env.DIRECTUS_STATIC_TOKEN || 'mlp_secret_directus_token_2026';

// Directus Client for SSR
export const directus = createDirectus(DIRECTUS_URL)
  .with(staticToken(DIRECTUS_TOKEN))
  .with(rest());

// Type Definitions
export interface DirectusFile {
  id: string;
  filename_download?: string;
  title?: string;
  type?: string;
  filesize?: number;
  width?: number;
  height?: number;
}

export interface Categoria {
  id: string;
  nombre: string;
  slug: string;
  descripcion?: string;
  color?: string;
}

export interface Portavoz {
  id: string;
  nombre: string;
  cargo: string;
  bio?: string;
  avatar?: string | DirectusFile;
  email_prensa?: string;
}

export interface Comunicado {
  id: string;
  status: 'published' | 'draft' | 'archived';
  fecha_publicacion: string;
  slug: string;
  titulo: string;
  bajada?: string;
  cuerpo?: string;
  imagen_portada?: string | DirectusFile;
  archivo_pdf?: string | DirectusFile;
  categoria?: string | Categoria;
  portavoz?: string | Portavoz;
  audio_video_url?: string;
  destacado?: boolean;
  tags?: string[];
}

export interface Sala {
  id: string;
  status: 'published' | 'draft' | 'archived';
  nombre: string;
  slug: string;
  tipo_espacio: 'discoteca' | 'sala_conciertos' | 'teatro_musical' | 'tablao' | 'bar_especial';
  distrito: string;
  direccion: string;
  aforo?: number;
  descripcion?: string;
  logo?: string | DirectusFile;
  imagen_portada?: string | DirectusFile;
  contacto_prensa_nombre?: string;
  contacto_prensa_email?: string;
  contacto_prensa_telefono?: string;
  dossier_pdf?: string | DirectusFile;
  sitio_web?: string;
  instagram?: string;
  destacado?: boolean;
}

export interface RecursoPrensa {
  id: string;
  status: string;
  titulo: string;
  categoria_recurso: 'logos' | 'b_roll' | 'fotografia' | 'informes' | 'infografias';
  descripcion?: string;
  archivo?: string | DirectusFile;
  formato?: string;
  peso?: string;
  imagen_previa?: string | DirectusFile;
}

export interface Evento {
  id: string;
  status: string;
  titulo: string;
  slug: string;
  fecha_evento: string;
  sala?: string | Sala;
  categoria?: string;
  descripcion?: string;
  imagen_portada?: string | DirectusFile;
  pases_prensa_disponibles?: boolean;
  fecha_limite_acreditacion?: string;
}

// Block Types for Page Builder (Many-to-Any)
export interface BlockHero {
  id: string;
  titular: string;
  subtitulo?: string;
  tipo_fondo: 'imagen' | 'video';
  fondo?: string | DirectusFile;
  cta_texto?: string;
  cta_enlace?: string;
  nota_prioritaria?: string | Comunicado;
}

export interface BlockPressGrid {
  id: string;
  titular: string;
  mostrar_filtro_categorias?: boolean;
  mostrar_descarga_pdf?: boolean;
  limite?: number;
  categoria_destacada?: string | Categoria;
}

export interface BlockRichText {
  id: string;
  titulo?: string;
  contenido?: string;
  cita_texto?: string;
  cita_autor?: string;
  cita_cargo?: string;
  cita_avatar?: string | DirectusFile;
}

export interface BlockMediaKit {
  id: string;
  titulo: string;
  descripcion?: string;
  archivo_zip?: string | DirectusFile;
  tamanio_formato?: string;
  imagen_previa?: string | DirectusFile;
  especificaciones?: string;
}

export interface BlockVenuesMap {
  id: string;
  titulo: string;
  descripcion?: string;
  distrito_defecto?: string;
  tipo_local_defecto?: string;
}

export interface BlockNewsletter {
  id: string;
  titulo: string;
  descripcion?: string;
  placeholder_input?: string;
  texto_boton?: string;
  texto_privacidad?: string;
}

export type PageBlockItem =
  | ({ collection: 'block_hero'; item: BlockHero })
  | ({ collection: 'block_press_grid'; item: BlockPressGrid })
  | ({ collection: 'block_rich_text'; item: BlockRichText })
  | ({ collection: 'block_media_kit'; item: BlockMediaKit })
  | ({ collection: 'block_venues_map'; item: BlockVenuesMap })
  | ({ collection: 'block_newsletter'; item: BlockNewsletter });

export interface Pagina {
  id: string;
  status: 'published' | 'draft' | 'archived';
  title: string;
  slug: string;
  seo_title?: string;
  seo_description?: string;
  seo_image?: string | DirectusFile;
  bloques?: PageBlockItem[];
}

/**
 * Helper to build Directus Asset URL with transformation options
 */
export function getAssetUrl(
  fileOrId: string | DirectusFile | null | undefined,
  options?: { width?: number; height?: number; quality?: number; format?: string }
): string {
  if (!fileOrId) return '';
  const id = typeof fileOrId === 'string' ? fileOrId : fileOrId.id;
  if (!id) return '';

  const params = new URLSearchParams();
  if (options?.width) params.set('width', options.width.toString());
  if (options?.height) params.set('height', options.height.toString());
  if (options?.quality) params.set('quality', options.quality.toString());
  if (options?.format) params.set('format', options.format);

  const query = params.toString();
  return `${DIRECTUS_URL}/assets/${id}${query ? `?${query}` : ''}`;
}

/**
 * Fetch a Page with its M2A Blocks
 */
export async function getPageBySlug(slug: string): Promise<Pagina | null> {
  try {
    const formattedSlug = slug.startsWith('/') ? slug : `/${slug}`;
    const cleanSlug = formattedSlug === '//' ? '/' : formattedSlug;

    const items = await directus.request(
      readItems('paginas' as any, {
        filter: {
          slug: { _eq: cleanSlug },
          status: { _eq: 'published' },
        },
        fields: [
          'id',
          'status',
          'title',
          'slug',
          'seo_title',
          'seo_description',
          'seo_image.*',
          {
            bloques: [
              'id',
              'collection',
              'sort',
              {
                item: {
                  block_hero: ['id', 'titular', 'subtitulo', 'tipo_fondo', 'fondo.*', 'cta_texto', 'cta_enlace', { nota_prioritaria: ['id', 'titulo', 'slug', 'fecha_publicacion', 'bajada', 'imagen_portada.*'] }],
                  block_press_grid: ['id', 'titular', 'mostrar_filtro_categorias', 'mostrar_descarga_pdf', 'limite', { categoria_destacada: ['id', 'nombre', 'slug'] }],
                  block_rich_text: ['id', 'titulo', 'contenido', 'cita_texto', 'cita_autor', 'cita_cargo', 'cita_avatar.*'],
                  block_media_kit: ['id', 'titulo', 'descripcion', 'archivo_zip.*', 'tamanio_formato', 'imagen_previa.*', 'especificaciones'],
                  block_venues_map: ['id', 'titulo', 'descripcion', 'distrito_defecto', 'tipo_local_defecto'],
                  block_newsletter: ['id', 'titulo', 'descripcion', 'placeholder_input', 'texto_boton', 'texto_privacidad'],
                },
              },
            ],
          },
        ],
        limit: 1,
      })
    );

    return (items && (items as any)[0]) || null;
  } catch (error) {
    console.error(`Error fetching page with slug "${slug}":`, error);
    return null;
  }
}
