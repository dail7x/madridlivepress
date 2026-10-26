import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_REGEX = re.compile(r"(?:(?:\+?34\s*)?(?:[9|6|7]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}))")
SOCIAL_PATTERNS = {
    "linkedin": re.compile(r"https?://(?:www\.)?linkedin\.com/(?:in|company)/[a-zA-Z0-9_-]+", re.I),
    "twitter": re.compile(r"https?://(?:www\.)?(?:twitter|x)\.com/[a-zA-Z0-9_]+", re.I),
    "instagram": re.compile(r"https?://(?:www\.)?instagram\.com/[a-zA-Z0-9_.]+", re.I)
}

def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()

def extract_emails(html_content: str, soup: BeautifulSoup) -> set[str]:
    emails = set()
    
    # 1. Mailto links
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.lower().startswith("mailto:"):
            email_candidate = unquote(href[7:].split("?")[0].strip())
            if "@" in email_candidate:
                emails.add(email_candidate.lower())

    # 2. Plain text regex
    for text_email in EMAIL_REGEX.findall(html_content):
        emails.add(text_email.lower())

    # 3. Obfuscated emails [at] / (arroba)
    obfuscated = re.findall(r"([a-zA-Z0-9_.+-]+)\s*(?:\[at\]|\(at\)|@)\s*([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", html_content)
    for user, dom in obfuscated:
        emails.add(f"{user}@{dom}".lower())

    return emails

def extract_phones(text: str) -> list[str]:
    matches = PHONE_REGEX.findall(text)
    clean_phones = []
    for m in matches:
        p = clean_text(m)
        if len(p) >= 9 and p not in clean_phones:
            clean_phones.append(p)
    return clean_phones

def extract_social_links(soup: BeautifulSoup) -> dict[str, str]:
    socials = {}
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        for network, pattern in SOCIAL_PATTERNS.items():
            if network not in socials and pattern.match(href):
                socials[network] = href
    return socials

def extract_editorial_team_blocks(soup: BeautifulSoup) -> list[dict]:
    """
    Intenta extraer listas de equipo/redacción cuando están formateadas
    con etiquetas de cargo y nombre (ej: <li><strong>Director:</strong> Juan Pérez</li>)
    o tablas de redacción.
    """
    contacts = []
    
    # Buscar patrones comunes en listas o párrafos
    elements = soup.find_all(["li", "p", "div", "tr"])
    role_pattern = re.compile(r"(director[a]?|redactor[a]?(?:\s+jefe)?|editor[a]?(?:\s+jefe)?|coordinador[a]?|colaborador[a]?|diseño|maquetación|fotografía)[\s:]+(.+)", re.I)

    for el in elements:
        text = clean_text(el.get_text())
        if len(text) > 200 or len(text) < 5:
            continue
        m = role_pattern.match(text)
        if m:
            cargo = clean_text(m.group(1)).capitalize()
            nombre = clean_text(m.group(2))
            
            # Si el nombre contiene email o teléfono, extraerlos
            email = None
            email_match = EMAIL_REGEX.search(nombre)
            if email_match:
                email = email_match.group(0).lower()
                nombre = nombre.replace(email, "").strip(" -–,()[]")

            # Separar nombre de apellidos si es un nombre plausible
            parts = nombre.split()
            if 2 <= len(parts) <= 4 and not any(ch in nombre for ch in ["@", "http", ".com", "www"]):
                contacts.append({
                    "nombre": parts[0],
                    "apellidos": " ".join(parts[1:]),
                    "cargo": cargo,
                    "email": email,
                    "contexto": text
                })

    return contacts

def extract_author_bylines(soup: BeautifulSoup) -> list[dict]:
    """Extrae autores de artículos o firmas."""
    authors = []
    author_nodes = soup.find_all(attrs={"rel": "author"}) or soup.find_all(class_=re.compile(r"author|byline|firma", re.I))
    for node in author_nodes:
        name = clean_text(node.get_text())
        parts = name.split()
        if 2 <= len(parts) <= 4 and not any(ch in name for ch in ["@", "http", "Publicado", "Por "]):
            # Buscar enlaces asociados al perfil del autor
            href = node.get("href") if node.name == "a" else (node.find("a")["href"] if node.find("a") else None)
            authors.append({
                "nombre": parts[0],
                "apellidos": " ".join(parts[1:]),
                "cargo": "Redactor / Periodista",
                "url_perfil": href
            })
    return authors
