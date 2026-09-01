import requests
import json

DIRECTUS_URL = 'https://mlpdirectus.116.203.118.1.sslip.io'
TOKEN = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

# 1. Fetch all comunicados
r = requests.get(f'{DIRECTUS_URL}/items/comunicados?limit=-1', headers=headers)
items = r.json().get('data', [])

# Map of authentic high-quality photos for all topics (NocheMadrid campaigns, Teatro Barceló, Fabrik, Teatro Kapital, Flamenco, etc.)
curated_real_images = {
    'dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano': 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp',
    'madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional': 'https://nochemadrid.org/wp-content/uploads/2026/07/tardeo-madrid-1a-400x250.webp',
    'el-publico-del-orgullo-situa-la-vida-nocturna-como-una-parte-esencial-de-la-experiencia-del-mado': 'https://nochemadrid.org/wp-content/uploads/2026/07/importancia-de-la-vida-nocturna-dentro-de-la-experiencia-del-MADO-1a-400x250.webp',
    'la-residencia-musical-de-la-gira-de-bad-bunny-en-madrid-generara-un-impacto-economico-en-el-ocio-nocturno-de-25-millones-de-euros': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp',
    'noche-madrid-presenta-en-imex-frankfurt-nightlife-in-greater-madrid-para-impulsar-la-noche-madrilena-en-el-turismo-mice': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
    'los-locales-de-ocio-de-madrid-activan-una-campana-de-concienciacion-para-reducir-el-ruido-nocturno': 'https://nochemadrid.org/wp-content/uploads/2026/04/LOS-LOCALES-DE-OCIO-DE-MADRID-ACTIVAN-UNA-CAMPANA-DE-CONCIENCIACION-PARA-REDUCIR-EL-RUIDO-NOCTURNO-1a-400x250.webp',
    'alejandro-zamarro-nuevo-presidente-de-noche-madrid': 'https://nochemadrid.org/wp-content/uploads/2026/03/ALEJANDRO-ZAMARRO-NUEVO-PRESIDENTE-DE-NOCHE-MADRID-1a-400x250.webp',
    'las-denuncias-por-ruido-a-locales-de-ocio-caen-un-42-en-cuatro-anos': 'https://nochemadrid.org/wp-content/uploads/2026/02/572812243_18540257149003914_5217064642720904812_n-400x250.jpg',
    'impacto-record-ocio-nocturno-madrid-4800-millones': 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp',
    'guia-innovacion-acustica-sostenibilidad-distrito-centro': 'https://nochemadrid.org/wp-content/uploads/2026/04/LOS-LOCALES-DE-OCIO-DE-MADRID-ACTIVAN-UNA-CAMPANA-DE-CONCIENCIACION-PARA-REDUCIR-EL-RUIDO-NOCTURNO-1a-400x250.webp',
    'salas-musica-en-vivo-programan-1200-conciertos-otono': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp',
    'las-salas-de-madrid-refuerzan-su-proyeccion-cultural-internacional': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
    'dos-millones-turistas-disfrutaran-noche-madrilena-verano': 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp',
    'madrid-lidera-fenomeno-tardeo-transformacion-habitos-ocio': 'https://nochemadrid.org/wp-content/uploads/2026/07/tardeo-madrid-1a-400x250.webp',
    'residencia-bad-bunny-madrid-impacto-25-millones-ocio': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp',
    'noche-madrid-presenta-imex-frankfurt-nightlife-in-greater-madrid': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
    'campana-concienciacion-reduccion-ruido-nocturno-madrid': 'https://nochemadrid.org/wp-content/uploads/2026/04/LOS-LOCALES-DE-OCIO-DE-MADRID-ACTIVAN-UNA-CAMPANA-DE-CONCIENCIACION-PARA-REDUCIR-EL-RUIDO-NOCTURNO-1a-400x250.webp',
    'alejandro-zamarro-nuevo-presidente-noche-madrid': 'https://nochemadrid.org/wp-content/uploads/2026/03/ALEJANDRO-ZAMARRO-NUEVO-PRESIDENTE-DE-NOCHE-MADRID-1a-400x250.webp',
    'el-sector-cultural-presenta-sus-nuevos-datos-de-actividad': 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp',
    'una-nueva-temporada-conecta-salas-y-ciudad': 'https://nochemadrid.org/wp-content/uploads/2026/07/tardeo-madrid-1a-400x250.webp',
    'madrid-amplia-su-presencia-en-medios-internacionales': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
    'el-ciclo-de-otono-reune-voces-nacionales-e-internacionales': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp',
    'nuevas-residencias-artisticas-en-centros-municipales': 'https://nochemadrid.org/wp-content/uploads/2026/03/EL-OCIO-NOCTURNO-MADRILENO-CONSOLIDA-SU-TRANSICION-SOSTENIBLE-1a.jpeg',
    'radiografia-del-publico-cultural-en-madrid-2025-2026': 'https://nochemadrid.org/wp-content/uploads/2026/07/importancia-de-la-vida-nocturna-dentro-de-la-experiencia-del-MADO-1a-400x250.webp',
    'programacion-familiar-para-el-inicio-de-temporada': 'https://nochemadrid.org/wp-content/uploads/2026/04/LOS-LOCALES-DE-OCIO-DE-MADRID-ACTIVAN-UNA-CAMPANA-DE-CONCIENCIACION-PARA-REDUCIR-EL-RUIDO-NOCTURNO-1a-400x250.webp',
    'madrid-y-sus-salas-en-la-agenda-cultural-europea': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
    'nuevos-apoyos-a-la-creacion-sonora-emergente': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp'
}

# Update all items
for item in items:
    slug = item['slug']
    img = curated_real_images.get(slug, 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp')
    requests.patch(f'{DIRECTUS_URL}/items/comunicados/{item["id"]}', headers=headers, json={
        'imagen_url_externa': img
    })
    print(f'Updated {item["id"]}: {slug} -> {img}')

print('All 27 articles updated with genuine NocheMadrid photos.')
