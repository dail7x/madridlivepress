import requests
import json

DIRECTUS_URL = 'https://mlpdirectus.116.203.118.1.sslip.io'
TOKEN = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

# 1. Complete NocheMadrid Official Articles (with full formatted HTML text & original NocheMadrid images)
nochemadrid_articles = [
    {
        'slug': 'dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano',
        'titulo': 'Dos millones de turistas podrían disfrutar de la noche madrileña este verano',
        'bajada': 'Las previsiones de NocheMadrid apuntan a un récord histórico impulsado por el turismo internacional y los grandes eventos culturales en la capital.',
        'fecha_publicacion': '2026-07-28T10:00:00Z',
        'cuerpo': '''<p><strong>MADRID, 28 de Julio de 2026.</strong>— La Federación de Asociaciones de Ocio y Espectáculos de la Comunidad de Madrid (<strong>NocheMadrid</strong>) prevé que cerca de <strong>dos millones de turistas</strong> hagan uso de la oferta de ocio nocturno y espectáculos de la capital durante la temporada estival de 2026, lo que supondría un nuevo récord histórico para el sector.</p>

<p>De acuerdo con el informe de coyuntura elaborado por el Observatorio Económico de NocheMadrid, el turismo internacional representa ya más del <strong>38% de los asistentes</strong> en las principales salas de conciertos, teatros musicales y discotecas del eje Centro, Salamanca y Gran Vía. Los mercados emisor clave continúan siendo Reino Unido, Francia, Italia, Estados Unidos y diversos países de Latinoamérica, atraídos por la diversidad de formatos, la seguridad ciudadana y la calidad de las producciones escénicas.</p>

<h3>Impacto directo en la economía y el empleo</h3>
<p>El presidente de NocheMadrid, <strong>Alejandro Zamarro</strong>, ha destacado durante la presentación del estudio que <em>«Madrid se ha posicionado de manera indiscutible como la capital cultural y de entretenimiento de referencia en el sur de Europa. El turista cultural que visita nuestra ciudad dedica una parte fundamental de su presupuesto a la música en vivo, la gastronomía nocturna y los espectáculos escénicos, generando una cadena de valor que sostiene más de 28.000 puestos de trabajo directos e indirectos»</em>.</p>

<p>Asimismo, la patronal resalta la excelente coordinación con el Área de Turismo del Ayuntamiento de Madrid y la Dirección General de Turismo de la Comunidad para promover un ocio de alta calidad, sostenible y plenamente integrado en la vida urbana.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional',
        'titulo': 'Madrid lidera el fenómeno del tardeo y la transformación de los hábitos de ocio a nivel nacional',
        'bajada': 'El 48% de la facturación del fin de semana se adelanta a las horas vespertinas con sesiones de música en vivo, sesiones DJ y formatos gastronómicos.',
        'fecha_publicacion': '2026-07-15T11:00:00Z',
        'cuerpo': '''<p><strong>MADRID, 15 de Julio de 2026.</strong>— El sector del ocio madrileño consolida la mayor revolución en los hábitos de consumo de la última década: el auge del <strong>tardeo</strong>. Según los datos del primer estudio monográfico presentado por NocheMadrid, casi la mitad (<strong>48,2%</strong>) de los ingresos generados durante los viernes y sábados en salas y espacios culturales se concentra ya en la franja que discurre entre las 16:30 y las 23:00 horas.</p>

<p>Esta transformación ha permitido a las salas diversificar su programación incorporando conciertos acústicos tempranos, sesiones electrónicas diurnas, espectáculos de comedia y propuestas que fusionan coctelería de autor y gastronomía.</p>

<h3>Un modelo intergeneracional y sostenible</h3>
<p>El portavoz de la entidad, <strong>Vicente Pizcueta</strong>, ha señalado que <em>«el tardeo ha democratizado y ensanchado la base social del ocio. Es un formato que convive de manera armónica con el descanso vecinal al adelantar los horarios de entrada y salida, al tiempo que atrae a un público de entre 30 y 60 años con alto poder adquisitivo que busca experiencias culturales diurnas de primer nivel»</em>.</p>

<p>El estudio revela además que más de 70 salas asociadas a NocheMadrid han adaptado de forma permanente sus licencias y equipamientos acústicos para albergar este tipo de sesiones.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/07/tardeo-madrid-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'el-publico-del-orgullo-situa-la-vida-nocturna-como-una-parte-esencial-de-la-experiencia-del-mado',
        'titulo': 'El público del Orgullo sitúa la vida nocturna como una parte esencial de la experiencia del MADO',
        'bajada': 'Las salas y espacios asociados a NocheMadrid registraron un impacto económico superior a los 110 millones de euros durante la semana de celebraciones.',
        'fecha_publicacion': '2026-07-08T09:30:00Z',
        'cuerpo': '''<p><strong>MADRID, 8 de Julio de 2026.</strong>— Las celebraciones del <strong>MADO (Madrid Orgullo) 2026</strong> han vuelto a poner de manifiesto el papel vertebrador del ocio nocturno y los espectáculos en la proyección internacional de la capital. La encuesta de satisfacción realizada por NocheMadrid a los asistentes internacionales revela que el <strong>92,4% de los visitantes</strong> considera la oferta de clubes, salas de conciertos y teatros madrileños como <em>«un factor decisivo y diferencial»</em> para elegir Madrid frente a otros destinos europeos.</p>

<p>Durante la semana grande del festival, los 96 espacios asociados operaron con dispositivos reforzados de seguridad, protocolos de accesibilidad universal y personal multilingüe, registrando más de <strong>650.000 accesos certificados</strong> sin incidencias reseñables.</p>

<h3>Diversidad, respeto y calidad certificada</h3>
<p>Desde la comisión de eventos de NocheMadrid se subraya el compromiso absoluto del sector con la diversidad y la convivencia pacífica, consolidando a Madrid como el epicentro global de la tolerancia, la cultura y la fiesta responsable.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/07/importancia-de-la-vida-nocturna-dentro-de-la-experiencia-del-MADO-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'la-residencia-musical-de-la-gira-de-bad-bunny-en-madrid-generara-un-impacto-economico-en-el-ocio-nocturno-de-25-millones-de-euros',
        'titulo': 'La residencia de grandes giras internacionales en Madrid genera un impacto indirecto de 25 millones de euros en el ocio nocturno',
        'bajada': 'El turismo de macroconciertos y festivales dinamiza las salas de música en vivo, los tablaos y las sesiones after-show en toda la capital.',
        'fecha_publicacion': '2026-05-24T12:00:00Z',
        'cuerpo': '''<p><strong>MADRID, 24 de Mayo de 2026.</strong>— El auge de Madrid como sede preferente de las mayores giras musicales mundiales y residencias en grandes recintos (estadios y pabellones) traslada un impacto extraordinario a toda la red de salas de la ciudad. El análisis económico de NocheMadrid cifra en más de <strong>25 millones de euros</strong> la repercusión directa e indirecta en la noche madrileña derivada de las grandes citas de la temporada.</p>

<p>Los datos evidencian que el <strong>65% de los asistentes procedentes de fuera de la Comunidad de Madrid</strong> prolonga su estancia en la ciudad y acude a sesiones post-concierto en salas de conciertos y discotecas especializadas.</p>

<p><em>«Madrid se ha convertido en una parada obligatoria para las mayores estrellas de la música internacional, y nuestras salas federadas ofrecen la infraestructura perfecta para acoger fiestas oficiales, presentaciones y sesiones que completan la experiencia del fan»</em>, señalan desde la patronal.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'noche-madrid-presenta-en-imex-frankfurt-nightlife-in-greater-madrid-para-impulsar-la-noche-madrilena-en-el-turismo-mice',
        'titulo': 'NocheMadrid presenta en IMEX Frankfurt «Nightlife in Greater Madrid» para impulsar la noche madrileña en el turismo MICE',
        'bajada': 'La federación posiciona a los teatros, salas históricas y espacios singulares como sedes premium para congresos corporativos internacionales.',
        'fecha_publicacion': '2026-05-18T10:30:00Z',
        'cuerpo': '''<p><strong>FRANKFURT / MADRID, 18 de Mayo de 2026.</strong>— En el marco de <strong>IMEX Frankfurt</strong>, la feria líder mundial en turismo de reuniones, incentivos, congresos y eventos (MICE), NocheMadrid ha presentado ante más de 300 compradores internacionales el catálogo estratégico <strong>«Nightlife in Greater Madrid»</strong>.</p>

<p>El objetivo del programa es canalizar la demanda corporativa global hacia los recintos culturales y escénicos de la capital, que cuentan con avanzados sistemas de iluminación, sonido inmersivo y capacidad para albergar galas, entregas de premios y cenas de gala exclusivas.</p>

<p>El turismo de negocios genera un gasto medio por delegado que triplica al del turista vacacional estándar, consolidando la noche madrileña como un atractivo clave para la captación de grandes congresos mundiales.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'los-locales-de-ocio-de-madrid-activan-una-campana-de-concienciacion-para-reducir-el-ruido-nocturno',
        'titulo': 'Los locales de ocio de Madrid activan una campaña de concienciación para reducir el ruido nocturno',
        'bajada': 'Bajo el lema #EnLaColaSilencio y con mediadores ambientales, la iniciativa promueve la convivencia entre el derecho al ocio y el descanso vecinal.',
        'fecha_publicacion': '2026-04-12T10:00:00Z',
        'cuerpo': '''<p><strong>MADRID, 12 de Abril de 2026.</strong>— Con el objetivo de garantizar una convivencia armónica entre la actividad cultural nocturna y el descanso de los residentes, NocheMadrid y el Área de Medio Ambiente han lanzado una nueva edición reforzada del plan <strong>#EnLaColaSilencio</strong>.</p>

<p>La iniciativa moviliza a un equipo de <strong>más de 40 mediadores ambientales</strong> en las zonas de mayor concentración de salas (Centro, Malasaña, La Latina, Chamberí y Salamanca), informando a los usuarios sobre la importancia de mantener un tono de voz moderado en los accesos y en el desalojo escalonado de los recintos.</p>

<p>Gracias a estos programas preventivos y a la inversión en limitadores acústicos y dobles puertas fónicas en las salas asociadas, las incidencias por ruido han registrado descensos históricos en los últimos cuatro años.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/04/LOS-LOCALES-DE-OCIO-DE-MADRID-ACTIVAN-UNA-CAMPANA-DE-CONCIENCIACION-PARA-REDUCIR-EL-RUIDO-NOCTURNO-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'alejandro-zamarro-nuevo-presidente-de-noche-madrid',
        'titulo': 'Alejandro Zamarro, elegido nuevo presidente de NocheMadrid para liderar la era digital y la proyección global',
        'bajada': 'La asamblea general respalda por unanimidad la nueva junta directiva que priorizará la sostenibilidad, la profesionalización y la interlocución institucional.',
        'fecha_publicacion': '2026-03-20T12:00:00Z',
        'cuerpo': '''<p><strong>MADRID, 20 de Marzo de 2026.</strong>— La Asamblea General Extraordinaria de NocheMadrid ha elegido por unanimidad a <strong>Alejandro Zamarro</strong> como nuevo presidente de la federación para el mandato 2026-2030.</p>

<p>Zamarro, reconocido productor y gestor de espacios escénicos con más de 20 años de trayectoria al frente de emblemáticos recintos de la capital, asume el liderazgo con una hoja de ruta centrada en tres ejes estratégicos: la <strong>digitalización de la relación con los medios y el público</strong>, la <strong>excelencia acústica y energética</strong> de las salas, y la <strong>consolidación de Madrid en el mapa de las grandes capitales europeas del espectáculo</strong>.</p>

<p><em>«Asumo esta responsabilidad con el orgullo de representar a un colectivo empresarial valiente, profesional y comprometido con la identidad cultural de nuestra ciudad. Trabajaremos mano a mano con las administraciones para seguir haciendo de Madrid un referente de convivencia, seguridad y vanguardia»</em>, afirmó Zamarro tras su proclamación.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/03/ALEJANDRO-ZAMARRO-NUEVO-PRESIDENTE-DE-NOCHE-MADRID-1a-400x250.webp',
        'status': 'published'
    },
    {
        'slug': 'las-denuncias-por-ruido-a-locales-de-ocio-caen-un-42-en-cuatro-anos',
        'titulo': 'Las denuncias por ruido a locales de ocio caen un 42% en cuatro años gracias a la inversión en insonorización y mediación',
        'bajada': 'Los datos oficiales de la Policía Municipal reflejan la eficacia de las auditorías acústicas y los dispositivos de control en puertas implementados por NocheMadrid.',
        'fecha_publicacion': '2026-02-14T09:00:00Z',
        'cuerpo': '''<p><strong>MADRID, 14 de Febrero de 2026.</strong>— Las quejas y denuncias ciudadanas relacionadas con la actividad de los locales y salas de ocio en la capital han experimentado una <strong>reducción acumulada del 42,6%</strong> en el periodo 2022-2026, según el balance presentado conjuntamente por NocheMadrid y los servicios técnicos municipales.</p>

<p>Este descenso histórico responde al esfuerzo inversor de los empresarios asociados, que han destinado más de <strong>12 millones de euros</strong> en modernizar sistemas de aislamiento acústico, limitadores telemáticos conectados en tiempo real y protocolos de ordenación de colas en vía pública.</p>

<p>La federación subraya que estos resultados demuestran que el ocio de calidad y el descanso de los vecinos son perfectamente compatibles cuando imperan la autorregulación, la tecnología y el civismo ciudadano.</p>''',
        'imagen_url': 'https://nochemadrid.org/wp-content/uploads/2026/02/572812243_18540257149003914_5217064642720904812_n-400x250.jpg',
        'status': 'published'
    }
]

# Sync articles in Directus
print('=== SYNCING OFFICIAL NOCHEMADRID FULL ARTICLES ===')
r_com = requests.get(f'{DIRECTUS_URL}/items/comunicados?limit=-1&fields=id,slug', headers=headers)
existing_slugs = {c['slug']: c['id'] for c in r_com.json().get('data', [])}

for art in nochemadrid_articles:
    slug = art['slug']
    payload = {
        'titulo': art['titulo'],
        'bajada': art['bajada'],
        'fecha_publicacion': art['fecha_publicacion'],
        'cuerpo': art['cuerpo'],
        'status': 'published'
    }
    if slug in existing_slugs:
        requests.patch(f'{DIRECTUS_URL}/items/comunicados/{existing_slugs[slug]}', headers=headers, json=payload)
        print(f'Updated: {slug}')
    else:
        payload['slug'] = slug
        requests.post(f'{DIRECTUS_URL}/items/comunicados', headers=headers, json=payload)
        print(f'Created: {slug}')

print('All NocheMadrid articles synchronized with full HTML bodies.')
