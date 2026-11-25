/**
 * Catálogo de la sección ESTUDIOS.
 * Fuente única: https://nochemadrid.org/campanas-en-locales-ocio-nocturno/
 * Consultado el 25 de noviembre de 2026. No se añaden cifras ni textos
 * que no figuren en esa página. Los títulos de los PDF se reproducen
 * tal como aparecen en los enlaces.
 */

export const ESTUDIOS_SOURCE = {
  url: 'https://nochemadrid.org/campanas-en-locales-ocio-nocturno/',
  title: 'Campañas en locales ocio nocturno',
  publisher: 'Noche Madrid',
  consulted: '2026-11-25',
};

export const ESTUDIOS_INTRO = {
  es: {
    kicker: 'Campañas dirigidas a la dinamización del sector y la promoción turística.',
    paragraphs: [
      'El reconocimiento de la importancia del ocio nocturno como generador de tendencias de consumo está cada vez más presente en los acuerdos de colaboración que Noche Madrid ha suscrito con el Ayuntamiento de Madrid, la Comunidad de Madrid y también con marcas y proveedores.',
      'Gracias a estos proyectos se impulsa una movilidad responsable, la participación en Fitur para reivindicar la importancia turística del ocio nocturno, la celebración de la Gala anual de Navidad y la convocatoria de los Premios Recicla la Noche, entre otras iniciativas que mantienen de actualidad las propuestas del sector recreativo.',
    ],
  },
  en: {
    kicker: 'Campaigns aimed at energising the sector and promoting tourism.',
    paragraphs: [
      'Recognition of nightlife as a source of consumption trends is increasingly present in the collaboration agreements Noche Madrid has signed with Madrid City Council, the Community of Madrid, and also with brands and suppliers.',
      'These projects support responsible mobility, participation in Fitur to assert the tourist importance of nightlife, the annual Christmas Gala, and the Recicla la Noche awards, among other initiatives that keep the recreational sector’s proposals current.',
    ],
  },
};

export interface EstudioLink {
  kind: 'Campaña' | 'Proyecto' | 'Estudio' | 'Colaboración';
  title: string;
  href: string;
  format: 'web' | 'pdf';
}

export const CAMPANAS: EstudioLink[] = [
  { kind: 'Campaña', title: 'Recicla la noche', href: 'https://nochemadrid.org/campana-recicla-la-noche/', format: 'web' },
  { kind: 'Campaña', title: 'Que no te den la lata', href: 'https://nochemadrid.org/campana-que-no-te-den-la-lata/', format: 'web' },
  { kind: 'Campaña', title: 'Vuelve seguro', href: 'https://nochemadrid.org/campana-vuelve-seguro/', format: 'web' },
  { kind: 'Proyecto', title: 'Fiesta is Madrid', href: 'https://fiestaismadrid.es/', format: 'web' },
  { kind: 'Proyecto', title: 'Nightlife in Greater Madrid', href: 'https://nightlifeingreatermadrid.com/es/', format: 'web' },
  { kind: 'Proyecto', title: 'Club del ocio sostenible', href: 'https://nochemadrid.org/guia-de-sostenibilidad-de-locales-de-ocio-y-espectaculos/', format: 'web' },
  {
    kind: 'Proyecto',
    title: 'Plan para impulsar la sostenibilidad y la seguridad de la vida nocturna de Madrid',
    href: 'https://nochemadrid.org/plan-para-impulsar-la-seguridad-y-lasostenibilidad-del-ocio-nocturno/',
    format: 'web',
  },
];

/**
 * Logotipos enlazados bajo «NOCHE MADRID también participa en campañas de
 * otras organizaciones con las que colabora». La página de origen no
 * publica un título junto a cada logo: el nombre sale del propio enlace.
 */
export const COLABORACIONES: EstudioLink[] = [
  { kind: 'Colaboración', title: 'Turismo Madrid', href: 'https://turismomadrid.es/es/', format: 'web' },
  { kind: 'Colaboración', title: 'Todo está en Madrid', href: 'https://todoestaenmadrid.com/', format: 'web' },
  { kind: 'Colaboración', title: 'carnejovenmadrid.com', href: 'https://carnejovenmadrid.com/', format: 'web' },
  { kind: 'Colaboración', title: 'Haz latir el corazón de Madrid', href: 'https://nochemadrid.org/lanzamiento-campana-haz-latir-el-corazon-de-madrid/', format: 'web' },
  { kind: 'Colaboración', title: 'volveremossituvuelves.com', href: 'https://volveremossituvuelves.com/', format: 'web' },
  { kind: 'Colaboración', title: 'Plan de viabilidad', href: 'https://planviabilidad.nochemadrid.org/', format: 'web' },
  { kind: 'Colaboración', title: 'España de Noche', href: 'https://nochemadrid.org/espana-de-noche/', format: 'web' },
  {
    kind: 'Colaboración',
    title: 'Coca-Cola impulsa la acción por el clima en el sector de la hostelería',
    href: 'https://nochemadrid.org/coca-cola-impulsa-la-accion-por-el-clima-en-el-sector-de-la-hosteleria/',
    format: 'web',
  },
];

export const ESTUDIOS_PDF: EstudioLink[] = [
  { kind: 'Estudio', title: 'ESTUDIO IMPORTANCIA TURISTICA OCIO NOCTURNO 2023', href: 'https://nochemadrid.org/wp-content/uploads/2023/04/ESTUDIO-IMPORTANCIA-TURISTICA-OCIO-NOCTURNO.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'ESTUDIO GUSTOS TURISTICOS MADRILEÑOS FIM 2023', href: 'https://nochemadrid.org/wp-content/uploads/2023/04/ESTUDIO-GUSTOS-TURISTICOS-MADRILENOS-FIM-23.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'ESTUDIO SOBRE LA IMPORTANCIA TURISTICA DEL OCIO NOCTURNO FITUR 2022', href: 'https://nochemadrid.org/wp-content/uploads/2022/03/ESTUDIO-SOBRE-LA-IMPORTANCIA-TURISTICA-DEL-OCIO-NOCTURNO-FITUR-2022-2.pdf', format: 'pdf' },
  { kind: 'Estudio', title: '¿CUANTAS GANAS TIENES DE VIAJAR? FITUR 2022', href: 'https://nochemadrid.org/wp-content/uploads/2022/03/¿CUANTAS-GANAS-TIENES-DE-VIAJAR-FITUR-2022-.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'ESTUDIO IMPORTANCIA TURISTICA OCIO NOCTURNO 2021', href: 'https://nochemadrid.org/wp-content/uploads/2021/07/ESTUDIO-IMPORTANCIA-TURISTICA-OCIO-NOCTURNO-FITUR-21.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'ESTUDIO CONSUMO CERVEZA OCIO NOCTURNO 2017', href: 'https://nochemadrid.org/wp-content/uploads/2018/04/2017_ESTUDIO_CONSUMO_CERVEZA_OCIO-NOCTURNO.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'FESTITUR 2018 ESTUDIO OCIO NOCTURNO PREFERENCIAS Y CONSUMOS', href: 'https://nochemadrid.org/wp-content/uploads/2018/04/FESTITUR_2018_ESTUDIO_OCIO_NOCTURNO_PREFERENCIAS_Y_CONSUMOS.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'FESTITUR 2017 PREFERENCIAS Y EL CONSUMO', href: 'https://nochemadrid.org/wp-content/uploads/2018/04/FESTITUR_2017_PREFERENCIAS_Y_EL_CONSUMO.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'FESTITUR 2016 PREFERENCIAS Y CONSUMOS', href: 'https://nochemadrid.org/wp-content/uploads/2018/04/FESTITUR_2016_PREFERENCIAS_Y_CONSUMOS.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'FESTITUR 2015 ESTUDIO SOBRE EL ATRACTIVO TURISTICO DEL OCIO NOCTURNO', href: 'https://nochemadrid.org/wp-content/uploads/2018/04/FESTITUR_2015_ESTUDIO_SOBRE_EL_ATRACTIVO_TURISTICO_DEL_OCIO_NOCTURNO.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'FESTITUR 2014 ESTUDIO SOBRE EL ATRACTIVO TURISTICO DEL OCIO NOCTURNO', href: 'https://nochemadrid.org/wp-content/uploads/2014/10/ESTUDIO-SOBRE-EL-ATRACTIVO-TURISTICO-DEL-OCIO-NOCTURNO.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'INFORME DE RESULTADOS “OCIO NOCTURNO EN LA COMUNIDAD DE MADRID 2010', href: 'https://nochemadrid.org/wp-content/uploads/2010/10/estudiosociologico.pdf', format: 'pdf' },
  { kind: 'Estudio', title: 'ESTUDIO PSICOSOCIAL SOBRE EL IMPACTO DE LA CONTAMINACIÓN ACÚSTICA AMBIENTAL EN SU CIUDADANÍA 2010', href: 'https://nochemadrid.org/wp-content/uploads/2010/10/estudiopsicosocialdelruidomadrid.pdf', format: 'pdf' },
];
