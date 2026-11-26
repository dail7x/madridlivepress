/**
 * Cobertura en medios de Noche Madrid durante 2026.
 * Fuente: clipping verificado (38 piezas). Se excluye la de Madrid Actual
 * «Ocio nocturno: 40 millones en Nochevieja» (30 dic 2025): figuraba
 * enlazada desde FITUR 2026, pero trata de Nochevieja 2025.
 * Orden: fecha descendente; dentro del mismo día se conserva el orden de la fuente.
 */

export interface CoberturaItem {
  medio: string;
  titular: string;
  /** ISO 8601, YYYY-MM-DD */
  fecha: string;
  url: string;
  /** Artículo de origen en nochemadrid.org, si existe. */
  origen: string;
}

const COBERTURA_FUENTE: CoberturaItem[] = [
  {
    medio: "Espacio Diario",
    titular: "Los Premios Noche Madrid 2026 ponen el foco en el tardeo, los nuevos aforos y la reducción del ruido",
    fecha: "2026-11-24",
    url: "https://espaciodiario.com/los-premios-noche-madrid-2026-ponen-el-foco-en-el-tardeo-los-nuevos-aforos-y-la-reduccion-del-ruido/",
    origen: "https://nochemadrid.org/iv-edicion-de-los-premios-noche-madrid/",
  },
  {
    medio: "Café con Podcast",
    titular: "Premios Noche Madrid 2026: aforos, tardeo y la lucha contra el ruido",
    fecha: "2026-11-24",
    url: "https://cafeconpodcast.com/premios-noche-madrid-2026-aforos-tardeo-y-la-lucha-contra-el-ruido/",
    origen: "https://nochemadrid.org/iv-edicion-de-los-premios-noche-madrid/",
  },
  {
    medio: "Espacio Diario",
    titular: "Noche Madrid impulsa la alianza entre el ocio nocturno y el turismo MICE en IBTM World",
    fecha: "2026-11-19",
    url: "https://espaciodiario.com/noche-madrid-impulsa-la-alianza-entre-el-ocio-nocturno-y-el-turismo-mice-en-ibtm-world/",
    origen: "https://nochemadrid.org/noche-madrid-refuerza-el-maridaje-entre-la-vida-nocturna-y-el-turismo-mice-en-ibtm-world/",
  },
  {
    medio: "Madrid es Noticia",
    titular: "Los locales de ocio de Centro mejoran sus protocolos para reducir el ruido",
    fecha: "2026-11-13",
    url: "https://www.madridesnoticia.es/2026/11/locales-de-ocio-ruido-calles/",
    origen: "https://nochemadrid.org/el-desalojo-ordenado-y-la-venta-anticipada-las-medidas-mas-eficaces-para-reducir-el-impacto-ambiental-del-ocio-nocturno-en-centro/",
  },
  {
    medio: "La Razón",
    titular: "El Ayuntamiento de Madrid presenta un plan para reducir el ruido del ocio nocturno",
    fecha: "2026-11-13",
    url: "https://www.larazon.es/madrid/ayuntamiento-madrid-presenta-plan-reducir-ruido-ocio-nocturno_202611136af702f503bbf30bb04af66c.html",
    origen: "https://nochemadrid.org/el-desalojo-ordenado-y-la-venta-anticipada-las-medidas-mas-eficaces-para-reducir-el-impacto-ambiental-del-ocio-nocturno-en-centro/",
  },
  {
    medio: "Espacio Diario",
    titular: "La venta anticipada y el cierre escalonado lideran las medidas contra el ruido nocturno en Centro",
    fecha: "2026-11-13",
    url: "https://espaciodiario.com/la-venta-anticipada-y-el-cierre-escalonado-lideran-las-medidas-contra-el-ruido-nocturno-en-centro/",
    origen: "https://nochemadrid.org/el-desalojo-ordenado-y-la-venta-anticipada-las-medidas-mas-eficaces-para-reducir-el-impacto-ambiental-del-ocio-nocturno-en-centro/",
  },
  {
    medio: "El Periódico de España",
    titular: "Madrid pone el foco en el ruido del ocio nocturno: desalojos ordenados, menos colas y limpieza para mejorar la convivencia",
    fecha: "2026-11-13",
    url: "https://www.epe.es/es/madrid/20261113/madrid-pone-foco-ruido-ocio-136409904",
    origen: "https://nochemadrid.org/el-desalojo-ordenado-y-la-venta-anticipada-las-medidas-mas-eficaces-para-reducir-el-impacto-ambiental-del-ocio-nocturno-en-centro/",
  },
  {
    medio: "El Diario de Madrid",
    titular: "Se prevé que Halloween supere a Nochevieja como la noche de mayor facturación para el ocio nocturno",
    fecha: "2026-10-31",
    url: "https://www.eldiariodemadrid.es/articulo/sociedad/halloween-facturacion-ocio-nocturno-empleo-espana/20261031164228145789.html",
    origen: "https://nochemadrid.org/halloween-adelanta-a-nochevieja-como-la-celebracion-con-mayor-peso-economico-para-el-ocio-nocturno-madrileno/",
  },
  {
    medio: "Espacio Diario",
    titular: "Noche Madrid, Transexualia y Stipendium se unen por la inserción laboral del colectivo trans",
    fecha: "2026-10-21",
    url: "https://espaciodiario.com/noche-madrid-transexualia-y-stipendium-se-unen-por-la-insercion-laboral-del-colectivo-trans/",
    origen: "https://nochemadrid.org/noche-madrid-transexualia-y-stipendium-colaboran-para-impulsar-la-insercion-laboral-de-las-personas-trans/",
  },
  {
    medio: "Madridiario",
    titular: "Más formación, más control y menos ruido: Madrid refuerza su plan para el ocio nocturno",
    fecha: "2026-10-07",
    url: "https://www.madridiario.es/mas-formacion-control-menos-ruido-madrid-refuerza-plan-ocio-nocturno",
    origen: "https://nochemadrid.org/la-junta-municipal-del-distrito-centro-y-noche-madrid-ponen-en-marcha-el-plan-para-impulsar-la-sostenibilidad-y-la-seguridad-de-la-vida-nocturna-de-madrid/",
  },
  {
    medio: "Ayuntamiento de Madrid (Diario de Madrid)",
    titular: "Centro impulsa la seguridad y la sostenibilidad del ocio nocturno con la campaña ‘La fiesta está dentro del club #EnLaCalleSilencio’",
    fecha: "2026-10-07",
    url: "https://diario.madrid.es/blog/notas-de-prensa/centro-impulsa-la-seguridad-y-la-sostenibilidad-del-ocio-nocturno-con-la-campana-la-fiesta-esta-dentro-del-club-enlacallesilencio",
    origen: "https://nochemadrid.org/la-junta-municipal-del-distrito-centro-y-noche-madrid-ponen-en-marcha-el-plan-para-impulsar-la-sostenibilidad-y-la-seguridad-de-la-vida-nocturna-de-madrid/",
  },
  {
    medio: "Europa Press",
    titular: "Empresarios de ocio nocturno piden replantear las inspecciones y redadas en locales por \"desproporcionadas y vejatorias\"",
    fecha: "2026-09-30",
    url: "https://www.europapress.es/madrid/noticia-empresarios-ocio-nocturno-piden-replantear-inspecciones-redadas-locales-desproporcionadas-vejatorias-20260930125240.html",
    origen: "https://nochemadrid.org/noche-madrid-reclama-inspecciones-laborales-que-no-paralicen-la-actividad-de-los-locales-ni-supongan-un-trato-vejatorio-para-los-clientes/",
  },
  {
    medio: "Que.es",
    titular: "La Fórmula 1 llega a Madrid con una factura millonaria para bares, discotecas y locales de ocio",
    fecha: "2026-09-07",
    url: "https://www.que.es/2026/09/07/formula-1-madrid-bares",
    origen: "https://nochemadrid.org/el-ocio-nocturno-arranca-en-madrid-a-ritmo-de-formula-1/",
  },
  {
    medio: "Europa Press",
    titular: "El ocio nocturno madrileño espera que la F1 deje un \"notable\" impacto económico cercano a los unos 30 millones",
    fecha: "2026-09-07",
    url: "https://www.europapress.es/madrid/noticia-ocio-nocturno-madrileno-espera-f1-deje-notable-impacto-economico-cercano-30-millones-20260907152957.html",
    origen: "https://nochemadrid.org/el-ocio-nocturno-arranca-en-madrid-a-ritmo-de-formula-1/",
  },
  {
    medio: "ABC",
    titular: "La Fórmula 1 dejará unos 30 millones de euros en el ocio nocturno madrileño",
    fecha: "2026-09-07",
    url: "https://www.abc.es/espana/madrid/formula-dejara-millones-euros-ocio-nocturno-madrileno-20260907145535-nt.html",
    origen: "https://nochemadrid.org/el-ocio-nocturno-arranca-en-madrid-a-ritmo-de-formula-1/",
  },
  {
    medio: "Telemadrid",
    titular: "Madrid, donde el turismo nunca descansa",
    fecha: "2026-08-14",
    url: "https://www.telemadrid.es/programas/telenoticias-1/Madrid-donde-el-turismo-nunca-descansa-2-2916328346--20260814025906.html",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "Madridiario",
    titular: "La noche madrileña atrae al turismo: se esperan dos millones de visitantes en bares, terrazas y discotecas este verano",
    fecha: "2026-08-14",
    url: "https://www.madridiario.es/noche-madrilena-atrae-turismo-dos-millones-visitantes-bares-terrazas-discotecas-verano",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "La Voz de Madrid",
    titular: "Madrid, destino líder de ocio nocturno este verano",
    fecha: "2026-08-14",
    url: "https://lavozmadrid.es/madrid-capital/general/madrid-destino-lider-de-ocio-nocturno-este-verano",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "La Razón",
    titular: "Esto es lo que gasta de media un turista en Madrid una noche de agosto",
    fecha: "2026-08-14",
    url: "https://www.larazon.es/madrid/esto-que-gasta-media-turista-madrid-noche-agosto-90-euros_202608146a7edc60a046ad6ebcb0abfb.html",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "Europa Press",
    titular: "Cerca de dos millones de turistas saldrán por la noche este verano en Madrid gastando 90 euros por persona de media",
    fecha: "2026-08-14",
    url: "https://www.europapress.es/madrid/noticia-cerca-dos-millones-turistas-saldran-noche-verano-madrid-gastando-90-euros-persona-media-20260814105447.html",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "Crónica Madrid",
    titular: "Cerca de dos millones de turistas disfrutarán de la vibrante vida nocturna de Madrid este verano",
    fecha: "2026-08-14",
    url: "https://www.cronicamadrid.com/noticia/1308001/capital/cerca-de-dos-millones-de-turistas-disfrutaran-de-la-vibrante-vida-nocturna-de-madrid-este-verano.html",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "Comunidad de Madrid",
    titular: "La Comunidad de Madrid, elegida por el 64% de sus visitantes como destino de ocio nocturno para este verano",
    fecha: "2026-08-14",
    url: "https://www.comunidad.madrid/noticias/2026/08/14/comunidad-madrid-elegida-64-visitantes-destino-ocio-nocturno-este-verano",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "ABC",
    titular: "El turista en Madrid sale al menos una noche y se deja 90 euros de media",
    fecha: "2026-08-14",
    url: "https://www.abc.es/espana/madrid/madrid-visita-noche-dos-millones-turistas-salir-20260814160546-nt.html",
    origen: "https://nochemadrid.org/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano/",
  },
  {
    medio: "Telemadrid",
    titular: "Madrid lidera ‘el tardeo’ con más del 25% de la facturación de los locales de la ciudad",
    fecha: "2026-08-05",
    url: "https://www.telemadrid.es/noticias/madrid/Madrid-lidera-el-tardeo-con-mas-del-25-de-la-facturacion-de-los-locales-de-la-ciudad-0-2913608628--20260805123627.html",
    origen: "https://nochemadrid.org/madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional/",
  },
  {
    medio: "El Mundo",
    titular: "Madrid lidera el tardeo en España, desplazando al aperitivo: el gasto medio alcanza los 45 euros y el 59% de los locales ya lo ofrece",
    fecha: "2026-08-05",
    url: "https://www.elmundo.es/madrid/2026/08/06/6a73577be9cf4ac1368b4583.html",
    origen: "https://nochemadrid.org/madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional/",
  },
  {
    medio: "El Economista",
    titular: "Madrid se corona como la capital del tardeo: ya genera el 26,3% de la facturación de los locales de ocio",
    fecha: "2026-08-05",
    url: "https://www.eleconomista.es/economia/noticias/14006644/08/26/madrid-se-corona-como-la-capital-del-tardeo-ya-genera-el-263-de-la-facturacion-de-los-locales-de-ocio.html",
    origen: "https://nochemadrid.org/madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional/",
  },
  {
    medio: "Espacio Diario",
    titular: "El público del MADO lo tiene claro: la noche es imprescindible en el Orgullo",
    fecha: "2026-07-03",
    url: "https://espaciodiario.com/el-publico-del-mado-lo-tiene-claro-la-noche-es-imprescindible-en-el-orgullo/",
    origen: "https://nochemadrid.org/el-publico-del-orgullo-situa-la-vida-nocturna-como-una-parte-esencial-de-la-experiencia-del-mado/",
  },
  {
    medio: "Telemadrid",
    titular: "La celebración del Orgullo dejará 50 millones en el ocio cultural y nocturno de la capital",
    fecha: "2026-06-27",
    url: "https://www.telemadrid.es/noticias/madrid/La-celebracion-del-Orgullo-dejara-50-millones-en-el-ocio-cultural-y-nocturno-de-la-capital-0-2901909787--20260627093536.html",
    origen: "https://nochemadrid.org/el-publico-del-orgullo-situa-la-vida-nocturna-como-una-parte-esencial-de-la-experiencia-del-mado/",
  },
  {
    medio: "Madridiario",
    titular: "Alejandro Zamarro, nuevo presidente de Noche Madrid",
    fecha: "2026-03-25",
    url: "https://www.madridiario.es/alejandro-zamarro-nuevo-presidente-noche-madrid",
    origen: "https://nochemadrid.org/alejandro-zamarro-nuevo-presidente-de-noche-madrid/",
  },
  {
    medio: "El Mundo",
    titular: "Alejandro Zamarro, nuevo presidente de la asociación Noche Madrid",
    fecha: "2026-03-25",
    url: "https://www.elmundo.es/madrid/2026/03/25/69c40353fc6c83e36d8b459e.html",
    origen: "https://nochemadrid.org/alejandro-zamarro-nuevo-presidente-de-noche-madrid/",
  },
  {
    medio: "El Español",
    titular: "Alejandro, el nuevo líder de los empresarios del ocio nocturno: luchará por la 'crisis de aforos'",
    fecha: "2026-03-25",
    url: "https://www.elespanol.com/madrid/ocio/20260325/alejandro-socio-varias-discotecas-lidera-empresarios-ocio-nocturno-luchara-crisis-aforos/1003744183263_0.html",
    origen: "https://nochemadrid.org/alejandro-zamarro-nuevo-presidente-de-noche-madrid/",
  },
  {
    medio: "Europa Press",
    titular: "El 100% de los locales adscritos a una iniciativa regional para la sostenibilidad del ocio nocturno usa iluminación LED",
    fecha: "2026-03-06",
    url: "https://www.europapress.es/madrid/noticia-100-locales-adscritos-iniciativa-regional-sostenibilidad-ocio-nocturno-usa-iluminacion-led-20260306134948.html",
    origen: "https://nochemadrid.org/el-ocio-nocturno-madrileno-consolida-su-transicion-sostenible/",
  },
  {
    medio: "El Mundo",
    titular: "Los locales de ocio nocturno cambian su consumo energético a sistemas de climatización eficiente y luces led",
    fecha: "2026-03-06",
    url: "https://www.elmundo.es/madrid/2026/03/06/69aadc11fdddff76298b45ab.html",
    origen: "https://nochemadrid.org/el-ocio-nocturno-madrileno-consolida-su-transicion-sostenible/",
  },
  {
    medio: "Comunidad de Madrid",
    titular: "La Comunidad de Madrid, en la entrega de diplomas a 18 locales de ocio por su compromiso en el cuidado del medio ambiente",
    fecha: "2026-03-06",
    url: "https://www.comunidad.madrid/notas-prensa/2026/03/06/comunidad-madrid-entrega-diplomas-18-locales-ocio-su-compromiso-cuidado-medio-ambiente",
    origen: "https://nochemadrid.org/el-ocio-nocturno-madrileno-consolida-su-transicion-sostenible/",
  },
  {
    medio: "Telemadrid",
    titular: "Fitur generará un impacto económico de casi 17 millones en el ocio nocturno madrileño",
    fecha: "2026-01-15",
    url: "https://www.telemadrid.es/programas/telenoticias-1/FITUR-generara-un-impacto-economico-de-casi-17-millones-en-el-ocio-nocturno-madrileno-2-2853034689--20260115024923.html",
    origen: "https://nochemadrid.org/presentacion-de-la-xii-edicion-de-fiesta-is-madrid-en-fitur-2026/",
  },
  {
    medio: "Europa Press",
    titular: "Noche Madrid estima que Fitur generará casi 17 millones por las más de 230.000 salidas nocturnas de profesionales",
    fecha: "2026-01-15",
    url: "https://www.europapress.es/madrid/noticia-noche-madrid-estima-fitur-generara-casi-17-millones-mas-230000-salidas-nocturnas-profesionales-20260115134843.html",
    origen: "https://nochemadrid.org/presentacion-de-la-xii-edicion-de-fiesta-is-madrid-en-fitur-2026/",
  },
  {
    medio: "El Diario de Madrid",
    titular: "Fitur generará un impacto económico de casi 17 millones de euros en el ocio nocturno madrileño",
    fecha: "2026-01-15",
    url: "https://www.eldiariodemadrid.es/articulo/turismo/fitur-generara-impacto-economico-casi-17-millones-euros-ocio-nocturno-madrileno-mas-230000-salidas-nocturnas/20260115143342118342.html",
    origen: "https://nochemadrid.org/presentacion-de-la-xii-edicion-de-fiesta-is-madrid-en-fitur-2026/",
  },
];

export const COBERTURA: CoberturaItem[] = [...COBERTURA_FUENTE].sort((a, b) => {
  if (a.fecha === b.fecha) return 0;
  return a.fecha < b.fecha ? 1 : -1;
});

export const COBERTURA_TOTAL = COBERTURA.length;

const MESES_ES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
const MESES_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const MESES_CORTOS_ES = ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEP', 'OCT', 'NOV', 'DIC'];
const MESES_CORTOS_EN = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];

function partes(iso: string) {
  const [year, month, day] = iso.split('-');
  const index = Number(month) - 1;
  return { year, month, day, index };
}

export function formatCoberturaFecha(iso: string, lang: 'es' | 'en' = 'es'): string {
  const { year, day, index } = partes(iso);
  const mes = (lang === 'en' ? MESES_CORTOS_EN : MESES_CORTOS_ES)[index];
  return `${Number(day)} ${mes} ${year}`;
}

export function formatCoberturaMes(iso: string, lang: 'es' | 'en' = 'es'): string {
  const { year, index } = partes(iso);
  const mes = (lang === 'en' ? MESES_EN : MESES_ES)[index];
  return `${mes} ${year}`;
}

export interface CoberturaGrupo {
  key: string;
  label: string;
  items: CoberturaItem[];
}

export function coberturaAgrupada(lang: 'es' | 'en' = 'es'): CoberturaGrupo[] {
  const groups: CoberturaGrupo[] = [];
  for (const item of COBERTURA) {
    const key = item.fecha.slice(0, 7);
    const last = groups[groups.length - 1];
    if (!last || last.key !== key) {
      groups.push({ key, label: formatCoberturaMes(item.fecha, lang), items: [item] });
    } else {
      last.items.push(item);
    }
  }
  return groups;
}

export function coberturaReciente(limit = 6): CoberturaItem[] {
  return COBERTURA.slice(0, limit);
}

/** Medios que aparecen en el clipping, del que más publica al que menos. */
export function mediosCobertura(): string[] {
  const counts = new Map<string, number>();
  for (const item of COBERTURA) {
    counts.set(item.medio, (counts.get(item.medio) ?? 0) + 1);
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'es'))
    .map(([medio]) => medio);
}
