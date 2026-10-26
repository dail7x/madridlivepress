import os
import requests
import json

DIRECTUS_URL = os.environ.get('DIRECTUS_URL', 'https://mlpdirectus.116.203.118.1.sslip.io')
DIRECTUS_TOKEN = os.environ.get('DIRECTUS_STATIC_TOKEN', 'mlp_secret_directus_token_2026')

headers = {
    'Authorization': f'Bearer {DIRECTUS_TOKEN}',
    'Content-Type': 'application/json'
}

def create_collection_if_not_exists():
    res = requests.get(f"{DIRECTUS_URL}/collections/contactos_prensa", headers=headers)
    if res.status_code == 200:
        print("La colección 'contactos_prensa' ya existe en Directus.")
        return

    payload = {
        "collection": "contactos_prensa",
        "meta": {
            "collection": "contactos_prensa",
            "icon": "contact_mail",
            "note": "Base de contactos de periodistas y medios segmentados para Noche Madrid Press",
            "display_template": "{{nombre}} {{apellidos}} - {{medio}} ({{cargo}})"
        },
        "schema": {},
        "fields": [
            {
                "field": "id",
                "type": "integer",
                "schema": {
                    "is_primary_key": True,
                    "has_auto_increment": True
                }
            }
        ]
    }
    create_res = requests.post(f"{DIRECTUS_URL}/collections", headers=headers, json=payload)
    if create_res.status_code in [200, 204]:
        print("Colección 'contactos_prensa' creada con éxito.")
    else:
        print(f"Error creando colección: {create_res.status_code} - {create_res.text}")

def add_or_update_field(field_name, field_type, interface="input", options=None, is_nullable=True, default_value=None):
    res = requests.get(f"{DIRECTUS_URL}/fields/contactos_prensa/{field_name}", headers=headers)
    if res.status_code == 200:
        print(f"Campo '{field_name}' ya existe.")
        return

    payload = {
        "field": field_name,
        "type": field_type,
        "meta": {
            "interface": interface,
            "special": None,
            "options": options or {}
        },
        "schema": {
            "is_nullable": is_nullable,
            "default_value": default_value
        }
    }

    if field_type == "text":
        payload["meta"]["interface"] = "input-multiline"
    elif field_type == "json":
        payload["meta"]["interface"] = interface if interface != "input" else "list"
    elif field_type == "boolean":
        payload["meta"]["interface"] = "boolean"

    r = requests.post(f"{DIRECTUS_URL}/fields/contactos_prensa", headers=headers, json=payload)
    if r.status_code in [200, 204]:
        print(f"Campo 'contactos_prensa.{field_name}' creado exitosamente.")
    else:
        print(f"Error al crear campo '{field_name}': {r.status_code} - {r.text[:120]}")

def setup_schema():
    print(f"Conectando a Directus: {DIRECTUS_URL}...")
    create_collection_if_not_exists()

    add_or_update_field("nombre", "string", "input")
    add_or_update_field("apellidos", "string", "input")
    add_or_update_field("cargo", "string", "input")
    add_or_update_field("medio", "string", "input")
    add_or_update_field("url_medio", "string", "input")
    add_or_update_field("url_perfil_articulo", "string", "input")
    add_or_update_field("email", "string", "input", is_nullable=False)
    add_or_update_field("telefono", "string", "input")

    # Categoría Principal con opciones predefinidas
    cat_options = {
        "choices": [
            {"text": "Ocio Nocturno y Entretenimiento", "value": "ocio_nocturno"},
            {"text": "Gastronomía y Restauración", "value": "gastronomia"},
            {"text": "Turismo y Destino Madrid", "value": "turismo"},
            {"text": "Cultura y Espectáculos", "value": "cultura_espectaculos"},
            {"text": "Tendencias y Estilo de Vida (Lifestyle)", "value": "estilo_de_vida"},
            {"text": "Revistas Sectoriales y Hostelería B2B", "value": "sectorial_hosteleria"},
            {"text": "Prensa Generalista y Agencias (Madrid)", "value": "generalista_madrid"}
        ]
    }
    add_or_update_field("categoria_principal", "string", "select-dropdown", cat_options, default_value="ocio_nocturno")
    
    # País / Mercado objetivo
    mercado_options = {
        "choices": [
            {"text": "España (Nacional / Madrid)", "value": "es"},
            {"text": "Francia (Francófono)", "value": "fr"},
            {"text": "Italia (Italiano)", "value": "it"},
            {"text": "Reino Unido / Internacional (Inglés)", "value": "uk"},
            {"text": "Alemania / DACH (Alemán)", "value": "de"},
            {"text": "Internacional / Global", "value": "int"}
        ]
    }
    add_or_update_field("pais_mercado", "string", "select-dropdown", mercado_options, default_value="es")

    # Tipo de medio / Creador
    tipo_medio_options = {
        "choices": [
            {"text": "Blog Especializado Independiente", "value": "blog"},
            {"text": "Creador de Contenido / Vlogger / Foodie", "value": "creador_vlogger"},
            {"text": "Guía de Ocio / Portal de Viajes", "value": "portal_turismo"},
            {"text": "Prensa Digital / Revista", "value": "prensa_digital"}
        ]
    }
    add_or_update_field("tipo_medio", "string", "select-dropdown", tipo_medio_options, default_value="blog")

    add_or_update_field("etiquetas", "json", "tags")

    tipo_options = {
        "choices": [
            {"text": "Periodista / Creador / Persona directa", "value": "personal"},
            {"text": "Buzón general / Contacto del Blog", "value": "redaccion_general"}
        ]
    }
    add_or_update_field("tipo_contacto", "string", "select-dropdown", tipo_options, default_value="personal")
    add_or_update_field("redes_sociales", "json", "list")

    estado_options = {
        "choices": [
            {"text": "Válido (MX y sintaxis verificados)", "value": "valido"},
            {"text": "Pendiente de verificación", "value": "pendiente"},
            {"text": "Servidor de correo inválido (Sin MX)", "value": "mx_invalido"},
            {"text": "Baja solicitada / Exclusión", "value": "baja"}
        ]
    }
    add_or_update_field("estado_verificacion", "string", "select-dropdown", estado_options, default_value="pendiente")
    add_or_update_field("fuente_origen", "string", "input")
    add_or_update_field("notas", "text", "input-multiline")

    print("Configuración del esquema 'contactos_prensa' finalizada.")

if __name__ == "__main__":
    setup_schema()
