import os
import sys
import csv
import json
import argparse
from datetime import datetime
from pathlib import Path

from core.directus_client import DirectusPressClient
from core.classifier import CATEGORIES

EXPORTS_DIR = Path(__file__).resolve().parent / "exports"

def export_contacts(categoria: str = None, mercado: str = None, tipo_medio: str = None, estado: str = None, output_filename: str = None):
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    directus = DirectusPressClient()

    print(f"📥 Descargando contactos desde Directus (Categoría: {categoria or 'TODAS'}, Mercado: {mercado or 'TODOS'}, Tipo: {tipo_medio or 'TODOS'})...")
    contacts = directus.list_contacts(categoria=categoria, mercado=mercado, tipo_medio=tipo_medio, estado=estado)

    if not contacts:
        print("⚠️ No se encontraron contactos con los filtros especificados.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    cat_slug = categoria or (mercado or "todos")
    if not output_filename:
        output_filename = f"contactos_prensa_{cat_slug}_{timestamp}.csv"

    filepath = EXPORTS_DIR / output_filename

    fields = [
        "email", "nombre", "apellidos", "cargo", "medio", "pais_mercado", "tipo_medio",
        "categoria_principal", "categoria_nombre", "tipo_contacto", "telefono", "etiquetas",
        "url_medio", "url_perfil_articulo", "estado_verificacion", "fuente_origen"
    ]

    with open(filepath, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for c in contacts:
            cat_key = c.get("categoria_principal", "")
            cat_nombre = CATEGORIES.get(cat_key, {}).get("nombre", cat_key)
            tags = c.get("etiquetas")
            tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags or "")

            row = {
                "email": c.get("email", ""),
                "nombre": c.get("nombre", ""),
                "apellidos": c.get("apellidos", ""),
                "cargo": c.get("cargo", ""),
                "medio": c.get("medio", ""),
                "pais_mercado": (c.get("pais_mercado") or "es").upper(),
                "tipo_medio": c.get("tipo_medio") or "blog",
                "categoria_principal": cat_key,
                "categoria_nombre": cat_nombre,
                "tipo_contacto": c.get("tipo_contacto", ""),
                "telefono": c.get("telefono", ""),
                "etiquetas": tags_str,
                "url_medio": c.get("url_medio", ""),
                "url_perfil_articulo": c.get("url_perfil_articulo", ""),
                "estado_verificacion": c.get("estado_verificacion", ""),
                "fuente_origen": c.get("fuente_origen", "")
            }
            writer.writerow(row)

    print(f"✅ Archivo exportado con éxito ({len(contacts)} contactos):")
    print(f"   📄 {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Exportador de base de contactos de prensa para difusión")
    parser.add_argument("--categoria", type=str, help="Filtrar por categoría (ej: ocio_nocturno, gastronomia, turismo, cultura_espectaculos, estilo_de_vida, sectorial_hosteleria, generalista_madrid)")
    parser.add_argument("--mercado", type=str, help="Filtrar por mercado (ej: es, fr, it, uk, de)")
    parser.add_argument("--tipo-medio", type=str, help="Filtrar por tipo de medio (ej: blog, creador_vlogger, portal_turismo, prensa_digital)")
    parser.add_argument("--estado", type=str, default=None, help="Filtrar por estado (valido, mx_verificado, pendiente)")
    parser.add_argument("--output", type=str, default=None, help="Nombre del archivo CSV de salida")
    args = parser.parse_args()

    export_contacts(categoria=args.categoria, mercado=args.mercado, tipo_medio=args.tipo_medio, estado=args.estado, output_filename=args.output)

if __name__ == "__main__":
    main()
