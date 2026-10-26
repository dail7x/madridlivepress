import requests
import json

url = 'https://mlpdirectus.116.203.118.1.sslip.io'
token = 'mlp_secret_directus_token_2026'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print("--- 1. Checking and Seeding IT and FR languages in Directus ---")
languages_to_seed = [
    {'code': 'it-IT', 'name': 'Italiano', 'direction': 'ltr'},
    {'code': 'fr-FR', 'name': 'Français', 'direction': 'ltr'}
]

# Fetch existing languages
r = requests.get(f'{url}/items/languages', headers=headers)
existing_codes = []
if r.status_code == 200:
    existing_codes = [l['code'] for l in r.json().get('data', [])]
    print(f"Existing languages: {existing_codes}")
else:
    print(f"Could not fetch languages: {r.status_code} - {r.text}")

for lang in languages_to_seed:
    if lang['code'] not in existing_codes:
        r_create = requests.post(f'{url}/items/languages', headers=headers, json=lang)
        print(f"Created language {lang['code']} ({lang['name']}): status {r_create.status_code}")
    else:
        print(f"Language {lang['code']} already exists.")

print("\n--- 2. Verifying public read permissions on comunicados_translations ---")
r_perms = requests.get(f'{url}/permissions?filter[collection][_eq]=comunicados_translations', headers=headers)
print("Permissions on comunicados_translations:", r_perms.status_code)

print("\n--- 3. Directus multilingual languages setup completed! ---")
