import os
import sys
import json
import argparse
from pathlib import Path
from urllib.parse import urljoin, urlparse

from core.crawler import MediaCrawler
from core.extractor import (
    extract_emails, extract_phones, extract_social_links,
    extract_editorial_team_blocks, extract_author_bylines
)
from core.classifier import classify_category, classify_role, CATEGORIES
from core.validator import validate_contact_email
from core.directus_client import DirectusPressClient

CONFIG_DIR = Path(__file__).resolve().parent / "config"
SEEDS_FILE = CONFIG_DIR / "seeds.json"

def load_seeds():
    if not SEEDS_FILE.exists():
        return []
    with open(SEEDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f).get("media_seeds", [])

def process_media_seed(seed: dict, crawler: MediaCrawler, existing_emails: set[str], verify_mx: bool = True) -> list[dict]:
    medio_name = seed.get("medio", "Medio Digital")
    base_url = seed.get("url", "")
    categoria_base = seed.get("categoria", "ocio_nocturno")
    etiquetas_base = seed.get("etiquetas", [])
    paths_contacto = seed.get("paths_contacto", ["/contacto", "/quienes-somos"])

    print(f"\n🔍 [PROSPECCIÓN] Medio: {medio_name} ({base_url})")
    print(f"   Categoría asignada: {categoria_base}")

    found_contacts = []
    seen_page_emails = set()

    # 1. Fetch Homepage
    code, html, soup = crawler.fetch_url(base_url)
    all_pages_to_crawl = []

    if soup:
        # Descubrir enlaces de contacto en el menú / footer
        discovered = crawler.discover_contact_links(base_url, soup)
        all_pages_to_crawl.extend(discovered)
        # Descubrir artículos recientes para firmas
        articles = crawler.discover_recent_articles(base_url, soup)
        all_pages_to_crawl.extend(articles)

    # Añadir rutas explícitas de la configuración semilla
    for p in paths_contacto:
        full = urljoin(base_url, p)
        if full not in all_pages_to_crawl:
            all_pages_to_crawl.append(full)

    print(f"   Páginas a explorar: {len(all_pages_to_crawl)} (contacto, redacción y artículos)")

    # 2. Explorar páginas objetivo
    for target_url in all_pages_to_crawl:
        c_code, c_html, c_soup = crawler.fetch_url(target_url)
        if not c_soup:
            continue

        # Extraer correos
        page_emails = extract_emails(c_html, c_soup)
        social_links = extract_social_links(c_soup)
        phones = extract_phones(c_html)
        phone = phones[0] if phones else None

        # Bloques de equipo / redacción
        team_members = extract_editorial_team_blocks(c_soup)
        # Firmas de autor si es artículo
        authors = extract_author_bylines(c_soup)

        # Analizar correos encontrados
        for email in page_emails:
            email_lower = email.lower().strip()
            if email_lower in existing_emails or email_lower in seen_page_emails:
                continue

            valid, tipo_contacto, estado = validate_contact_email(email_lower, verify_mx=verify_mx)
            if not valid and estado == "invalido":
                continue

            # Buscar si este email coincide con algún miembro de equipo detectado
            matched_member = next((m for m in team_members if m.get("email") == email_lower), None)
            
            if matched_member:
                nombre = matched_member["nombre"]
                apellidos = matched_member["apellidos"]
                cargo = classify_role(matched_member["cargo"])
            elif tipo_contacto == "redaccion_general":
                nombre = "Redacción"
                apellidos = medio_name
                cargo = "Buzón de Redacción"
            else:
                # Si hay autores y solo un correo personal en la página de autor
                if len(authors) == 1:
                    nombre = authors[0]["nombre"]
                    apellidos = authors[0]["apellidos"]
                    cargo = authors[0].get("cargo", "Redactor / Periodista")
                else:
                    user_part = email_lower.split("@")[0]
                    nombre = user_part.replace(".", " ").title()
                    apellidos = ""
                    cargo = "Redactor / Periodista"

            contact_obj = {
                "nombre": nombre,
                "apellidos": apellidos,
                "cargo": cargo,
                "medio": medio_name,
                "url_medio": base_url,
                "url_perfil_articulo": target_url,
                "email": email_lower,
                "telefono": phone,
                "categoria_principal": categoria_base,
                "pais_mercado": seed.get("pais_mercado", "es"),
                "tipo_medio": seed.get("tipo_medio", "blog"),
                "etiquetas": etiquetas_base,
                "tipo_contacto": tipo_contacto,
                "redes_sociales": social_links,
                "estado_verificacion": estado,
                "fuente_origen": target_url,
                "notas": f"Descubierto automáticamente por NocheMadrid Press Bot desde {target_url}"
            }

            seen_page_emails.add(email_lower)
            found_contacts.append(contact_obj)
            print(f"   ✨ Encontrado: {email_lower} | {nombre} {apellidos} ({cargo}) | {seed.get('pais_mercado', 'es').upper()} | {estado}")

    return found_contacts

def run(categories_filter: list[str] = None, mercados_filter: list[str] = None, tipo_medio_filter: str = None, verify_mx: bool = True, dry_run: bool = False):
    print("=" * 65)
    print("🤖 INICIANDO BOT DE PROSPECCIÓN Y SEGMENTACIÓN DE PRENSA")
    print("   Noche Madrid Press — Detector de Periodistas, Blogs y Creadores")
    print("=" * 65)

    directus = DirectusPressClient()
    existing_emails = set()
    if not dry_run:
        print("📥 Conectando con Directus para consultar contactos existentes...")
        existing_emails = directus.get_existing_emails()
        print(f"   Contactos ya registrados en Directus: {len(existing_emails)}")

    seeds = load_seeds()
    if categories_filter:
        seeds = [s for s in seeds if s.get("categoria") in categories_filter]
        print(f"🎯 Filtrando por categorías: {', '.join(categories_filter)}")

    if mercados_filter:
        seeds = [s for s in seeds if s.get("pais_mercado") in mercados_filter]
        print(f"🌍 Filtrando por mercados: {', '.join(mercados_filter).upper()}")

    if tipo_medio_filter:
        seeds = [s for s in seeds if s.get("tipo_medio") == tipo_medio_filter]
        print(f"📰 Filtrando por tipo de medio: {tipo_medio_filter}")

    print(f"📋 Total de medios/blogs semilla a prospectar: {len(seeds)}")

    crawler = MediaCrawler(timeout=8, delay=0.6)
    total_new_contacts = 0
    saved_contacts_by_cat = {}

    for seed in seeds:
        new_contacts = process_media_seed(seed, crawler, existing_emails, verify_mx=verify_mx)
        for c in new_contacts:
            cat = c["categoria_principal"]
            saved_contacts_by_cat[cat] = saved_contacts_by_cat.get(cat, 0) + 1
            total_new_contacts += 1

            if not dry_run:
                directus.save_contact(c)
                existing_emails.add(c["email"])

    print("\n" + "=" * 65)
    print("📊 RESUMEN DE PROSPECCIÓN Y CLASIFICACIÓN")
    print("=" * 65)
    print(f"Total contactos nuevos procesados: {total_new_contacts}")
    print("Distribución por categorías segmentadas:")
    for cat, count in saved_contacts_by_cat.items():
        cat_name = CATEGORIES.get(cat, {}).get("nombre", cat)
        print(f"  • {cat_name}: {count} contactos")
    
    if dry_run:
        print("\n⚠️ Modo simulado (Dry Run): No se guardaron registros en Directus.")
    else:
        print("\n✅ Todos los nuevos contactos se han sincronizado en Directus.")

def main():
    parser = argparse.ArgumentParser(description="Bot de prospección de contactos de prensa, blogs y creadores para Noche Madrid Press")
    parser.add_argument("--categoria", type=str, help="Filtrar por categoría (ej: ocio_nocturno, gastronomia, turismo, cultura_espectaculos, estilo_de_vida, sectorial_hosteleria, generalista_madrid)")
    parser.add_argument("--mercado", type=str, help="Filtrar por mercado/país (ej: es, fr, it, uk, de)")
    parser.add_argument("--tipo-medio", type=str, help="Filtrar por tipo de medio (ej: blog, creador_vlogger, portal_turismo, prensa_digital)")
    parser.add_argument("--no-mx", action="store_true", help="Desactivar verificación DNS MX para mayor velocidad")
    parser.add_argument("--dry-run", action="store_true", help="Ejecutar sin guardar en Directus")
    args = parser.parse_args()

    cats = [args.categoria] if args.categoria else None
    mercados = [args.mercado] if args.mercado else None
    run(categories_filter=cats, mercados_filter=mercados, tipo_medio_filter=args.tipo_medio, verify_mx=not args.no_mx, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
