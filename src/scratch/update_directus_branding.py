import urllib.request
import json

DIRECTUS_URL = "https://mlpdirectus.116.203.118.1.sslip.io"
TOKEN = "mlp_secret_directus_token_2026"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def update_collection(collection_name):
    # Fetch all items that might contain 'Madrid Live Press'
    url = f"{DIRECTUS_URL}/items/{collection_name}?search=Madrid%20Live%20Press&limit=100"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())['data']

    print(f"Found {len(data)} items in {collection_name} matching 'Madrid Live Press'")

    for item in data:
        item_id = item['id']
        payload = {}
        for field in ['cuerpo', 'bajada', 'titulo', 'audio_script', 'audio_script_es', 'audio_script_en']:
            if field in item and item[field] and "Madrid Live Press" in str(item[field]):
                payload[field] = item[field].replace("Madrid Live Press", "Noche Madrid Press")
        
        if payload:
            print(f"Updating {collection_name} ID {item_id}: {list(payload.keys())}")
            patch_url = f"{DIRECTUS_URL}/items/{collection_name}/{item_id}"
            req_patch = urllib.request.Request(
                patch_url,
                data=json.dumps(payload).encode(),
                headers=HEADERS,
                method='PATCH'
            )
            with urllib.request.urlopen(req_patch) as patch_resp:
                res = json.loads(patch_resp.read().decode())
                print(f"Successfully updated ID {item_id}")

if __name__ == '__main__':
    update_collection('comunicados')
    update_collection('comunicados_translations')
