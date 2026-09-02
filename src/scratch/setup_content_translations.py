import requests
import json

url = 'https://mlpdirectus.116.203.118.1.sslip.io'
token = 'mlp_secret_directus_token_2026'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

print("--- 1. Setting up 'languages' collection ---")
# Check if languages collection exists
r_lang = requests.get(f'{url}/collections/languages', headers=headers)
if r_lang.status_code == 404:
    lang_col = {
        'collection': 'languages',
        'meta': {
            'singleton': False,
            'hidden': False,
            'icon': 'translate',
            'translations': [
                {'language': 'es-ES', 'translation': 'Idiomas'},
                {'language': 'en-US', 'translation': 'Languages'}
            ]
        },
        'schema': {},
        'fields': [
            {
                'field': 'code',
                'type': 'string',
                'meta': {
                    'primary_key': True,
                    'interface': 'input',
                    'required': True
                },
                'schema': {
                    'is_primary_key': True,
                    'is_nullable': False
                }
            },
            {
                'field': 'name',
                'type': 'string',
                'meta': {
                    'interface': 'input',
                    'required': True
                },
                'schema': {'is_nullable': False}
            },
            {
                'field': 'direction',
                'type': 'string',
                'meta': {
                    'interface': 'select-dropdown',
                    'options': {
                        'choices': [
                            {'text': 'Left to Right (LTR)', 'value': 'ltr'},
                            {'text': 'Right to Left (RTL)', 'value': 'rtl'}
                        ]
                    }
                },
                'schema': {'default_value': 'ltr'}
            }
        ]
    }
    r_create_lang = requests.post(f'{url}/collections', headers=headers, json=lang_col)
    print('Created languages collection:', r_create_lang.status_code)
else:
    print("languages collection already exists.")

# Seed languages
languages_data = [
    {'code': 'es-ES', 'name': 'Español', 'direction': 'ltr'},
    {'code': 'en-US', 'name': 'English', 'direction': 'ltr'}
]
for lang in languages_data:
    r_seed = requests.post(f'{url}/items/languages', headers=headers, json=lang)
    print(f"Seed language {lang['code']}: {r_seed.status_code}")

print("\n--- 2. Setting up 'comunicados_translations' collection ---")
r_trans = requests.get(f'{url}/collections/comunicados_translations', headers=headers)
if r_trans.status_code == 404:
    trans_col = {
        'collection': 'comunicados_translations',
        'meta': {
            'hidden': True,
            'icon': 'translate'
        },
        'schema': {},
        'fields': [
            {
                'field': 'id',
                'type': 'integer',
                'meta': {'primary_key': True, 'hidden': True},
                'schema': {'is_primary_key': True, 'has_auto_increment': True}
            },
            {
                'field': 'comunicados_id',
                'type': 'integer',
                'meta': {'hidden': True},
                'schema': {'is_nullable': True}
            },
            {
                'field': 'languages_code',
                'type': 'string',
                'meta': {'interface': 'select-dropdown-m2o'},
                'schema': {'is_nullable': True}
            },
            {
                'field': 'titulo',
                'type': 'string',
                'meta': {'interface': 'input', 'width': 'full'}
            },
            {
                'field': 'slug',
                'type': 'string',
                'meta': {'interface': 'input', 'width': 'full'}
            },
            {
                'field': 'bajada',
                'type': 'text',
                'meta': {'interface': 'input-multiline'}
            },
            {
                'field': 'cuerpo',
                'type': 'text',
                'meta': {'interface': 'input-rich-text-html'}
            },
            {
                'field': 'audio_script',
                'type': 'text',
                'meta': {'interface': 'input-multiline'}
            },
            {
                'field': 'puntos_clave',
                'type': 'json',
                'meta': {'interface': 'list'}
            }
        ]
    }
    r_create_trans = requests.post(f'{url}/collections', headers=headers, json=trans_col)
    print('Created comunicados_translations collection:', r_create_trans.status_code)
else:
    print("comunicados_translations collection already exists.")

print("\n--- 3. Creating Relations for Content Translations ---")
# 1) Relation comunicados_translations.comunicados_id -> comunicados.id
r_rel1 = requests.post(f'{url}/relations', headers=headers, json={
    'collection': 'comunicados_translations',
    'field': 'comunicados_id',
    'related_collection': 'comunicados',
    'meta': {
        'many_collection': 'comunicados_translations',
        'many_field': 'comunicados_id',
        'one_collection': 'comunicados',
        'one_field': 'translations',
        'junction_field': 'languages_code'
    },
    'schema': {'on_delete': 'CASCADE'}
})
print('Relation 1 (comunicados_id):', r_rel1.status_code)

# 2) Relation comunicados_translations.languages_code -> languages.code
r_rel2 = requests.post(f'{url}/relations', headers=headers, json={
    'collection': 'comunicados_translations',
    'field': 'languages_code',
    'related_collection': 'languages',
    'meta': {
        'many_collection': 'comunicados_translations',
        'many_field': 'languages_code',
        'one_collection': 'languages'
    },
    'schema': {'on_delete': 'SET NULL'}
})
print('Relation 2 (languages_code):', r_rel2.status_code)

# 3) Add the translations alias field to comunicados if missing
r_f_trans = requests.post(f'{url}/fields/comunicados', headers=headers, json={
    'field': 'translations',
    'type': 'alias',
    'meta': {
        'interface': 'translations',
        'special': ['translations']
    }
})
print('Field comunicados.translations alias:', r_f_trans.status_code)

# 4) Enable public read permissions on languages and comunicados_translations
for col in ['languages', 'comunicados_translations']:
    r_perm = requests.post(f'{url}/permissions', headers=headers, json={
        'collection': col,
        'action': 'read',
        'fields': ['*'],
        'role': None
    })
    print(f'Public permission for {col}: {r_perm.status_code}')

print("\n--- Directus Content Translations schema setup completed! ---")
