import requests

url = 'https://mlpdirectus.116.203.118.1.sslip.io'
token = 'mlp_secret_directus_token_2026'
headers = {'Authorization': f'Bearer {token}'}

print("--- Testing Directus Query with translations collection ---")
r = requests.get(f'{url}/items/comunicados?limit=1&fields=id,slug,titulo,translations.*', headers=headers)
if r.status_code == 200:
    data = r.json().get('data', [])
    if data:
        item = data[0]
        print(f"Article ID: {item.get('id')}")
        print(f"Slug: {item.get('slug')}")
        print(f"Title: {item.get('titulo')}")
        translations = item.get('translations', [])
        print(f"Available translation records in comunicados_translations: {len(translations)}")
        for t in translations:
            print(f"  - Lang: {t.get('languages_code')} | Slug: {t.get('slug')} | Title: {t.get('titulo')[:40]}...")
    else:
        print("No articles found.")
else:
    print(f"Error: {r.status_code} - {r.text}")
