import os
import requests
import json
from typing import Optional

DIRECTUS_URL = os.environ.get('DIRECTUS_URL', 'https://mlpdirectus.116.203.118.1.sslip.io')
DIRECTUS_TOKEN = os.environ.get('DIRECTUS_STATIC_TOKEN', 'mlp_secret_directus_token_2026')

class DirectusPressClient:
    def __init__(self, base_url: str = DIRECTUS_URL, token: str = DIRECTUS_TOKEN):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        self.collection = "contactos_prensa"

    def get_existing_emails(self) -> set[str]:
        """Obtiene la lista de emails ya registrados para evitar duplicados."""
        emails = set()
        page = 1
        limit = 100
        while True:
            params = {
                "fields": "email",
                "limit": limit,
                "page": page
            }
            try:
                res = requests.get(f"{self.base_url}/items/{self.collection}", headers=self.headers, params=params, timeout=10)
                if res.status_code == 200:
                    data = res.json().get("data", [])
                    if not data:
                        break
                    for item in data:
                        if item.get("email"):
                            emails.add(item["email"].lower().strip())
                    page += 1
                else:
                    break
            except Exception as e:
                print(f"Error consultando Directus emails existentes: {e}")
                break
        return emails

    def save_contact(self, contact: dict) -> bool:
        """Inserta un nuevo contacto en Directus."""
        try:
            res = requests.post(
                f"{self.base_url}/items/{self.collection}",
                headers=self.headers,
                json=contact,
                timeout=10
            )
            if res.status_code in [200, 204]:
                return True
            else:
                # print(f"Error guardando contacto {contact.get('email')}: {res.status_code} - {res.text[:100]}")
                return False
        except Exception as e:
            print(f"Excepción guardando contacto en Directus: {e}")
            return False

    def list_contacts(self, categoria: Optional[str] = None, mercado: Optional[str] = None, tipo_medio: Optional[str] = None, estado: Optional[str] = None) -> list[dict]:
        """Recupera los contactos almacenados, opcionalmente filtrados."""
        params = {"limit": -1}
        filter_dict = {}
        if categoria:
            filter_dict["categoria_principal"] = {"_eq": categoria}
        if mercado:
            filter_dict["pais_mercado"] = {"_eq": mercado}
        if tipo_medio:
            filter_dict["tipo_medio"] = {"_eq": tipo_medio}
        if estado:
            filter_dict["estado_verificacion"] = {"_eq": estado}
        
        if filter_dict:
            params["filter"] = json.dumps(filter_dict)

        try:
            res = requests.get(f"{self.base_url}/items/{self.collection}", headers=self.headers, params=params, timeout=15)
            if res.status_code == 200:
                return res.json().get("data", [])
            return []
        except Exception as e:
            print(f"Error listando contactos: {e}")
            return []
