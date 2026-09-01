import requests
import json

url = 'https://mlpdirectus.116.203.118.1.sslip.io'
token = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

def add_field(collection, field_name, field_type='string', interface='input', default_value=None):
    payload = {
        "field": field_name,
        "type": field_type,
        "meta": {
            "interface": interface,
            "special": None
        },
        "schema": {
            "is_nullable": True,
            "default_value": default_value
        }
    }
    if field_type == 'text':
        payload["meta"]["interface"] = "input-multiline"
    elif field_type == 'boolean':
        payload["meta"]["interface"] = "boolean"
    elif field_type == 'json':
        payload["meta"]["interface"] = "list"

    r = requests.post(f"{url}/fields/{collection}", headers=headers, json=payload)
    if r.status_code in [200, 204]:
        print(f"Created {collection}.{field_name}")
    else:
        print(f"{collection}.{field_name} response: {r.status_code} - {r.text[:100]}")

# 1. Add fields for Audio-Brief and Executive TL;DR
add_field('comunicados', 'audio_habilitado', 'boolean', 'boolean', True)
add_field('comunicados', 'audio_url', 'string', 'input')
add_field('comunicados', 'audio_duracion', 'string', 'input', '1:30 min')
add_field('comunicados', 'audio_script_es', 'text', 'input-multiline')
add_field('comunicados', 'audio_script_en', 'text', 'input-multiline')
add_field('comunicados', 'puntos_clave', 'json', 'list')
add_field('comunicados', 'puntos_clave_en', 'json', 'list')

print("All new fields created in Directus.")
