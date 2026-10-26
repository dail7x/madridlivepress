import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "categories.json"

def load_categories_config():
    if not CONFIG_PATH.exists():
        return {"categories": {}, "roles_keywords": {}}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

CONFIG = load_categories_config()
CATEGORIES = CONFIG.get("categories", {})
ROLES = CONFIG.get("roles_keywords", {})

def classify_role(text: str, default: str = "Redactor / Periodista") -> str:
    """Detecta el cargo o función a partir de un texto (cargo declarado, bio o contexto)."""
    if not text:
        return default
    text_lower = text.lower()
    for role_name, keywords in ROLES.items():
        for kw in keywords:
            if kw in text_lower:
                return role_name
    return default

def classify_category(text_corpus: str, fallback: str = "ocio_nocturno") -> tuple[str, list[str]]:
    """
    Analiza un texto o contenido web y determina la categoría principal y las etiquetas recomendadas
    calculando la mayor frecuencia de palabras clave.
    """
    if not text_corpus:
        cat_info = CATEGORIES.get(fallback, {})
        return fallback, cat_info.get("default_tags", [fallback])

    text_lower = text_corpus.lower()
    scores = {}
    found_tags = set()

    for cat_key, cat_data in CATEGORIES.items():
        score = 0
        keywords = cat_data.get("keywords", [])
        for kw in keywords:
            if kw in text_lower:
                score += 1
                if score <= 4:
                    tag_candidate = kw.replace(" ", "-")
                    found_tags.add(tag_candidate)
        scores[cat_key] = score

    best_cat = max(scores, key=scores.get) if scores and max(scores.values()) > 0 else fallback
    cat_default_tags = CATEGORIES.get(best_cat, {}).get("default_tags", [])
    all_tags = list(set(cat_default_tags).union(found_tags))[:8]

    return best_cat, all_tags
