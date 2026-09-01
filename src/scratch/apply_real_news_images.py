import requests
import json

DIRECTUS_URL = 'https://mlpdirectus.116.203.118.1.sslip.io'
TOKEN = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

# 1. Ensure field imagen_url_externa in comunicados
try:
    requests.post(f'{DIRECTUS_URL}/fields/comunicados', headers=headers, json={
        'field': 'imagen_url_externa',
        'type': 'string',
        'meta': {
            'interface': 'input',
            'special': None,
            'options': {'placeholder': 'https://nochemadrid.org/wp-content/uploads/...'},
            'width': 'full'
        }
    })
    print('imagen_url_externa field created/ensured.')
except Exception as e:
    print('Field note:', e)

# 2. Grant permissions
try:
    r_perm = requests.get(f'{DIRECTUS_URL}/permissions?filter[collection][_eq]=comunicados', headers=headers)
    for p in r_perm.json().get('data', []):
        requests.patch(f'{DIRECTUS_URL}/permissions/{p["id"]}', headers=headers, json={'fields': ['*']})
    print('Permissions updated.')
except Exception as e:
    print('Perm note:', e)

# 3. Map exact real images
image_map = {
    'dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano': 'https://nochemadrid.org/wp-content/uploads/2026/07/dos-millones-de-turistas-podrian-disfrutar-de-la-noche-madrilena-este-verano-1a-400x250.webp',
    'madrid-lidera-el-fenomeno-del-tardeo-y-la-transformacion-de-los-habitos-de-ocio-a-nivel-nacional': 'https://nochemadrid.org/wp-content/uploads/2026/07/tardeo-madrid-1a-400x250.webp',
    'el-publico-del-orgullo-situa-la-vida-nocturna-como-una-parte-esencial-de-la-experiencia-del-mado': 'https://nochemadrid.org/wp-content/uploads/2026/07/importancia-de-la-vida-nocturna-dentro-de-la-experiencia-del-MADO-1a-400x250.webp',
    'la-residencia-musical-de-la-gira-de-bad-bunny-en-madrid-generara-un-impacto-economico-en-el-ocio-nocturno-de-25-millones-de-euros': 'https://nochemadrid.org/wp-content/uploads/2026/05/BAD-BUNNY-EN-MADRID-1a-400x250.webp',
    'noche-madrid-presenta-en-imex-frankfurt-nightlife-in-greater-madrid-para-impulsar-la-noche-madrilena-en-el-turismo-mice': 'https://nochemadrid.org/wp-content/uploads/2026/05/NOCHE-MADRID-PRESENTA-EN-IMEX-FRANKFURT-NIGHTLIFE-IN-GREATER-MADRID-1a-400x250.webp',
    'los-locales-de-ocio-de-madrid-activan-una-campana-de-concienciacion-para-reducir-el-ruido-nocturno': 'https://nochemadrid.org/wp-content/uploads/2026/04/LOS-LOCALES-DE-OCIO-DE-MADRID-ACTIVAN-UNA-CAMPANA-DE-CONCIENCIACION-PARA-REDUCIR-EL-RUIDO-NOCTURNO-1a-400x250.webp',
    'alejandro-zamarro-nuevo-presidente-de-noche-madrid': 'https://nochemadrid.org/wp-content/uploads/2026/03/ALEJANDRO-ZAMARRO-NUEVO-PRESIDENTE-DE-NOCHE-MADRID-1a-400x250.webp',
    'el-ocio-nocturno-madrileno-consolida-su-transicion-sostenible': 'https://nochemadrid.org/wp-content/uploads/2026/03/EL-OCIO-NOCTURNO-MADRILENO-CONSOLIDA-SU-TRANSICION-SOSTENIBLE-1a.jpeg',
    'las-denuncias-por-ruido-a-locales-de-ocio-caen-un-42-en-cuatro-anos': 'https://nochemadrid.org/wp-content/uploads/2026/02/572812243_18540257149003914_5217064642720904812_n.jpg',
    'convocado-el-examen-de-controladores-de-acceso-2026': 'https://nochemadrid.org/wp-content/uploads/2026/05/CONVOCATORIA-DEL-EXAMEN-PARA-CONTROLADORES-DE-ACCESO-1a-400x250.webp',
    'noche-madrid-ha-sido-reconocidas-en-los-premios-recicla-la-noche-por-la-puesta-en-marcha-de-la-campana-enlacolasilencio': 'https://nochemadrid.org/wp-content/uploads/2026/05/Noche-Madrid-ha-sido-reconocidas-en-los-Premios-Recicla-la-Noche-1a.jpeg',
    'noche-madrid-presenta-el-primer-estudio-sobre-el-tardeo-en-madrid': 'https://nochemadrid.org/wp-content/uploads/2026/07/tardeo-madrid-1a-400x250.webp'
}

r_com = requests.get(f'{DIRECTUS_URL}/items/comunicados?limit=-1&fields=id,slug', headers=headers)
for c in r_com.json().get('data', []):
    slug = c['slug']
    if slug in image_map:
        requests.patch(f'{DIRECTUS_URL}/items/comunicados/{c["id"]}', headers=headers, json={
            'imagen_url_externa': image_map[slug]
        })
        print(f'Set real image for {slug}')

print('Done updating real NocheMadrid images!')
