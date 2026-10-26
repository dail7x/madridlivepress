import re
import dns.resolver

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

GENERIC_PREFIXES = {
    "redaccion", "prensa", "comunicacion", "info", "contacto", "redaccionmadrid",
    "prensamadrid", "noticias", "agenda", "cultura", "ocio", "redactores", "gabinete",
    "medios", "redaccionweb", "digital", "comercial", "publicidad", "admin", "soporte"
}

IGNORED_DOMAINS = {
    "example.com", "domain.com", "wix.com", "wordpress.com", "sentry.io",
    "cloudflare.com", "schema.org", "w3.org", "google.com", "apple.com",
    "gravatar.com", "facebook.com", "twitter.com", "instagram.com"
}

_MX_CACHE = {}

def is_valid_email_syntax(email: str) -> bool:
    if not email or len(email) > 254:
        return False
    email = email.strip().lower()
    if not EMAIL_REGEX.match(email):
        return False
    domain = email.split("@")[-1]
    if domain in IGNORED_DOMAINS:
        return False
    # Evitar archivos mal interpretados como emails (ej: image@2x.png)
    if domain.split(".")[-1] in ["png", "jpg", "jpeg", "webp", "gif", "svg", "css", "js"]:
        return False
    return True

def classify_email_type(email: str) -> str:
    """Retorna 'personal' o 'redaccion_general' según el alias de correo."""
    if not email:
        return "redaccion_general"
    local_part = email.split("@")[0].lower().replace(".", "").replace("-", "").replace("_", "")
    for prefix in GENERIC_PREFIXES:
        if local_part == prefix or local_part.startswith(prefix):
            return "redaccion_general"
    return "personal"

def check_domain_mx(domain: str, timeout: float = 3.0) -> bool:
    """Verifica si el dominio tiene registros MX válidos para recibir correos."""
    domain = domain.strip().lower()
    if domain in _MX_CACHE:
        return _MX_CACHE[domain]

    try:
        resolver = dns.resolver.Resolver()
        resolver.lifetime = timeout
        resolver.timeout = timeout
        answers = resolver.resolve(domain, "MX")
        has_mx = len(answers) > 0
        _MX_CACHE[domain] = has_mx
        return has_mx
    except Exception:
        # Si falla MX, intentar fallback de registro A
        try:
            answers = resolver.resolve(domain, "A")
            has_a = len(answers) > 0
            _MX_CACHE[domain] = has_a
            return has_a
        except Exception:
            _MX_CACHE[domain] = False
            return False

def validate_contact_email(email: str, verify_mx: bool = True) -> tuple[bool, str, str]:
    """
    Retorna: (es_valido, tipo_contacto, estado_verificacion)
    tipo_contacto: 'personal' | 'redaccion_general'
    estado_verificacion: 'valido' | 'mx_invalido' | 'invalido'
    """
    if not is_valid_email_syntax(email):
        return False, "redaccion_general", "invalido"

    domain = email.split("@")[-1]
    tipo = classify_email_type(email)

    if verify_mx:
        has_mx = check_domain_mx(domain)
        if not has_mx:
            return False, tipo, "mx_invalido"
        return True, tipo, "valido"

    return True, tipo, "pendiente"
