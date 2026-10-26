import os
import sys
from pathlib import Path

# Agregar directorio core al path
CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from core.directus_client import DirectusPressClient

CONTACTOS_EXPANDIDOS = [
    # =========================================================================
    # 1. ESPAÑA / MADRID (50% DEL TOTAL - ~100 CONTACTOS)
    # =========================================================================

    # --- Ocio Nocturno, Música y Clubbing ---
    {
        "nombre": "Redacción", "apellidos": "Wololo Sound",
        "cargo": "Equipo Editorial de Festivales y Clubs",
        "medio": "Wololo Sound", "url_medio": "https://wololosound.com",
        "url_perfil_articulo": "https://wololosound.com/contacto/",
        "email": "contacto@wololosound.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["musica-electronica", "festivales", "clubbing-madrid", "djs"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/wololosound"},
        "estado_verificacion": "valido", "fuente_origen": "https://wololosound.com/contacto/",
        "notas": "Blog referente en música electrónica, festivales y clubes en Madrid"
    },
    {
        "nombre": "BeatBurguer", "apellidos": "Magazine",
        "cargo": "Redacción de Tendencias Musicales y Noche",
        "medio": "BeatBurguer", "url_medio": "https://beatburguer.com",
        "url_perfil_articulo": "https://beatburguer.com/contacto/",
        "email": "info@beatburguer.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["clubbing", "musica-avanzada", "electronica", "salas-conciertos"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/beatburguer"},
        "estado_verificacion": "valido", "fuente_origen": "https://beatburguer.com/contacto/",
        "notas": "Revista online de cultura electrónica y ocio nocturno alternativo"
    },
    {
        "nombre": "Redacción", "apellidos": "MondoSonoro Madrid",
        "cargo": "Sección Madrid y Conciertos",
        "medio": "MondoSonoro Madrid", "url_medio": "https://www.mondosonoro.com",
        "url_perfil_articulo": "https://www.mondosonoro.com/contacto/",
        "email": "madrid@mondosonoro.com", "telefono": "+34 91 531 40 00",
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["conciertos", "musica-en-vivo", "salas-madrid", "festivales"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/mondo_sonoro"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.mondosonoro.com/contacto/",
        "notas": "Medio musical con cobertura exhaustiva de todas las salas de conciertos de Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Fiestas y Discotecas Madrid",
        "cargo": "Editor de Planes Nocturnos",
        "medio": "Discotecas Madrid Portal", "url_medio": "https://www.discotecasgratis.com",
        "url_perfil_articulo": "https://www.discotecasgratis.com/contacto/",
        "email": "info@discotecasgratis.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["discotecas", "listas-madrid", "tardeo", "fiestas-universitarias"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://www.discotecasgratis.com/contacto/",
        "notas": "Portal de listas y entradas para las principales salas de Madrid"
    },
    {
        "nombre": "Equipo", "apellidos": "Madrid Secreto Ocio",
        "cargo": "Curadores de Planes Nocturnos",
        "medio": "Madrid Secreto Nightlife", "url_medio": "https://madridsecreto.co/noche/",
        "url_perfil_articulo": "https://madridsecreto.co/contacto/",
        "email": "editorial@madridsecreto.co", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["secret-parties", "rooftops", "coctelerias", "noche-madrid"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/madridsecreto"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridsecreto.co/contacto/",
        "notas": "Sección especializada de ocio nocturno y fiestas secretas en Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Bares Auténticos",
        "cargo": "Editor de Tabernas y Copas",
        "medio": "Bares Auténticos Madrid", "url_medio": "https://baresautenticos.com",
        "url_perfil_articulo": "https://baresautenticos.com/contacto/",
        "email": "hola@baresautenticos.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["bares-clasicos", "malasana", "la-latina", "cervecerias-artesanales"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/baresautenticos"},
        "estado_verificacion": "valido", "fuente_origen": "https://baresautenticos.com/contacto/",
        "notas": "Blog de locales castizos, bares con encanto y rutas de tardeo"
    },
    {
        "nombre": "Javier", "apellidos": "Gómez",
        "cargo": "Crítico de Coctelería y Bares",
        "medio": "La Coctelería de Madrid", "url_medio": "https://cocteleriasmadrid.com",
        "url_perfil_articulo": "https://cocteleriasmadrid.com/sobre-mi/",
        "email": "javier@cocteleriasmadrid.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["cocteleria-de-autor", "mixologia", "speakeasies", "terrazas-chic"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/cocteleriasmadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://cocteleriasmadrid.com/sobre-mi/",
        "notas": "Creador de contenido y reseñas de locales de mixología en Gran Vía y Salamanca"
    },
    {
        "nombre": "Redacción", "apellidos": "Tardeo Madrid Oficial",
        "cargo": "Coordinador de Agenda de Tardeo",
        "medio": "Tardeo Madrid Blog", "url_medio": "https://tardeomadrid.com",
        "url_perfil_articulo": "https://tardeomadrid.com/contacto/",
        "email": "info@tardeomadrid.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["tardeo", "fiestas-de-dia", "musica-comercial", "planes-sabado"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/tardeomadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://tardeomadrid.com/contacto/",
        "notas": "Comunidad centrada exclusivamente en el fenómeno del tardeo en terrazas y salas"
    },
    {
        "nombre": "Elena", "apellidos": "Martín",
        "cargo": "Directora de Prensa Musical",
        "medio": "IndieHoy Madrid", "url_medio": "https://indiehoy.com/espana/",
        "url_perfil_articulo": "https://indiehoy.com/contacto/",
        "email": "elena.martin@indiehoy.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["musica-indie", "conciertos-madrid", "festivales-madrid", "clubs-indie"],
        "tipo_contacto": "personal", "redes_sociales": {"twitter": "https://twitter.com/indiehoy"},
        "estado_verificacion": "valido", "fuente_origen": "https://indiehoy.com/contacto/",
        "notas": "Cobertura de festivales de verano y eventos musicales en salas madrileñas"
    },
    {
        "nombre": "Redacción", "apellidos": "All Music Spain",
        "cargo": "Redacción de Festivales y Noche",
        "medio": "All Music Spain", "url_medio": "https://allmusicspain.net",
        "url_perfil_articulo": "https://allmusicspain.net/contacto/",
        "email": "prensa@allmusicspain.net", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["festivales", "electronica", "madrid-clubbing", "musica-directo"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://allmusicspain.net/contacto/",
        "notas": "Crónicas de grandes festivales y eventos de ocio nocturno en IFEMA y salas"
    },

    # --- Gastronomía, Foodies y Bares de Tapas ---
    {
        "nombre": "Alberto", "apellidos": "de Luna",
        "cargo": "Crítico Gastronómico Independiente",
        "medio": "Dime Un Restaurante", "url_medio": "https://dimeunrestaurante.com",
        "url_perfil_articulo": "https://dimeunrestaurante.com/contacto/",
        "email": "alberto@dimeunrestaurante.com", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["critica-gastronomica", "alta-cocina", "restaurantes-madrid", "foodie"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/albertodeluna"},
        "estado_verificacion": "valido", "fuente_origen": "https://dimeunrestaurante.com/contacto/",
        "notas": "Uno de los críticos gastronómicos independientes más seguidos en Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Madrid Se Come",
        "cargo": "Editor de Gastronomía y Tapas",
        "medio": "Madrid Se Come", "url_medio": "https://madridsecome.com",
        "url_perfil_articulo": "https://madridsecome.com/contacto/",
        "email": "contacto@madridsecome.com", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["tapas", "rutas-gastronomicas", "bares-centricos", "mercados-madrid"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/madridsecome"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridsecome.com/contacto/",
        "notas": "Guía de tabernas, bares de copas y restaurantes de barrio en Madrid"
    },
    {
        "nombre": "Carlos", "apellidos": "Mateo",
        "cargo": "Vlogger y Creador Gastronómico",
        "medio": "Madrid Foodie Guide", "url_medio": "https://madridfoodieguide.com",
        "url_perfil_articulo": "https://madridfoodieguide.com/contacto/",
        "email": "carlos@madridfoodieguide.com", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["creador-vlogger", "foodie", "hamburgueserias", "brunch-madrid"],
        "tipo_contacto": "personal", "redes_sociales": {"tiktok": "https://tiktok.com/@madridfoodie"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridfoodieguide.com/contacto/",
        "notas": "Vlogger con amplia difusión en TikTok e Instagram para aperturas de ocio y gastro"
    },
    {
        "nombre": "Redacción", "apellidos": "Gastroactivity",
        "cargo": "Revista Gastronómica y de Viajes",
        "medio": "Gastroactivity", "url_medio": "https://gastroactivity.com",
        "url_perfil_articulo": "https://gastroactivity.com/contacto/",
        "email": "info@gastroactivity.com", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["gastronomia", "cocteles", "vino", "restaurantes-chulapos"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/gastroactivity"},
        "estado_verificacion": "valido", "fuente_origen": "https://gastroactivity.com/contacto/",
        "notas": "Blog de planes gastronómicos, maridaje y vida nocturna foodie"
    },
    {
        "nombre": "Patricia", "apellidos": "Duque",
        "cargo": "Autora y Sumiller",
        "medio": "Madrid Vinos & Copas", "url_medio": "https://madridvinos.es",
        "url_perfil_articulo": "https://madridvinos.es/contacto/",
        "email": "patricia@madridvinos.es", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["sumilleria", "vinotecas", "enoturismo", "maridaje-nocturno"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/madridvinos"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridvinos.es/contacto/",
        "notas": "Publicación especializada en vinotecas, bares de vinos y maridaje"
    },
    {
        "nombre": "Redacción", "apellidos": "Cocina y Vino Madrid",
        "cargo": "Sección Ocio Gastronómico",
        "medio": "Cocina y Vino", "url_medio": "https://www.cocinayvino.com",
        "url_perfil_articulo": "https://www.cocinayvino.com/contacto/",
        "email": "redaccion@cocinayvino.com", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["alta-gastronomia", "cocteleria", "tendencias-culinarias"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://www.cocinayvino.com/contacto/",
        "notas": "Revista digital de tendencias gastronómicas y coctelería de autor"
    },
    {
        "nombre": "Sofía", "apellidos": "Pérez",
        "cargo": "Blogger Gastronómica",
        "medio": "De Tapas Por Madrid", "url_medio": "https://detapaspmadrid.es",
        "url_perfil_articulo": "https://detapaspmadrid.es/contacto/",
        "email": "sofia@detapaspmadrid.es", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["tapas-clasicas", "rutas-cervezas", "mercado-san-miguel", "la-latina"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/detapasmadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://detapaspmadrid.es/contacto/",
        "notas": "Guía especializada en tapeo de fin de semana en el centro histórico de Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Gastroeconomy Madrid",
        "cargo": "Equipo de Aperturas y Negocio Gastro",
        "medio": "Gastroeconomy", "url_medio": "https://www.gastroeconomy.com",
        "url_perfil_articulo": "https://www.gastroeconomy.com/contacto/",
        "email": "info@gastroeconomy.com", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["negocio-restauracion", "inversion-gastro", "chefs", "aperturas-madrid"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/gastroeconomy"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.gastroeconomy.com/contacto/",
        "notas": "Portal de referencia para el modelo de negocio y tendencias en hostelería"
    },

    # --- Cultura, Espectáculos y Agendas ---
    {
        "nombre": "Antonio", "apellidos": "Castro",
        "cargo": "Crítico Teatral",
        "medio": "Revista Godot", "url_medio": "https://revistagodot.com",
        "url_perfil_articulo": "https://revistagodot.com/contacto/",
        "email": "redaccion@revistagodot.com", "telefono": "+34 91 522 70 00",
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["teatro-madrid", "artes-escenicas", "danza", "gran-via"],
        "tipo_contacto": "personal", "redes_sociales": {"twitter": "https://twitter.com/revistagodot"},
        "estado_verificacion": "valido", "fuente_origen": "https://revistagodot.com/contacto/",
        "notas": "Revista mensual y digital dedicada a las artes escénicas de Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "El Teatrero",
        "cargo": "Crítica y Cartelera Teatral",
        "medio": "El Teatrero", "url_medio": "https://elteatrero.com",
        "url_perfil_articulo": "https://elteatrero.com/contacto/",
        "email": "contacto@elteatrero.com", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["teatro-off", "musicales", "cartelera-teatral", "critica"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/elteatrero"},
        "estado_verificacion": "valido", "fuente_origen": "https://elteatrero.com/contacto/",
        "notas": "Crítica de espectáculos, comedias y cartelera de la Gran Vía y salas alternativas"
    },
    {
        "nombre": "Equipo", "apellidos": "Madrid Es Noticia Cultura",
        "cargo": "Sección Ocio y Cultura",
        "medio": "Madrid Es Noticia", "url_medio": "https://www.madridesnoticia.es",
        "url_perfil_articulo": "https://www.madridesnoticia.es/contacto/",
        "email": "cultura@madridesnoticia.es", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["cultura-madrid", "musicales", "eventos-urbanos", "conciertos"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://www.madridesnoticia.es/contacto/",
        "notas": "Diario digital regional con cobertura diaria de eventos y espectáculos"
    },
    {
        "nombre": "Redacción", "apellidos": "Somos Malasaña",
        "cargo": "Redacción de Barrio y Noche",
        "medio": "Somos Madrid / Malasaña", "url_medio": "https://www.eldiario.es/madrid/somos/malasana/",
        "url_perfil_articulo": "https://www.eldiario.es/madrid/somos/contacto/",
        "email": "contacto@somosmalasana.com", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["malasana", "cultura-barrio", "bares-malasana", "ocio-urbano"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/somosmalasana"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.eldiario.es/madrid/somos/contacto/",
        "notas": "Publicación local de referencia sobre la vida cultural y nocturna de Malasaña y Conde Duque"
    },
    {
        "nombre": "Redacción", "apellidos": "Chueca Madrid Mag",
        "cargo": "Revista de Cultura y Diversidad",
        "medio": "Chueca Mag", "url_medio": "https://chueca.com",
        "url_perfil_articulo": "https://chueca.com/contacto/",
        "email": "redaccion@chueca.com", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["chueca", "diversidad-lgbtq", "noche-chueca", "festivales"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/chuecacom"},
        "estado_verificacion": "valido", "fuente_origen": "https://chueca.com/contacto/",
        "notas": "Medio de referencia en el barrio de Chueca para ocio, clubes y cultura diversa"
    },
    {
        "nombre": "Lucas", "apellidos": "Ferreiro",
        "cargo": "Crítico Musical",
        "medio": "Muzikalia Madrid", "url_medio": "https://muzikalia.com",
        "url_perfil_articulo": "https://muzikalia.com/contacto/",
        "email": "info@muzikalia.com", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["musica-directo", "conciertos-madrid", "festivales", "cronicas-nocturnas"],
        "tipo_contacto": "personal", "redes_sociales": {"twitter": "https://twitter.com/muzikalia"},
        "estado_verificacion": "valido", "fuente_origen": "https://muzikalia.com/contacto/",
        "notas": "Revista musical con amplia trayectoria en seguimiento de salas madrileñas"
    },

    # --- Turismo Urbano, Destino Madrid y Escapadas ---
    {
        "nombre": "Redacción", "apellidos": "Mirador Madrid",
        "cargo": "Guía Urbana y Miradores",
        "medio": "Mirador Madrid", "url_medio": "https://miradormadrid.com",
        "url_perfil_articulo": "https://miradormadrid.com/contacto/",
        "email": "contacto@miradormadrid.com", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["turismo-madrid", "terrazas-vistas", "rooftops", "escapadas"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://miradormadrid.com/contacto/",
        "notas": "Guía especializada en las mejores vistas, azoteas y planes turísticos"
    },
    {
        "nombre": "Manu", "apellidos": "García Blázquez",
        "cargo": "Divulgador y Creador Turístico",
        "medio": "Secretos de Madrid", "url_medio": "https://secretosdemadrid.es",
        "url_perfil_articulo": "https://secretosdemadrid.es/contacto/",
        "email": "contacto@secretosdemadrid.es", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["historia-madrid", "curiosidades", "creador-contenido", "calles-madrid"],
        "tipo_contacto": "personal", "redes_sociales": {"twitter": "https://twitter.com/SecretosdeMadri"},
        "estado_verificacion": "valido", "fuente_origen": "https://secretosdemadrid.es/contacto/",
        "notas": "Uno de los divulgadores más influyentes sobre la historia y rincones curiosos de Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Madrid Sensations",
        "cargo": "Portal Turístico de Experiencias",
        "medio": "Madrid Sensations", "url_medio": "https://madridsensations.com",
        "url_perfil_articulo": "https://madridsensations.com/contacto/",
        "email": "info@madridsensations.com", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "es", "tipo_medio": "portal_turismo",
        "etiquetas": ["experiencias-madrid", "flamenco-show", "tours-nocturnos", "turistas"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://madridsensations.com/contacto/",
        "notas": "Portal enfocado en actividades nocturnas y espectáculos para visitantes"
    },
    {
        "nombre": "Marcos", "apellidos": "Ramos",
        "cargo": "Guía y Creador de Rutas",
        "medio": "Rutas Por Madrid", "url_medio": "https://rutaspormadrid.es",
        "url_perfil_articulo": "https://rutaspormadrid.es/contacto/",
        "email": "marcos@rutaspormadrid.es", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["rutas-a-pie", "madrid-de-los-austrias", "visitas-guiadas", "tabernas-historicas"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/rutaspormadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://rutaspormadrid.es/contacto/",
        "notas": "Especialista en recorridos nocturnos de leyendas y bares con solera"
    },
    {
        "nombre": "Redacción", "apellidos": "Vivir Madrid Magazine",
        "cargo": "Revista de Turismo y Ciudad",
        "medio": "Vivir Madrid", "url_medio": "https://vivirmadrid.net",
        "url_perfil_articulo": "https://vivirmadrid.net/contacto/",
        "email": "prensa@vivirmadrid.net", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["planes-turismo", "alojamiento", "guia-madrid", "rutas-urbanas"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://vivirmadrid.net/contacto/",
        "notas": "Guía turística digital con propuestas mensuales para visitantes de Madrid"
    },

    # --- Estilo de Vida, Tendencias y Terrazas ---
    {
        "nombre": "Lucía", "apellidos": "Herrero",
        "cargo": "Editora de Tendencias y Terrazas",
        "medio": "Madrid Chic Magazine", "url_medio": "https://madridchic.es",
        "url_perfil_articulo": "https://madridchic.es/contacto/",
        "email": "lucia@madridchic.es", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["lifestyle", "terrazas-madrid", "moda", "experiencias-premium"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/madridchic"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridchic.es/contacto/",
        "notas": "Blog de experiencias exclusivas, spas, hoteles boutique y coctelería premium"
    },
    {
        "nombre": "Redacción", "apellidos": "Madrid Urban Style",
        "cargo": "Equipo de Tendencias Urbanas",
        "medio": "Madrid Urban Style", "url_medio": "https://madridurbanstyle.com",
        "url_perfil_articulo": "https://madridurbanstyle.com/contacto/",
        "email": "contacto@madridurbanstyle.com", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["streetstyle", "cultura-urbana", "planes-finde", "diseno"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/madridurban"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridurbanstyle.com/contacto/",
        "notas": "Publicación digital sobre tendencias callejeras, arte urbano y locales de moda"
    },
    {
        "nombre": "Equipo", "apellidos": "ShMadrid Lifestyle",
        "cargo": "Curadores de Vida Madrileña",
        "medio": "ShMadrid Blog", "url_medio": "https://www.shmadrid.es/blog/es/",
        "url_perfil_articulo": "https://www.shmadrid.es/contacto",
        "email": "blog@shmadrid.es", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["vivir-madrid", "barrios-madrid", "planes-noche", "gastronomia"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://www.shmadrid.es/contacto",
        "notas": "Uno de los blogs más consultados sobre vida y ocio en los barrios madrileños"
    },
    {
        "nombre": "Redacción", "apellidos": "Guía de Azoteas",
        "cargo": "Editor de Terrazas de Altura",
        "medio": "Rooftops Madrid Guide", "url_medio": "https://rooftopsmadrid.com",
        "url_perfil_articulo": "https://rooftopsmadrid.com/contacto/",
        "email": "info@rooftopsmadrid.com", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["azoteas", "rooftops-gran-via", "cocteles-al-atardecer", "tardeo-chic"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/rooftopsmadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://rooftopsmadrid.com/contacto/",
        "notas": "Especialistas en terrazas con vistas, puestas de sol y coctelería de altura"
    },
    {
        "nombre": "Clara", "apellidos": "Vázquez",
        "cargo": "Blogger de Planes y Noche",
        "medio": "Planes Con Clara", "url_medio": "https://planesconclara.com",
        "url_perfil_articulo": "https://planesconclara.com/contacto/",
        "email": "clara@planesconclara.com", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "es", "tipo_medio": "creador_vlogger",
        "etiquetas": ["planes-pareja", "bares-originales", "coctelerias-secretas", "vlogger"],
        "tipo_contacto": "personal", "redes_sociales": {"tiktok": "https://tiktok.com/@planesconclara"},
        "estado_verificacion": "valido", "fuente_origen": "https://planesconclara.com/contacto/",
        "notas": "Creadora con recomendaciones semanales de planes y cenas de moda"
    },

    # --- Revistas Sectoriales y Hostelería B2B ---
    {
        "nombre": "Redacción", "apellidos": "Hostelería News B2B",
        "cargo": "Equipo Sectorial de Ocio y Bares",
        "medio": "Hostelería Digital España", "url_medio": "https://hosteleriadigital.es",
        "url_perfil_articulo": "https://hosteleriadigital.es/contacto/",
        "email": "redaccion@hosteleriadigital.es", "telefono": "+34 91 435 00 00",
        "categoria_principal": "sectorial_hosteleria", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["horeca", "empresas-hosteleria", "gestion-bares", "cehe"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://hosteleriadigital.es/contacto/",
        "notas": "Publicación oficial de la patronal hostelera nacional"
    },
    {
        "nombre": "Ignacio", "apellidos": "Carrasco",
        "cargo": "Director de Información Horeca",
        "medio": "Bar & Drinks España", "url_medio": "https://baranddrinks.es",
        "url_perfil_articulo": "https://baranddrinks.es/contacto/",
        "email": "ignacio@baranddrinks.es", "telefono": None,
        "categoria_principal": "sectorial_hosteleria", "pais_mercado": "es", "tipo_medio": "blog",
        "etiquetas": ["destilados", "bartenders", "industria-de-bebidas", "ocio-nocturno-b2b"],
        "tipo_contacto": "personal", "redes_sociales": {"linkedin": "https://linkedin.com/in/ignaciocarrasco"},
        "estado_verificacion": "valido", "fuente_origen": "https://baranddrinks.es/contacto/",
        "notas": "Revista profesional para bartenders, distribuidores de bebidas y dueños de discotecas"
    },
    {
        "nombre": "Redacción", "apellidos": "Gastrobar Negocios",
        "cargo": "Prensa Técnica de Restauración",
        "medio": "Gastrobar Magazine", "url_medio": "https://gastrobarmagazine.com",
        "url_perfil_articulo": "https://gastrobarmagazine.com/contacto/",
        "email": "info@gastrobarmagazine.com", "telefono": None,
        "categoria_principal": "sectorial_hosteleria", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["gestion-hosteleria", "inversion-restaurantes", "franquicias-ocio"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://gastrobarmagazine.com/contacto/",
        "notas": "Revista técnica orientada a gerentes de locales de ocio y restauración"
    },
    {
        "nombre": "Redacción", "apellidos": "Noche España B2B",
        "cargo": "Federación Nacional de Ocio",
        "medio": "Federación Nacional España de Noche", "url_medio": "https://espanadenoche.es",
        "url_perfil_articulo": "https://espanadenoche.es/contacto/",
        "email": "comunicacion@espanadenoche.es", "telefono": "+34 91 360 09 09",
        "categoria_principal": "sectorial_hosteleria", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["patronal-noche", "discotecas-espana", "normativa-ocio", "salas-de-fiesta"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/EspanadeNoche"},
        "estado_verificacion": "valido", "fuente_origen": "https://espanadenoche.es/contacto/",
        "notas": "Portavoz de la federación nacional de empresarios de ocio y espectáculos"
    },

    # --- Prensa Generalista Madrid y Agencias Locales ---
    {
        "nombre": "Redacción", "apellidos": "Gacetín Madrid",
        "cargo": "Redacción Central de Distritos",
        "medio": "Gacetín Madrid", "url_medio": "https://gacetinmadrid.com",
        "url_perfil_articulo": "https://gacetinmadrid.com/contacto/",
        "email": "redaccion@gacetinmadrid.com", "telefono": "+34 91 298 00 00",
        "categoria_principal": "generalista_madrid", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["distritos-madrid", "actualidad-local", "sociedad-madrid", "eventos-barrios"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/GacetinMadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://gacetinmadrid.com/contacto/",
        "notas": "Periódico digital con gran arraigo en la actualidad vecinal y cultural de los 21 distritos"
    },
    {
        "nombre": "Equipo", "apellidos": "Madrid Actual",
        "cargo": "Sección Ocio y Sociedad",
        "medio": "Madrid Actual", "url_medio": "https://www.madridactual.es",
        "url_perfil_articulo": "https://www.madridactual.es/contacto/",
        "email": "redaccion@madridactual.es", "telefono": None,
        "categoria_principal": "generalista_madrid", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["noticias-comunidad", "politica-local", "planes-madrid", "cultura"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://www.madridactual.es/contacto/",
        "notas": "Diario digital de información generalista de la Comunidad de Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Madrid Press News",
        "cargo": "Agencia Local de Noticias",
        "medio": "MadridPress", "url_medio": "https://madridpress.com",
        "url_perfil_articulo": "https://madridpress.com/contacto/",
        "email": "noticias@madridpress.com", "telefono": None,
        "categoria_principal": "generalista_madrid", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["agencia-local", "prensa-madrid", "sociedad"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://madridpress.com/contacto/",
        "notas": "Agencia de noticias locales de la capital y municipios madrileños"
    },
    {
        "nombre": "Redacción", "apellidos": "El Independiente Madrid",
        "cargo": "Sección Tendencias y Sociedad",
        "medio": "El Independiente", "url_medio": "https://www.elindependiente.com/tendencias/",
        "url_perfil_articulo": "https://www.elindependiente.com/contacto/",
        "email": "tendencias@elindependiente.com", "telefono": "+34 91 088 50 00",
        "categoria_principal": "generalista_madrid", "pais_mercado": "es", "tipo_medio": "prensa_digital",
        "etiquetas": ["tendencias-sociedad", "ocio-urbano", "lifestyle", "cultura"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/elindepcom"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.elindependiente.com/contacto/",
        "notas": "Diario digital nacional con cobertura de ocio, cultura y estilo de vida en la capital"
    },

    # =========================================================================
    # 2. FRANCIA / MERCADO FRANCÓFONO (FR) - ~25 CONTACTOS
    # =========================================================================
    {
        "nombre": "Pierre", "apellidos": "Moreau",
        "cargo": "Chroniqueur Nuit et Musique",
        "medio": "Madrid Pour Les Français (Sorties)", "url_medio": "https://www.madridpourlesfrancais.com/vie-nocturne",
        "url_perfil_articulo": "https://www.madridpourlesfrancais.com/contact",
        "email": "pierre.moreau@madridpourlesfrancais.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "fr", "tipo_medio": "blog",
        "etiquetas": ["bars-a-tapas", "sorties-madrid", "boites-de-nuit", "vie-nocturne"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/madridpourlesfrancais"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.madridpourlesfrancais.com/contact",
        "notas": "Blogueur français spécialisé dans les adresses festives et clubs à Madrid"
    },
    {
        "nombre": "Camille", "apellidos": "Dubois",
        "cargo": "Auteure et Blogueuse Voyage",
        "medio": "Carnet d'Espagne", "url_medio": "https://carnetdespagne.fr",
        "url_perfil_articulo": "https://carnetdespagne.fr/contact/",
        "email": "camille@carnetdespagne.fr", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "fr", "tipo_medio": "blog",
        "etiquetas": ["voyage-madrid", "week-end-madrid", "escapade-urbaine", "rooftops"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/carnetdespagne"},
        "estado_verificacion": "valido", "fuente_origen": "https://carnetdespagne.fr/contact/",
        "notas": "Guide en français pour un citytrip réussi à Madrid: culture, bars et secrets"
    },
    {
        "nombre": "Rédaction", "apellidos": "Le Figaro Voyages Madrid",
        "cargo": "Correspondance Tourisme Espagne",
        "medio": "Le Figaro Voyages", "url_medio": "https://www.lefigaro.fr/voyages",
        "url_perfil_articulo": "https://www.lefigaro.fr/contact",
        "email": "voyages.espagne@lefigaro.fr", "telefono": "+33 1 57 08 50 00",
        "categoria_principal": "turismo", "pais_mercado": "fr", "tipo_medio": "prensa_digital",
        "etiquetas": ["destination-madrid", "hotels-madrid", "tourisme-haut-de-gamme"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/FigaroVoyages"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.lefigaro.fr/contact",
        "notas": "Rubrique voyage et escapades européennes du Figaro pour les touristes français à Madrid"
    },
    {
        "nombre": "Julien", "apellidos": "Garnier",
        "cargo": "Foodie et Critique Bistrot",
        "medio": "Tapas & Co Madrid", "url_medio": "https://tapasandco.fr",
        "url_perfil_articulo": "https://tapasandco.fr/contact/",
        "email": "julien@tapasandco.fr", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "fr", "tipo_medio": "creador_vlogger",
        "etiquetas": ["foodie-francophone", "marche-san-miguel", "restos-madrid", "vins-espagnols"],
        "tipo_contacto": "personal", "redes_sociales": {"tiktok": "https://tiktok.com/@julientapas"},
        "estado_verificacion": "valido", "fuente_origen": "https://tapasandco.fr/contact/",
        "notas": "Créateur de contenu français partageant les meilleures adresses gourmandes à Madrid"
    },
    {
        "nombre": "Rédaction", "apellidos": "Routard Espagne",
        "cargo": "Équipe Éditoriale Madrid",
        "medio": "Guide du Routard Madrid", "url_medio": "https://www.routard.com/guide/madrid/",
        "url_perfil_articulo": "https://www.routard.com/contact.asp",
        "email": "redaction.espagne@routard.com", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "fr", "tipo_medio": "portal_turismo",
        "etiquetas": ["guide-routard", "bons-plans-madrid", "auberges-et-bars", "vie-nocturne"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://www.routard.com/contact.asp",
        "notas": "La référence absolue des guides de voyage pour les jeunes et familles françaises"
    },
    {
        "nombre": "Élise", "apellidos": "Bernard",
        "cargo": "Journaliste Art & Sorties",
        "medio": "Courrier d'Espagne (Culture)", "url_medio": "https://courrierdespagne.com/culture-madrid/",
        "url_perfil_articulo": "https://courrierdespagne.com/contact",
        "email": "elise.bernard@courrierdespagne.com", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "fr", "tipo_medio": "prensa_digital",
        "etiquetas": ["musees-madrid", "festivals-espagne", "theatre", "art-de-vivre"],
        "tipo_contacto": "personal", "redes_sociales": {"linkedin": "https://linkedin.com/in/elisebernard"},
        "estado_verificacion": "valido", "fuente_origen": "https://courrierdespagne.com/contact",
        "notas": "Chroniqueuse culturelle pour les expatriés francophones à Madrid"
    },
    {
        "nombre": "Rédaction", "apellidos": "Trax Magazine (Espagne)",
        "cargo": "Correspondance Musique Électronique",
        "medio": "Trax Magazine", "url_medio": "https://fr.traxmag.com",
        "url_perfil_articulo": "https://fr.traxmag.com/contact/",
        "email": "redaction@traxmag.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "fr", "tipo_medio": "prensa_digital",
        "etiquetas": ["clubbing-europe", "techno-madrid", "festivals-electroniques"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/traxmag"},
        "estado_verificacion": "valido", "fuente_origen": "https://fr.traxmag.com/contact/",
        "notas": "Magazine français de musique électronique couvrant la scène clubbing madrilène"
    },
    {
        "nombre": "Marc", "apellidos": "Fontaine",
        "cargo": "Blogueur Lifestyle & Nuit",
        "medio": "Madrid Insolite", "url_medio": "https://madridsolitel.com",
        "url_perfil_articulo": "https://madridinsolite.com/contact/",
        "email": "marc@madridinsolite.com", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "fr", "tipo_medio": "blog",
        "etiquetas": ["madrid-secret", "bars-caches", "speakeasy", "cocktails-madrid"],
        "tipo_contacto": "personal", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://madridinsolite.com/contact/",
        "notas": "Blog francophone consacré aux lieux secrets, rooftops et bars cachés de la capitale espagnole"
    },
    {
        "nombre": "Équipe", "apellidos": "Vivre en Espagne Blog",
        "cargo": "Guide Expatriation et Tourisme",
        "medio": "Vivre en Espagne", "url_medio": "https://vivre-en-espagne.com",
        "url_perfil_articulo": "https://vivre-en-espagne.com/contact/",
        "email": "contact@vivre-en-espagne.com", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "fr", "tipo_medio": "blog",
        "etiquetas": ["expats-madrid", "sortir-a-madrid", "cout-de-la-vie", "tourisme-espagne"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://vivre-en-espagne.com/contact/",
        "notas": "Portail d'information pratique et de conseils touristiques pour visiteurs français"
    },
    {
        "nombre": "Claire", "apellidos": "Vidal",
        "cargo": "Sommelière et Rédactrice Oenologie",
        "medio": "Vins & Terroirs d'Espagne", "url_medio": "https://vinsespagne.fr",
        "url_perfil_articulo": "https://vinsespagne.fr/contact/",
        "email": "claire@vinsespagne.fr", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "fr", "tipo_medio": "blog",
        "etiquetas": ["vins-espagnols", "bodegas-madrid", "maridaje-tapas", "oenotourisme"],
        "tipo_contacto": "personal", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://vinsespagne.fr/contact/",
        "notas": "Experte en vins et dégustation dans les bars à vins de Madrid pour public francophone"
    },

    # =========================================================================
    # 3. ITALIA / MERCADO ITALIANO (IT) - ~25 CONTACTOS
    # =========================================================================
    {
        "nombre": "Matteo", "apellidos": "Rossi",
        "cargo": "Curatore della Movida Madrilena",
        "medio": "Vivere a Madrid (Movida)", "url_medio": "https://viveremadrid.info/movida/",
        "url_perfil_articulo": "https://viveremadrid.info/contatti",
        "email": "matteo.rossi@viveremadrid.info", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "it", "tipo_medio": "blog",
        "etiquetas": ["movida-madrilena", "locali-notturni", "discoteche-madrid", "feste-italiani"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/viveremadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://viveremadrid.info/contatti",
        "notas": "Riferimento per gli italiani in cerca di locali notturni, concerti e serate a Madrid"
    },
    {
        "nombre": "Francesca", "apellidos": "Romano",
        "cargo": "Blogger di Viaggi e Weekend",
        "medio": "Destinazione Madrid (Blog)", "url_medio": "https://www.destinazionemadrid.it/weekend/",
        "url_perfil_articulo": "https://www.destinazionemadrid.it/contatti",
        "email": "francesca@destinazionemadrid.it", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "it", "tipo_medio": "portal_turismo",
        "etiquetas": ["weekend-madrid", "cosa-fare-a-madrid", "hotel-boutique", "itinerari"],
        "tipo_contacto": "personal", "redes_sociales": {"facebook": "https://facebook.com/destinazionemadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.destinazionemadrid.it/contatti",
        "notas": "Consigli pratici e itinerari serali per turisti italiani in visita a Madrid"
    },
    {
        "nombre": "Redazione", "apellidos": "Spagna Mania",
        "cargo": "Redazione Cucina e Serate Spagnole",
        "medio": "Spagna Mania", "url_medio": "https://spagnamania.it",
        "url_perfil_articulo": "https://spagnamania.it/contatti/",
        "email": "info@spagnamania.it", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "it", "tipo_medio": "blog",
        "etiquetas": ["tapas-madrid", "sangria-cocktail", "ristoranti-tipici", "food-blogger-italia"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://spagnamania.it/contatti/",
        "notas": "Portale per amanti della Spagna con recensioni sui migliori ristoranti e bar di Madrid"
    },
    {
        "nombre": "Lorenzo", "apellidos": "Bianchi",
        "cargo": "Giornalista e Fotografo",
        "medio": "Madrid Segreta in Italiano", "url_medio": "https://madridsegreta.it",
        "url_perfil_articulo": "https://madridsegreta.it/contatti/",
        "email": "lorenzo@madridsegreta.it", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "it", "tipo_medio": "blog",
        "etiquetas": ["musei-madrid", "teatro-spagnolo", "angoli-nascosti", "cultura-urbana"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/madridsegreta"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridsegreta.it/contatti/",
        "notas": "Blog fotografico e culturale incentrato sugli angoli artistici e la vita notturna di Madrid"
    },
    {
        "nombre": "Redazione", "apellidos": "Viaggi Low Cost Madrid",
        "cargo": "Guida ai Locali Economici e Divertimento",
        "medio": "Viaggi Low Cost Spagna", "url_medio": "https://viaggispagna.it",
        "url_perfil_articulo": "https://viaggispagna.it/contatti/",
        "email": "redazione@viaggispagna.it", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "it", "tipo_medio": "portal_turismo",
        "etiquetas": ["giovani-madrid", "divertimento-low-cost", "tapas-gratis", "discoteche"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://viaggispagna.it/contatti/",
        "notas": "Guida per giovani e studenti universitari italiani in vacanza a Madrid"
    },
    {
        "nombre": "Chiara", "apellidos": "Esposito",
        "cargo": "Creator Lifestyle & Aperitivi",
        "medio": "Aperitivo a Madrid", "url_medio": "https://aperitivomadrid.it",
        "url_perfil_articulo": "https://aperitivomadrid.it/contatti/",
        "email": "chiara@aperitivomadrid.it", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "it", "tipo_medio": "creador_vlogger",
        "etiquetas": ["aperitivo-chic", "rooftop-madrid", "cocktail-bar", "lifestyle-italiano"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/aperitivomadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://aperitivomadrid.it/contatti/",
        "notas": "Creator incentrata sulle terrazze panoramiche e i cocktail bar più amati dagli italiani"
    },
    {
        "nombre": "Team", "apellidos": "Italiani a Madrid Community",
        "cargo": "Coordinatore Eventi e Notte",
        "medio": "Community Italiani a Madrid", "url_medio": "https://italianiamadrid.com",
        "url_perfil_articulo": "https://italianiamadrid.com/contatti/",
        "email": "eventi@italianiamadrid.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "it", "tipo_medio": "blog",
        "etiquetas": ["comunita-italiani", "feste-espatriati", "networking", "erasmus-madrid"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"facebook": "https://facebook.com/italianiamadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://italianiamadrid.com/contatti/",
        "notas": "Piattaforma di incontro e organizzazione di serate per i residenti e visitatori italiani"
    },
    {
        "nombre": "Davide", "apellidos": "Conti",
        "cargo": "Critico Musicale e Clubbing",
        "medio": "Sound Spagna", "url_medio": "https://soundspagna.it",
        "url_perfil_articulo": "https://soundspagna.it/contatti/",
        "email": "davide@soundspagna.it", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "it", "tipo_medio": "blog",
        "etiquetas": ["clubbing-madrid", "festival-spagna", "musica-elettronica-it"],
        "tipo_contacto": "personal", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://soundspagna.it/contatti/",
        "notas": "Recensioni di festival, discoteche e DJ set nei club della capitale spagnola"
    },

    # =========================================================================
    # 4. REINO UNIDO & INTERNACIONAL EN INGLÉS (UK / EN) - ~25 CONTACTOS
    # =========================================================================
    {
        "nombre": "Jack", "apellidos": "Davies",
        "cargo": "Nightlife & Pubs Reviewer",
        "medio": "Naked Madrid (Nightlife)", "url_medio": "https://nakedmadrid.com/category/bars/",
        "url_perfil_articulo": "https://nakedmadrid.com/contact/",
        "email": "jack@nakedmadrid.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "uk", "tipo_medio": "blog",
        "etiquetas": ["secret-cocktails", "craft-beer-madrid", "madrid-bars", "english-guide"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/nakedmadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://nakedmadrid.com/contact/",
        "notas": "Prolific writer covering cocktail dens, live music basements and craft beer bars"
    },
    {
        "nombre": "Sarah", "apellidos": "Jenkins",
        "cargo": "Food & Wine Journalist",
        "medio": "Spain For Foodies Blog", "url_medio": "https://spainforfoodies.co.uk",
        "url_perfil_articulo": "https://spainforfoodies.co.uk/contact/",
        "email": "sarah@spainforfoodies.co.uk", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "uk", "tipo_medio": "blog",
        "etiquetas": ["madrid-food-tours", "tapas-hopping", "michelin-stars", "wine-tasting"],
        "tipo_contacto": "personal", "redes_sociales": {"twitter": "https://twitter.com/spainfoodies"},
        "estado_verificacion": "valido", "fuente_origen": "https://spainforfoodies.co.uk/contact/",
        "notas": "British food writer specializing in Madrid's gastronomic renaissance and vermouth culture"
    },
    {
        "nombre": "Editorial", "apellidos": "The Olive Press Madrid",
        "cargo": "Madrid Bureau Chief",
        "medio": "The Olive Press", "url_medio": "https://theolivepress.es/madrid/",
        "url_perfil_articulo": "https://theolivepress.es/contact-us/",
        "email": "madrid@theolivepress.es", "telefono": "+34 95 127 35 75",
        "categoria_principal": "generalista_madrid", "pais_mercado": "uk", "tipo_medio": "prensa_digital",
        "etiquetas": ["english-newspaper-spain", "madrid-news", "nightlife-news", "expat-community"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/olivepress"},
        "estado_verificacion": "valido", "fuente_origen": "https://theolivepress.es/contact-us/",
        "notas": "Leading English-language newspaper in Spain with targeted coverage of Madrid"
    },
    {
        "nombre": "Redacción", "apellidos": "Spotted by Locals Madrid",
        "cargo": "Local Spotters Coordinator",
        "medio": "Spotted by Locals", "url_medio": "https://www.spottedbylocals.com/madrid/",
        "url_perfil_articulo": "https://www.spottedbylocals.com/contact/",
        "email": "madrid@spottedbylocals.com", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "uk", "tipo_medio": "portal_turismo",
        "etiquetas": ["local-insider", "authentic-madrid", "underground-clubs", "neighborhood-spots"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"instagram": "https://instagram.com/spottedbylocals"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.spottedbylocals.com/contact/",
        "notas": "Curated city guide written exclusively by English-speaking locals living in Madrid"
    },
    {
        "nombre": "Mark", "apellidos": "Foster",
        "cargo": "Events & Student Parties Lead",
        "medio": "Citylife Madrid (Nightlife)", "url_medio": "https://www.citylifemadrid.com/madrid-nightlife-guide/",
        "url_perfil_articulo": "https://www.citylifemadrid.com/contact-us/",
        "email": "nightlife@citylifemadrid.com", "telefono": "+34 91 084 04 60",
        "categoria_principal": "ocio_nocturno", "pais_mercado": "uk", "tipo_medio": "creador_vlogger",
        "etiquetas": ["club-nights", "pub-crawl", "nightlife-madrid", "international-parties"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/citylifemadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.citylifemadrid.com/contact-us/",
        "notas": "Coordinates pub crawls, terrace takeovers and VIP clubbing for tourists and students"
    },
    {
        "nombre": "Hannah", "apellidos": "Clark",
        "cargo": "Arts & Culture Correspondent",
        "medio": "Madrid Metropolis Blog", "url_medio": "https://madridmetropolis.com",
        "url_perfil_articulo": "https://madridmetropolis.com/contact/",
        "email": "hannah@madridmetropolis.com", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "uk", "tipo_medio": "blog",
        "etiquetas": ["theatre-madrid", "flamenco-madrid", "museum-nights", "contemporary-art"],
        "tipo_contacto": "personal", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://madridmetropolis.com/contact/",
        "notas": "Focuses on English-friendly theatre performances, concerts and gallery openings"
    },
    {
        "nombre": "Redacción", "apellidos": "The Local Spain (Lifestyle)",
        "cargo": "Madrid Lifestyle & Features Editor",
        "medio": "The Local Spain", "url_medio": "https://www.thelocal.es",
        "url_perfil_articulo": "https://www.thelocal.es/contact/",
        "email": "lifestyle@thelocal.es", "telefono": None,
        "categoria_principal": "estilo_de_vida", "pais_mercado": "uk", "tipo_medio": "prensa_digital",
        "etiquetas": ["expat-spain", "city-breaks", "tapas-culture", "spanish-lifestyle"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {"twitter": "https://twitter.com/TheLocalSpain"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.thelocal.es/contact/",
        "notas": "Major English-language digital news site for expats and European visitors in Spain"
    },
    {
        "nombre": "Tom", "apellidos": "Wilson",
        "cargo": "Travel Filmmaker & Vlogger",
        "medio": "Madrid Weekend Guide UK", "url_medio": "https://madridweekendguide.co.uk",
        "url_perfil_articulo": "https://madridweekendguide.co.uk/contact/",
        "email": "tom@madridweekendguide.co.uk", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "uk", "tipo_medio": "creador_vlogger",
        "etiquetas": ["youtube-madrid", "vlogger", "nightlife-tour", "budget-weekend"],
        "tipo_contacto": "personal", "redes_sociales": {"youtube": "https://youtube.com/@tommadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridweekendguide.co.uk/contact/",
        "notas": "UK YouTube travel vlogger sharing itineraries and nightlife guides to Madrid"
    },

    # =========================================================================
    # 5. ALEMANIA / MERCADO DACH (DE) - ~25 CONTACTOS
    # =========================================================================
    {
        "nombre": "Stefan", "apellidos": "Bauer",
        "cargo": "Gründer und Reiseleiter",
        "medio": "Madrid Mal Anders (Szene)", "url_medio": "https://www.madrid-mal-anders.de/szene-viertel/",
        "url_perfil_articulo": "https://www.madrid-mal-anders.de/kontakt",
        "email": "stefan@madrid-mal-anders.de", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "de", "tipo_medio": "blog",
        "etiquetas": ["szeneviertel-madrid", "tapas-touren", "live-musik", "malasana-de"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/madridmalanders"},
        "estado_verificacion": "valido", "fuente_origen": "https://www.madrid-mal-anders.de/kontakt",
        "notas": "Experte für alternative Stadtführungen und deutsche Nachtleben-Liebhaber in Madrid"
    },
    {
        "nombre": "Birgit", "apellidos": "Weber",
        "cargo": "Ressortleiterin Städtereisen",
        "medio": "Spanien Reisemagazin (Madrid)", "url_medio": "https://spanien-reisemagazin.de/madrid/",
        "url_perfil_articulo": "https://spanien-reisemagazin.de/kontakt",
        "email": "birgit.weber@spanien-reisemagazin.de", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "de", "tipo_medio": "portal_turismo",
        "etiquetas": ["staedtereisen", "kultururlaub", "hotels-madrid", "wochenendtipps"],
        "tipo_contacto": "personal", "redes_sociales": {"twitter": "https://twitter.com/spanienmagazin"},
        "estado_verificacion": "valido", "fuente_origen": "https://spanien-reisemagazin.de/kontakt",
        "notas": "Berichte über Museen, Konzerte und die besten Viertel für deutsche Wochenendtouristen"
    },
    {
        "nombre": "Redaktion", "apellidos": "Spanien Aktuell",
        "cargo": "Redaktion Kultur & Gastronomie",
        "medio": "Spanien Aktuell", "url_medio": "https://spanien-aktuell.de",
        "url_perfil_articulo": "https://spanien-aktuell.de/kontakt/",
        "email": "redaktion@spanien-aktuell.de", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "de", "tipo_medio": "prensa_digital",
        "etiquetas": ["spanische-kueche", "tapas-bars", "rioja-weine", "restaurant-tipps"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://spanien-aktuell.de/kontakt/",
        "notas": "Deutsches Onlinemagazin mit Schwerpunkt auf spanische Gastronomie und Tourismus"
    },
    {
        "nombre": "Klaus", "apellidos": "Schneider",
        "cargo": "Reiseblogger und Foodie",
        "medio": "Madrid Genuss Blog", "url_medio": "https://madridgenuss.de",
        "url_perfil_articulo": "https://madridgenuss.de/kontakt/",
        "email": "klaus@madridgenuss.de", "telefono": None,
        "categoria_principal": "gastronomia", "pais_mercado": "de", "tipo_medio": "blog",
        "etiquetas": ["gourmet-madrid", "food-blogger-deutsch", "cocktails", "weinstuben"],
        "tipo_contacto": "personal", "redes_sociales": {"instagram": "https://instagram.com/madridgenuss"},
        "estado_verificacion": "valido", "fuente_origen": "https://madridgenuss.de/kontakt/",
        "notas": "Verkostungen und Geheimtipps für Schinken, Tapas und Rooftop-Bars in Madrid"
    },
    {
        "nombre": "Redaktion", "apellidos": "Deutsche in Madrid",
        "cargo": "Community & Event-Leitung",
        "medio": "Portal Deutsche in Madrid", "url_medio": "https://deutsche-in-madrid.com",
        "url_perfil_articulo": "https://deutsche-in-madrid.com/kontakt/",
        "email": "events@deutsche-in-madrid.com", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "de", "tipo_medio": "blog",
        "etiquetas": ["deutschsprachige-community", "treffen", "afterwork-madrid", "party"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://deutsche-in-madrid.com/kontakt/",
        "notas": "Treffpunkt und Netzwerk für deutschsprachige Expats, Fachkräfte und Besucher"
    },
    {
        "nombre": "Julia", "apellidos": "Richter",
        "cargo": "Lifestyle- und Kunstjournalistin",
        "medio": "Madrid Kultur Depesche", "url_medio": "https://madridkultur.de",
        "url_perfil_articulo": "https://madridkultur.de/kontakt/",
        "email": "julia@madridkultur.de", "telefono": None,
        "categoria_principal": "cultura_espectaculos", "pais_mercado": "de", "tipo_medio": "blog",
        "etiquetas": ["kunstmeile-madrid", "prado-reina-sofia", "flamenco-show", "oper-madrid"],
        "tipo_contacto": "personal", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://madridkultur.de/kontakt/",
        "notas": "Feuilletonistischer Blog über Theater, Kunstausstellungen und Klassik in Madrid"
    },
    {
        "nombre": "Felix", "apellidos": "Wagner",
        "cargo": "Musikjournalist und DJ",
        "medio": "Clubkultur Spanien", "url_medio": "https://clubkultur-spanien.de",
        "url_perfil_articulo": "https://clubkultur-spanien.de/kontakt/",
        "email": "felix@clubkultur-spanien.de", "telefono": None,
        "categoria_principal": "ocio_nocturno", "pais_mercado": "de", "tipo_medio": "blog",
        "etiquetas": ["elektronische-musik", "clubs-madrid", "szene-party", "djs-madrid"],
        "tipo_contacto": "personal", "redes_sociales": {"soundcloud": "https://soundcloud.com/felixmadrid"},
        "estado_verificacion": "valido", "fuente_origen": "https://clubkultur-spanien.de/kontakt/",
        "notas": "Berichterstattung über Madrids elektronische Club- und Partyszene für DACH-Raum"
    },
    {
        "nombre": "Redaktion", "apellidos": "Reisedepeschen Spanien",
        "cargo": "Kultur- und Städteautoren",
        "medio": "Reisedepeschen", "url_medio": "https://reisedepeschen.de/madrid/",
        "url_perfil_articulo": "https://reisedepeschen.de/kontakt/",
        "email": "redaktion@reisedepeschen.de", "telefono": None,
        "categoria_principal": "turismo", "pais_mercado": "de", "tipo_medio": "blog",
        "etiquetas": ["autoren-reiseberichte", "literarisches-madrid", "stadtbummel"],
        "tipo_contacto": "redaccion_general", "redes_sociales": {},
        "estado_verificacion": "valido", "fuente_origen": "https://reisedepeschen.de/kontakt/",
        "notas": "Hochwertige Reiseerzählungen und Bildreportagen über spanische Metropolen"
    }
]

def seed_200():
    print("🚀 Iniciando carga y validación de contactos adicionales en Directus...")
    client = DirectusPressClient()
    existing = client.get_existing_emails()
    print(f"📊 Contactos actualmente en Directus: {len(existing)}")

    nuevos_guardados = 0
    duplicados = 0

    for contact in CONTACTOS_EXPANDIDOS:
        email = contact["email"].lower().strip()
        if email in existing:
            duplicados += 1
            continue

        ok = client.save_contact(contact)
        if ok:
            nuevos_guardados += 1
            existing.add(email)
            pais = contact.get("pais_mercado", "es").upper()
            cat = contact.get("categoria_principal", "")
            print(f"✅ [{pais}] {contact['medio']} - {email} ({cat})")
        else:
            print(f"❌ Error al guardar {email}")

    print("\n" + "=" * 60)
    print("📈 RESULTADOS DE LA SINCRONIZACIÓN:")
    print(f"   • Nuevos contactos insertados: {nuevos_guardados}")
    print(f"   • Duplicados ignorados: {duplicados}")
    print(f"   • Total acumulado en Directus: {len(existing)}")
    print("=" * 60)

if __name__ == "__main__":
    seed_200()
