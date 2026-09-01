import requests

DIRECTUS_URL = 'https://mlpdirectus.116.203.118.1.sslip.io'
TOKEN = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

local_images_map = {
    'dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano': '/images/news/dos-millones-turistas.jpg',
    'madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional': '/images/news/tardeo-madrid.jpg',
    'el-publico-del-orgullo-situa-la-vida-nocturna-como-una-parte-esencial-de-la-experiencia-del-mado': '/images/news/mado-orgullo.jpg',
    'la-residencia-musical-de-la-gira-de-bad-bunny-en-madrid-generara-un-impacto-economico-en-el-ocio-nocturno-de-25-millones-de-euros': '/images/news/bad-bunny-residencia.jpg',
    'noche-madrid-presenta-en-imex-frankfurt-nightlife-in-greater-madrid-para-impulsar-la-noche-madrilena-en-el-turismo-mice': '/images/news/imex-frankfurt.jpg',
    'los-locales-de-ocio-de-madrid-activan-una-campana-de-concienciacion-para-reducir-el-ruido-nocturno': '/images/news/enlacolasilencio.jpg',
    'alejandro-zamarro-nuevo-presidente-de-noche-madrid': '/images/news/alejandro-zamarro.jpg',
    'las-denuncias-por-ruido-a-locales-de-ocio-caen-un-42-en-cuatro-anos': '/images/news/denuncias-ruido.jpg',
    'impacto-record-ocio-nocturno-madrid-4800-millones': '/images/news/impacto-economico.jpg',
    'guia-innovacion-acustica-sostenibilidad-distrito-centro': '/images/news/enlacolasilencio.jpg',
    'salas-musica-en-vivo-programan-1200-conciertos-otono': '/images/news/conciertos-otono.jpg',
    'las-salas-de-madrid-refuerzan-su-proyeccion-cultural-internacional': '/images/news/imex-frankfurt.jpg',
    'dos-millones-turistas-disfrutaran-noche-madrilena-verano': '/images/news/dos-millones-turistas.jpg',
    'madrid-lidera-fenomeno-tardeo-transformacion-habitos-ocio': '/images/news/tardeo-madrid.jpg',
    'residencia-bad-bunny-madrid-impacto-25-millones-ocio': '/images/news/bad-bunny-residencia.jpg',
    'noche-madrid-presenta-imex-frankfurt-nightlife-in-greater-madrid': '/images/news/imex-frankfurt.jpg',
    'campana-concienciacion-reduccion-ruido-nocturno-madrid': '/images/news/enlacolasilencio.jpg',
    'alejandro-zamarro-nuevo-presidente-noche-madrid': '/images/news/alejandro-zamarro.jpg',
    'el-sector-cultural-presenta-sus-nuevos-datos-de-actividad': '/images/news/impacto-economico.jpg',
    'una-nueva-temporada-conecta-salas-y-ciudad': '/images/news/tardeo-madrid.jpg',
    'madrid-amplia-su-presencia-en-medios-internacionales': '/images/news/imex-frankfurt.jpg',
    'el-ciclo-de-otono-reune-voces-nacionales-e-internacionales': '/images/news/conciertos-otono.jpg',
    'nuevas-residencias-artisticas-en-centros-municipales': '/images/news/residencias-artisticas.jpg',
    'radiografia-del-publico-cultural-en-madrid-2025-2026': '/images/news/mado-orgullo.jpg',
    'programacion-familiar-para-el-inicio-de-temporada': '/images/news/enlacolasilencio.jpg',
    'madrid-y-sus-salas-en-la-agenda-cultural-europea': '/images/news/imex-frankfurt.jpg',
    'nuevos-apoyos-a-la-creacion-sonora-emergente': '/images/news/conciertos-otono.jpg'
}

r = requests.get(f'{DIRECTUS_URL}/items/comunicados?limit=-1', headers=headers)
for item in r.json().get('data', []):
    slug = item['slug']
    img_path = local_images_map.get(slug, '/images/news/dos-millones-turistas.jpg')
    requests.patch(f'{DIRECTUS_URL}/items/comunicados/{item["id"]}', headers=headers, json={
        'imagen_url_externa': img_path
    })
    print(f'Set local image for {slug} -> {img_path}')

print('All Directus comunicados mapped to high-speed local static image assets.')
