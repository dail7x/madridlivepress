import requests
import json

url = 'https://mlpdirectus.116.203.118.1.sslip.io'
token = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

def add_field(collection, field_name, field_type='string', interface='input'):
    payload = {
        "field": field_name,
        "type": field_type,
        "meta": {
            "interface": interface,
            "special": None
        },
        "schema": {
            "is_nullable": True
        }
    }
    if field_type == 'text':
        payload["meta"]["interface"] = "input-multiline"
    r = requests.post(f"{url}/fields/{collection}", headers=headers, json=payload)
    if r.status_code in [200, 204]:
        print(f"Created {collection}.{field_name}")
    else:
        print(f"{collection}.{field_name} response: {r.status_code} - {r.text[:100]}")

# 1. Add fields to comunicados
add_field('comunicados', 'titulo_en', 'string', 'input')
add_field('comunicados', 'slug_en', 'string', 'input')
add_field('comunicados', 'bajada_en', 'text', 'input-multiline')
add_field('comunicados', 'cuerpo_en', 'text', 'input-rich-text-html')

# 2. Add fields to salas
add_field('salas', 'tipo_espacio_en', 'string', 'input')
add_field('salas', 'descripcion_en', 'text', 'input-multiline')

# 3. Add fields to recursos_prensa
add_field('recursos_prensa', 'titulo_en', 'string', 'input')
add_field('recursos_prensa', 'descripcion_en', 'text', 'input-multiline')

# 4. Add fields to eventos
add_field('eventos', 'titulo_en', 'string', 'input')
add_field('eventos', 'slug_en', 'string', 'input')
add_field('eventos', 'descripcion_en', 'text', 'input-multiline')

# 5. Add fields to categorias
add_field('categorias', 'nombre_en', 'string', 'input')
add_field('categorias', 'slug_en', 'string', 'input')

print("All translation fields added to Directus schema.")
