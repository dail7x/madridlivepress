import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 NocheMadridPressBot/1.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

KEYWORDS_CONTACTO = [
    "contacto", "contact", "redaccion", "redacción", "equipo", "quienes-somos", 
    "quiénes somos", "staff", "aviso-legal", "legal", "prensa", "editorial"
]

class MediaCrawler:
    def __init__(self, timeout: int = 10, delay: float = 1.0):
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.timeout = timeout
        self.delay = delay
        self.visited_urls = set()

    def fetch_url(self, url: str) -> tuple[int, str, BeautifulSoup]:
        if url in self.visited_urls:
            return 0, "", None
        self.visited_urls.add(url)
        time.sleep(self.delay)

        try:
            res = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            if res.status_code == 200 and "text/html" in res.headers.get("Content-Type", ""):
                soup = BeautifulSoup(res.text, "html.parser")
                return 200, res.text, soup
            return res.status_code, "", None
        except Exception as e:
            # print(f"Error accediendo a {url}: {e}")
            return -1, "", None

    def discover_contact_links(self, base_url: str, soup: BeautifulSoup) -> list[str]:
        """Encuentra enlaces a páginas de contacto, redacción, equipo o aviso legal."""
        found_links = set()
        base_domain = urlparse(base_url).netloc

        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            
            # Asegurar que pertenece al mismo dominio o subdominio
            if parsed.netloc != base_domain:
                continue

            link_text = (a.get_text() or "").lower()
            path_lower = parsed.path.lower()

            for kw in KEYWORDS_CONTACTO:
                if kw in link_text or kw in path_lower:
                    found_links.add(full_url)
                    break

        return list(found_links)[:6]

    def discover_recent_articles(self, base_url: str, soup: BeautifulSoup) -> list[str]:
        """Encuentra enlaces a artículos recientes para identificar firmas de periodistas."""
        articles = set()
        base_domain = urlparse(base_url).netloc

        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            if parsed.netloc != base_domain:
                continue
            path = parsed.path
            
            # Patrón de artículo típico (longitud de slug razonable con guiones o fecha)
            segments = [s for s in path.split("/") if s]
            if len(segments) >= 2 and any("-" in s and len(s) > 15 for s in segments):
                articles.add(full_url)

        return list(articles)[:4]
