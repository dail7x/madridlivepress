import fs from 'node:fs';

const DIRECTUS_URL = 'https://mlpdirectus.116.203.118.1.sslip.io';
const DIRECTUS_TOKEN = 'mlp_secret_directus_token_2026';
const LOCAL_API = 'http://localhost:3001/api';

const articles = [
  {
    titulo: 'La Junta Municipal del Distrito Centro y Noche Madrid ponen en marcha el plan para impulsar la sostenibilidad y la seguridad de la vida nocturna de Madrid',
    slug: 'la-junta-municipal-del-distrito-centro-y-noche-madrid-ponen-en-marcha-el-plan-para-impulsar-la-sostenibilidad-y-la-seguridad-de-la-vida-nocturna-de-madrid',
    fecha_publicacion: '2026-10-07T16:25:00',
    status: 'published',
    categoria: 3, // Sostenibilidad & Innovación
    portavoz: 1, // Vicente Pizcueta
    destacado: true,
    imagen_url_externa: 'https://nochemadrid.org/wp-content/uploads/2026/10/PLAN-PARA-IMPULSAR-LA-SOSTENIBILIDAD-Y-LA-SEGURIDAD-DE-LA-VIDA-NOCTURNA-DE-MADRID-1A.webp',
    tags: ['Distrito Centro', 'Sostenibilidad', 'Seguridad', 'Ruido Nocturno', 'Policía Municipal', 'Convivencia Vecinal'],
    bajada: 'Los locales participantes en la campaña de 2025 incrementaron un 34,5% la adopción de medidas preventivas para reducir el ruido y mejorar la gestión del entorno nocturno. La nueva edición amplía su actuación a la vía pública y refuerza la coordinación con la Policía Municipal.',
    cuerpo: `<p>La Junta Municipal del <strong>Distrito Centro del Ayuntamiento de Madrid</strong> y la Asociación de Empresarios de Ocio y Espectáculos de la Comunidad de Madrid, <strong>Noche Madrid</strong>, ponen en marcha el <strong>PLAN PARA IMPULSAR LA SOSTENIBILIDAD Y LA SEGURIDAD DEL OCIO NOCTURNO</strong>.</p>

<blockquote class="destacado">
  <p>Los locales participantes en la campaña de 2025 incrementaron un 34,5% la adopción de medidas preventivas para reducir el ruido y mejorar la gestión del entorno nocturno. La nueva edición amplía su actuación a la vía pública y a los distintos focos de ruido nocturno.</p>
</blockquote>

<p>Tras los buenos resultados obtenidos en 2025, el nuevo plan amplía el ámbito de la campaña <strong>#ENLACALLESILENCIO</strong> más allá del entorno inmediato de los locales de ocio para actuar en la vía pública y abordar de forma conjunta los distintos focos emisores de ruido nocturno.</p>

<p>El plan contempla también la creación de un <strong>grupo de trabajo</strong> para reforzar la <strong>coordinación y colaboración del sector del ocio con la Policía Municipal de Madrid</strong>.</p>

<p>Los <strong>locales participantes en la campaña de 2025 incrementaron un 34,5% la adopción de medidas preventivas para reducir el ruido y mejorar la gestión del entorno nocturno</strong>. En concreto, el grado de implantación pasó del 45,8% antes de la campaña al 61,6% al finalizarla.</p>

<p>El ranking de las <strong>medidas más implantadas</strong> estuvo encabezado por los <strong>protocolos de desalojo ordenado</strong> y la <strong>limpieza del entorno</strong>, seguidos de la venta anticipada y online de entradas, el escaneo de <strong>códigos QR</strong> y la <strong>ampliación de los horarios del personal de admisión</strong>.</p>`,
    puntos_clave: [
      'Incremento del 34,5%: Los locales participantes pasaron del 45,8% al 61,6% de implantación de medidas preventivas contra el ruido.',
      'Medidas prioritarias: Protocolos de desalojo escalonado y ordenado, limpieza activa del perímetro y control mediante ticketing QR.',
      'Acción en vía pública: La campaña #ENLACALLESILENCIO se extiende a los espacios abiertos y flujos peatonales del Distrito Centro.',
      'Mesa policial: Creación de un grupo de trabajo específico y permanente con la Policía Municipal de Madrid.'
    ],
    audio_script_es: 'Noche Madrid Press presenta el nuevo plan conjunto entre la Junta Municipal de Distrito Centro y Noche Madrid para potenciar la sostenibilidad y seguridad en la vida nocturna de la capital. Tras lograr que los locales adheridos incrementaran un 34,5% sus medidas preventivas contra el ruido ambiental, la iniciativa evoluciona extendiendo la campaña En La Calle Silencio a los espacios públicos y articulando un grupo de trabajo directo con la Policía Municipal de Madrid.',
    audio_habilitado: true
  },
  {
    titulo: 'Noche Madrid, Transexualia y Stipendium colaboran para impulsar la inserción laboral de las personas trans',
    slug: 'noche-madrid-transexualia-y-stipendium-colaboran-para-impulsar-la-insercion-laboral-de-las-personas-trans',
    fecha_publicacion: '2026-10-21T14:50:00',
    status: 'published',
    categoria: 1, // Institucional & Economía
    portavoz: 1, // Vicente Pizcueta
    destacado: true,
    imagen_url_externa: 'https://nochemadrid.org/wp-content/uploads/2026/10/NOCHE-MADRID-TRANSEXUALIA-Y-STIPENDIUM-COLABORAN-PARA-IMPULSAR-LA-INSERCION-LABORAL-DE-LAS-PERSONAS-TRANS-1a.webp',
    tags: ['Inserción Laboral', 'Diversidad', 'Personas Trans', 'Empleabilidad', 'Transexualia', 'Stipendium', 'Compromiso Social'],
    bajada: 'Noche Madrid, la Asociación Transexualia y Stipendium Te Ayuda firman un convenio de colaboración para abrir oportunidades de empleo a personas trans y colectivos con barreras de acceso en los sectores de ocio, hostelería y espectáculos.',
    cuerpo: `<p>La Asociación de Empresarios de Ocio y Espectáculos de la Comunidad de Madrid, <strong>Noche Madrid</strong>; la Asociación <strong>Transexualia</strong>, y <strong>Stipendium</strong> Te Ayuda, S. L., han firmado un <strong>convenio de colaboración para difundir programas de inserción laboral dirigidos a personas trans</strong> y promover oportunidades de empleo para <strong>colectivos con dificultades de acceso al mercado</strong> laboral en los sectores del ocio y los espectáculos.</p>

<blockquote class="destacado">
  <p><em>El acuerdo contempla acciones de difusión y sensibilización entre las empresas del ocio y los espectáculos, así como el seguimiento conjunto de las iniciativas.</em></p>
</blockquote>

<p>El acuerdo, suscrito el martes 20 de octubre por <strong>Antonio Extremera</strong>, vicepresidente de Noche Madrid; <strong>Cristina Jiménez</strong>, presidenta de Transexualia; y <strong>Carmen Rodríguez</strong>, en representación de Stipendium, tendrá una vigencia de un año. La firma se ha celebrado en la sede de Transexualia, en Madrid.</p>

<p>Entre las actuaciones previstas figuran la publicación de <strong>información</strong> y <strong>enlaces</strong> a los programas de ambas entidades en los <strong>canales de Noche Madrid</strong>, el envío de una circular a las empresas asociadas para dar a conocer sus servicios y la creación de un <strong>comité de seguimiento</strong> que evaluará el desarrollo de la colaboración. También se promoverán <strong>acciones de comunicación y sensibilización dirigidas al sector</strong>.</p>

<p>Fundada en 1987, <strong>Transexualia</strong> trabaja por los derechos y la inclusión de las personas trans y desarrolla programas de inserción sociolaboral. Entre sus iniciativas recientes figuran el proyecto «Atención integral para la inserción social y laboral de personas transexuales» y las dinámicas de empleabilidad que puso en marcha en 2025 junto a la Agencia para el Empleo de Madrid. Los estudios disponibles describen <strong>dificultades de acceso y permanencia en el empleo</strong>. Como antecedente de la actividad de la entidad, un estudio previo del Ministerio de Igualdad recoge que <strong>su programa de empleo logró la inserción laboral del 93,3 % de sus usuarias en 2019</strong>.</p>

<p><strong>Stipendium</strong> Te Ayuda presta asesoramiento legal, fiscal, contable y laboral a pequeñas empresas hosteleras, además de gestionar subvenciones. La colaboración busca <strong>dotar de recursos al tejido empresarial</strong> y facilitar que los establecimientos conozcan las iniciativas de Transexualia y las posibilidades de <strong>contratación inclusiva</strong>.</p>

<blockquote class="cita-portavoz">
  <p>«La inserción laboral necesita que las entidades sociales y las empresas trabajen conectadas. Con este acuerdo queremos acercar al sector del ocio y los espectáculos los programas de Transexualia y Stipendium, y ayudar a que más empresas conozcan cómo impulsar oportunidades laborales para las personas trans y otros colectivos con dificultades de acceso al empleo», señala <strong>Antonio Extremera</strong>, vicepresidente de Noche Madrid.</p>
</blockquote>`,
    puntos_clave: [
      'Alianza social: Convenio anual suscrito entre Noche Madrid, Transexualia y Stipendium para la inclusión sociolaboral.',
      'Efectividad probada: El programa de empleo de Transexualia acreditó un 93,3% de inserción laboral en estudios del Ministerio de Igualdad.',
      'Asesoramiento a salas: Stipendium prestará soporte laboral, legal y de ayudas públicas a empresas que incorporen contratación inclusiva.',
      'Plan de acción: Circular informativa a salas asociadas, canales oficiales y comité mixto de seguimiento y evaluación.'
    ],
    audio_script_es: 'Noche Madrid Press informa de la firma del convenio de colaboración entre Noche Madrid, Transexualia y la consultora Stipendium para impulsar la inserción laboral de las personas trans en las salas y locales de la capital. El vicepresidente de Noche Madrid Antonio Extremera, la presidenta de Transexualia Cristina Jiménez y Carmen Rodríguez de Stipendium rubricaron este acuerdo anual para conectar el talento y la formación de Transexualia con las necesidades de contratación del sector de ocio y espectáculos.',
    audio_habilitado: true
  }
];

async function main() {
  console.log('Iniciando inserción en Directus...');

  for (const art of articles) {
    console.log(`\n========================================`);
    console.log(`Procesando: "${art.titulo}"`);
    console.log(`Slug: ${art.slug}`);

    // Comprobar si ya existe
    const checkRes = await fetch(`${DIRECTUS_URL}/items/comunicados?filter[slug][_eq]=${encodeURIComponent(art.slug)}`, {
      headers: { Authorization: `Bearer ${DIRECTUS_TOKEN}` }
    });
    const checkData = await checkRes.json();
    let articleId = null;

    if (checkData.data && checkData.data.length > 0) {
      articleId = checkData.data[0].id;
      console.log(`El artículo ya existía con ID: ${articleId}. Actualizando datos en español...`);
      const updateRes = await fetch(`${DIRECTUS_URL}/items/comunicados/${articleId}`, {
        method: 'PATCH',
        headers: {
          Authorization: `Bearer ${DIRECTUS_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(art)
      });
      console.log(`Respuesta actualización Directus: ${updateRes.status}`);
    } else {
      console.log(`Insertando nuevo registro en Directus...`);
      const createRes = await fetch(`${DIRECTUS_URL}/items/comunicados`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${DIRECTUS_TOKEN}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(art)
      });
      if (!createRes.ok) {
        const errText = await createRes.text();
        console.error(`Error creando artículo en Directus:`, errText);
        continue;
      }
      const createData = await createRes.json();
      articleId = createData.data.id;
      console.log(`¡Artículo creado con éxito en Directus! ID: ${articleId}`);
    }

    // 1. Ejecutar auto-traducción a inglés
    console.log(`\n-> Disparando traducción a Inglés vía Cloudflare AI...`);
    try {
      const autoRes = await fetch(`${LOCAL_API}/auto-translate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: articleId })
      });
      const autoJson = await autoRes.json();
      console.log(`Resultado auto-traducción EN:`, autoRes.status, autoJson.success ? 'OK' : autoJson);
    } catch (err) {
      console.error(`Error en auto-translate EN:`, err.message);
    }

    // 2. Ejecutar traducción a Italiano y Francés
    console.log(`\n-> Disparando traducciones a Italiano y Francés (Directus translations)...`);
    try {
      const transRes = await fetch(`${LOCAL_API}/translate-article`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${DIRECTUS_TOKEN}`
        },
        body: JSON.stringify({
          articleId: articleId,
          targetLangs: ['it', 'fr']
        })
      });
      const transJson = await transRes.json();
      console.log(`Resultado traducciones IT & FR:`, transRes.status, JSON.stringify(transJson.results || transJson));
    } catch (err) {
      console.error(`Error en translate-article IT/FR:`, err.message);
    }

    // 3. Precalentar generación de audio TTS en Español y en Inglés
    console.log(`\n-> Precalentando audio briefs ElevenLabs TTS...`);
    try {
      const ttsEsRes = await fetch(`${LOCAL_API}/elevenlabs-tts?slug=${encodeURIComponent(art.slug)}&lang=es`);
      console.log(`Audio TTS Español status: ${ttsEsRes.status}`);
    } catch (err) {
      console.error(`Error en TTS ES:`, err.message);
    }

    // Obtener slug en inglés actualizado
    const itemEnRes = await fetch(`${DIRECTUS_URL}/items/comunicados/${articleId}?fields=slug_en`, {
      headers: { Authorization: `Bearer ${DIRECTUS_TOKEN}` }
    });
    const itemEnData = await itemEnRes.json();
    const slugEn = itemEnData.data?.slug_en;
    if (slugEn) {
      try {
        const ttsEnRes = await fetch(`${LOCAL_API}/elevenlabs-tts?slug=${encodeURIComponent(slugEn)}&lang=en`);
        console.log(`Audio TTS Inglés (${slugEn}) status: ${ttsEnRes.status}`);
      } catch (err) {
        console.error(`Error en TTS EN:`, err.message);
      }
    }
  }

  console.log(`\n\n========================================`);
  console.log(`¡Proceso completado con éxito para todas las notas de prensa!`);
}

main().catch(console.error);
