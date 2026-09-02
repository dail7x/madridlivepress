import requests
import json
import re

url = 'https://mlpdirectus.116.203.118.1.sslip.io'
token = 'mlp_secret_directus_token_2026'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

def clean_html_for_speech(html_text):
    if not html_text:
        return ""
    # Convert closing paragraphs and blocks to period pauses
    text = re.sub(r'</?(?:p|div|h[1-6]|li|blockquote)[^>]*>', '. ', html_text)
    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Normalize periods
    text = re.sub(r'\.+', '.', text)
    return text

r = requests.get(f'{url}/items/comunicados?limit=-1', headers=headers)
items = r.json().get('data', [])
print(f'Populating {len(items)} articles into Directus Content Translations...')

for item in items:
    art_id = item['id']
    title_es = item.get('titulo') or ''
    slug_es = item.get('slug') or ''
    bajada_es = item.get('bajada') or ''
    cuerpo_es = item.get('cuerpo') or ''
    puntos_es = item.get('puntos_clave') or []
    
    # Complete article speech text for ElevenLabs (Title + Subtitle + Complete Body)
    speech_body_es = clean_html_for_speech(cuerpo_es)
    full_audio_es = f"{title_es}. {bajada_es}. {speech_body_es}".strip()
    
    title_en = item.get('titulo_en') or title_es
    slug_en = item.get('slug_en') or slug_es
    bajada_en = item.get('bajada_en') or bajada_es
    cuerpo_en = item.get('cuerpo_en') or cuerpo_es
    puntos_en = item.get('puntos_clave_en') or puntos_es
    
    speech_body_en = clean_html_for_speech(cuerpo_en)
    full_audio_en = f"{title_en}. {bajada_en}. {speech_body_en}".strip()

    # Limit to 4500 chars to respect ElevenLabs per-request limits safely
    full_audio_es = full_audio_es[:4500]
    full_audio_en = full_audio_en[:4500]

    # 1. Insert Spanish Translation Record
    trans_es = {
        'comunicados_id': art_id,
        'languages_code': 'es-ES',
        'titulo': title_es,
        'slug': slug_es,
        'bajada': bajada_es,
        'cuerpo': cuerpo_es,
        'audio_script': full_audio_es,
        'puntos_clave': puntos_es
    }
    r_es = requests.post(f'{url}/items/comunicados_translations', headers=headers, json=trans_es)

    # 2. Insert English Translation Record
    trans_en = {
        'comunicados_id': art_id,
        'languages_code': 'en-US',
        'titulo': title_en,
        'slug': slug_en,
        'bajada': bajada_en,
        'cuerpo': cuerpo_en,
        'audio_script': full_audio_en,
        'puntos_clave': puntos_en
    }
    r_en = requests.post(f'{url}/items/comunicados_translations', headers=headers, json=trans_en)

    # 3. Update main record with complete audio script for ElevenLabs
    requests.patch(f'{url}/items/comunicados/{art_id}', headers=headers, json={
        'audio_script_es': full_audio_es,
        'audio_script_en': full_audio_en
    })

    print(f"[{art_id}] '{slug_es}': ES={r_es.status_code}, EN={r_en.status_code}")

print('Done populating all articles into Directus Content Translations!')
