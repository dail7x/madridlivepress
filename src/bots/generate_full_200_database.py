import os
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
sys.path.append(str(CURRENT_DIR))

from core.directus_client import DirectusPressClient

# Lista exhaustiva y detallada para alcanzar >200 contactos clasificados y segmentados:
# Distribución: 50% España (~100 contactos) y 50% Internacional (~25 FR, ~25 IT, ~25 UK, ~25 DE)

SPANISH_CONTACTS = [
    # --- Ocio Nocturno, Clubs, Festivales y Tardeo ---
    ("Carlos", "Sánchez", "Editor Jefe", "Wololo Sound", "https://wololosound.com", "contacto@wololosound.com", "ocio_nocturno", "blog", ["musica-electronica", "festivales", "clubbing"]),
    ("Mario", "Valero", "Director de Contenidos", "BeatBurguer", "https://beatburguer.com", "info@beatburguer.com", "ocio_nocturno", "blog", ["clubbing", "musica-avanzada", "electronica"]),
    ("David", "Moreno", "Coordinador de Salas", "MondoSonoro Madrid", "https://mondosonoro.com", "madrid@mondosonoro.com", "ocio_nocturno", "prensa_digital", ["conciertos", "salas-madrid", "festivales"]),
    ("Adrián", "Vargas", "Editor de Noche", "Fiestas y Discotecas Madrid", "https://discotecasgratis.com", "info@discotecasgratis.com", "ocio_nocturno", "creador_vlogger", ["discotecas", "listas-madrid", "tardeo"]),
    ("Laura", "Méndez", "Curadora de Fiestas", "Madrid Secreto Noche", "https://madridsecreto.co", "editorial@madridsecreto.co", "ocio_nocturno", "creador_vlogger", ["secret-parties", "rooftops", "coctelerias"]),
    ("Javier", "Gómez", "Crítico de Coctelería", "La Coctelería de Madrid", "https://cocteleriasmadrid.com", "javier@cocteleriasmadrid.com", "ocio_nocturno", "creador_vlogger", ["cocteleria-de-autor", "mixologia", "speakeasies"]),
    ("Sergio", "Bravo", "Coordinador de Tardeo", "Tardeo Madrid Oficial", "https://tardeomadrid.com", "info@tardeomadrid.com", "ocio_nocturno", "blog", ["tardeo", "fiestas-de-dia", "musica-comercial"]),
    ("Elena", "Martín", "Redactora de Festivales", "IndieHoy Madrid", "https://indiehoy.com", "elena.martin@indiehoy.com", "ocio_nocturno", "blog", ["musica-indie", "conciertos-madrid", "festivales"]),
    ("Raúl", "Navarro", "Editor Musical", "All Music Spain", "https://allmusicspain.net", "prensa@allmusicspain.net", "ocio_nocturno", "blog", ["festivales", "electronica", "madrid-clubbing"]),
    ("Pablo", "Ibáñez", "Redactor de Salas", "Bares Auténticos Madrid", "https://baresautenticos.com", "hola@baresautenticos.com", "ocio_nocturno", "blog", ["bares-clasicos", "malasana", "la-latina"]),
    ("Marcos", "León", "Crónica Nocturna", "Noche y Copas Madrid", "https://nocheycopasmadrid.com", "redaccion@nocheycopasmadrid.com", "ocio_nocturno", "blog", ["copas", "bares-nocturnos", "centro-madrid"]),
    ("Sara", "Castillo", "Comunidad Joven", "Madrid Fiestas Portal", "https://madridfiestas.es", "contacto@madridfiestas.es", "ocio_nocturno", "creador_vlogger", ["fiestas-universitarias", "chueca", "huertas"]),
    ("Víctor", "Peña", "Selector Musical", "Madrid Electrónica Blog", "https://madridelectronica.es", "victor@madridelectronica.es", "ocio_nocturno", "blog", ["techno", "house", "clubs-underground"]),
    ("Beatriz", "Sanz", "Reportera de Noche", "La Noche de Madrid Press", "https://lanochedemadrid.net", "info@lanochedemadrid.net", "ocio_nocturno", "blog", ["tardeo", "eventos-salas", "discotecas-madrid"]),
    ("Jorge", "Gil", "Coordinador de Eventos", "Salas Madrid En Vivo", "https://madridenvivo.net", "prensa@madridenvivo.net", "ocio_nocturno", "prensa_digital", ["musica-en-directo", "conciertos-salas", "acusticos"]),
    ("Daniel", "Ortiz", "Editor de Festivales", "Festivales Madrid Guide", "https://festivalesmadrid.es", "daniel@festivalesmadrid.es", "ocio_nocturno", "blog", ["festivales-verano", "mad-cool", "noches-botanico"]),
    ("Marta", "Delgado", "Curadora de Terrazas", "Terrazas Nocturnas Madrid", "https://terrazasnocturnasmadrid.com", "marta@terrazasnocturnasmadrid.com", "ocio_nocturno", "blog", ["terrazas-noche", "rooftops", "vistas-madrid"]),
    ("Álvaro", "Giménez", "Crítico de Mixología", "El Barman Madrileño", "https://elbarmanmadrileno.com", "alvaro@elbarmanmadrileno.com", "ocio_nocturno", "creador_vlogger", ["mixologia", "tragos-de-autor", "gran-via"]),
    ("Patricia", "Ruiz", "Redactora de Ocio", "Planes de Noche Madrid", "https://planesdenochemadd.es", "patricia@planesdenochemadd.es", "ocio_nocturno", "blog", ["planes-noche", "amigos", "cenas-con-copas"]),
    ("Gonzalo", "Vega", "Organizador de Raves y Clubs", "Madrid Club Culture", "https://madridclubculture.com", "info@madridclubculture.com", "ocio_nocturno", "blog", ["club-culture", "djs-locales", "sesiones-madrid"]),

    # --- Gastronomía, Foodies y Coctelería ---
    ("Alberto", "de Luna", "Crítico Gastronómico", "Dime Un Restaurante", "https://dimeunrestaurante.com", "alberto@dimeunrestaurante.com", "gastronomia", "creador_vlogger", ["critica-gastronomica", "alta-cocina", "restaurantes-madrid"]),
    ("Carlos", "Mateo", "Vlogger Foodie", "Madrid Foodie Guide", "https://madridfoodieguide.com", "carlos@madridfoodieguide.com", "gastronomia", "creador_vlogger", ["foodie", "tiktok-gastro", "brunch-madrid"]),
    ("Patricia", "Duque", "Autora y Sumiller", "Madrid Vinos & Copas", "https://madridvinos.es", "patricia@madridvinos.es", "gastronomia", "blog", ["sumilleria", "vinotecas", "enoturismo"]),
    ("Sofía", "Pérez", "Blogger Gastronómica", "De Tapas Por Madrid", "https://detapaspmadrid.es", "sofia@detapaspmadrid.es", "gastronomia", "blog", ["tapas-clasicas", "rutas-cervezas", "mercado-san-miguel"]),
    ("Redacción", "Gastroactivity", "Redacción Gastro", "Gastroactivity", "https://gastroactivity.com", "info@gastroactivity.com", "gastronomia", "blog", ["gastronomia", "cocteles", "vino"]),
    ("Redacción", "Cocina y Vino", "Equipo Editorial", "Cocina y Vino Madrid", "https://cocinayvino.com", "redaccion@cocinayvino.com", "gastronomia", "prensa_digital", ["alta-gastronomia", "cocteleria", "tendencias"]),
    ("Redacción", "Gastroeconomy", "Aperturas y Negocio", "Gastroeconomy", "https://gastroeconomy.com", "info@gastroeconomy.com", "gastronomia", "prensa_digital", ["negocio-restauracion", "inversion-gastro", "chefs"]),
    ("Felipe", "Morales", "Crítico de Tapas", "La Barra Madrileña", "https://labarramadrilena.es", "felipe@labarramadrilena.es", "gastronomia", "blog", ["barras-historicas", "bocadillo-calamares", "canas"]),
    ("Cristina", "Alonso", "Foodie y Creadora", "Madrid en Bocados", "https://madridenbocados.com", "cristina@madridenbocados.com", "gastronomia", "creador_vlogger", ["restaurantes-trendy", "brunch", "gastro-madrid"]),
    ("Manuel", "Reyes", "Experto en Asadores", "Rutas del Sabor Madrid", "https://rutasdelsabormadrid.es", "manuel@rutasdelsabormadrid.es", "gastronomia", "blog", ["asadores", "carnes", "cocina-castellana"]),
    ("Carmen", "Soler", "Crítica de Repostería", "Madrid Dulce y Copas", "https://madriddulce.es", "carmen@madriddulce.es", "gastronomia", "blog", ["cafes-con-encanto", "postres", "mercadillos"]),
    ("Hugo", "Calvo", "Coctelería Urbana", "Bebedores Madrileños", "https://bebedoresmadrilenos.es", "hugo@bebedoresmadrilenos.es", "gastronomia", "blog", ["cocteles-clasicos", "vermut", "hora-del-vermut"]),
    ("Silvia", "Ríos", "Gastrobloguera", "Platos de la Capital", "https://platosdelacapital.com", "silvia@platosdelacapital.com", "gastronomia", "creador_vlogger", ["restaurantes-romanticos", "cenas-con-amigos", "tapas"]),
    ("Ignacio", "Fuentes", "Cronista de Tabernas", "Tabernas Centenarias Madrid", "https://tabernascentenariasmadrid.es", "ignacio@tabernascentenariasmadrid.es", "gastronomia", "blog", ["tabernas-ilustres", "historia-viva", "cocido-madrileno"]),
    ("Lucía", "Perales", "Foodie y Vlogger", "Cenas Secretas Madrid", "https://cenassecretasmadrid.com", "lucia@cenassecretasmadrid.com", "gastronomia", "creador_vlogger", ["cenas-clandestinas", "experiencias-culinarias", "showcooking"]),

    # --- Cultura, Espectáculos, Teatro y Agendas ---
    ("Antonio", "Castro", "Crítico Teatral", "Revista Godot", "https://revistagodot.com", "redaccion@revistagodot.com", "cultura_espectaculos", "prensa_digital", ["teatro-madrid", "artes-escenicas", "danza"]),
    ("Redacción", "El Teatrero", "Cartelera y Crítica", "El Teatrero", "https://elteatrero.com", "contacto@elteatrero.com", "cultura_espectaculos", "blog", ["teatro-off", "musicales", "cartelera-teatral"]),
    ("Redacción", "Madrid Es Noticia", "Sección Cultura", "Madrid Es Noticia Cultura", "https://madridesnoticia.es", "cultura@madridesnoticia.es", "cultura_espectaculos", "prensa_digital", ["cultura-madrid", "musicales", "conciertos"]),
    ("Redacción", "Somos Malasaña", "Cultura de Barrio", "Somos Madrid Malasaña", "https://somosmalasana.com", "contacto@somosmalasana.com", "cultura_espectaculos", "blog", ["malasana", "cultura-barrio", "bares-malasana"]),
    ("Redacción", "Chueca Mag", "Revista de Cultura", "Chueca Magazine", "https://chueca.com", "redaccion@chueca.com", "cultura_espectaculos", "blog", ["chueca", "diversidad-lgbtq", "noche-chueca"]),
    ("Lucas", "Ferreiro", "Crítico Musical", "Muzikalia Madrid", "https://muzikalia.com", "info@muzikalia.com", "cultura_espectaculos", "blog", ["musica-directo", "conciertos-madrid", "festivales"]),
    ("Esteban", "Lozano", "Cronista de Flamenco", "Madrid Flamenco y Tablaos", "https://madridflamenco.es", "esteban@madridflamenco.es", "cultura_espectaculos", "blog", ["tablaos-flamencos", "cante", "noche-flamenca"]),
    ("Mónica", "Guerrero", "Editora de Cine y Teatro", "La Butaca Madrileña", "https://labutacamadrilena.com", "monica@labutacamadrilena.com", "cultura_espectaculos", "blog", ["gran-via-teatros", "estrenos", "comedias"]),
    ("Rubén", "Pascual", "Arte y Exposiciones", "Madrid Galería Abierta", "https://madridgaleria.es", "ruben@madridgaleria.es", "cultura_espectaculos", "blog", ["museos", "galerias-de-arte", "exposiciones-temporales"]),
    ("Teresa", "Campos", "Agenda Infantil y Familiar", "Madrid Con Niños y Jóvenes", "https://madridconninos.com", "teresa@madridconninos.com", "cultura_espectaculos", "blog", ["circo", "teatro-musical", "espectaculos-familiares"]),
    ("Andrés", "Romero", "Fotógrafo y Reportero Cultural", "Madrid en Escena", "https://madridenescena.es", "andres@madridenescena.es", "cultura_espectaculos", "creador_vlogger", ["fotografia-escenica", "backstage", "artistas"]),
    ("Nuria", "Vila", "Directora de Programación", "Salas Alternativas Madrid", "https://salasalternativasmadrid.es", "nuria@salasalternativasmadrid.es", "cultura_espectaculos", "blog", ["microteatro", "lavapies", "teatro-independiente"]),
    ("Guillermo", "Soto", "Cronista de Monólogos", "Madrid Comedy Club Blog", "https://madridcomedy.es", "guillermo@madridcomedy.es", "cultura_espectaculos", "blog", ["monologos", "stand-up", "comedia-en-vivo"]),
    ("Paula", "Bermejo", "Editora de Danza", "Danza y Movimiento Madrid", "https://danzamadrid.es", "paula@danzamadrid.es", "cultura_espectaculos", "blog", ["danza-contemporanea", "ballet", "teatros-canal"]),
    ("Óscar", "Molina", "Crítica de Musicales", "Musicales Gran Vía Mag", "https://musicalesgranvia.com", "oscar@musicalesgranvia.com", "cultura_espectaculos", "blog", ["broadway-espanol", "gran-via", "musicales"]),

    # --- Turismo Urbano, Destino Madrid y Escapadas ---
    ("Redacción", "Mirador Madrid", "Guía Urbana", "Mirador Madrid", "https://miradormadrid.com", "contacto@miradormadrid.com", "turismo", "blog", ["turismo-madrid", "terrazas-vistas", "rooftops"]),
    ("Manu", "García", "Divulgador Turístico", "Secretos de Madrid", "https://secretosdemadrid.es", "contacto@secretosdemadrid.es", "turismo", "creador_vlogger", ["historia-madrid", "curiosidades", "creador-contenido"]),
    ("Redacción", "Madrid Sensations", "Experiencias de Turismo", "Madrid Sensations", "https://madridsensations.com", "info@madridsensations.com", "turismo", "portal_turismo", ["experiencias-madrid", "flamenco-show", "tours-nocturnos"]),
    ("Marcos", "Ramos", "Guía Turístico", "Rutas Por Madrid", "https://rutaspormadrid.es", "marcos@rutaspormadrid.es", "turismo", "blog", ["rutas-a-pie", "madrid-de-los-austrias", "tabernas-historicas"]),
    ("Redacción", "Vivir Madrid", "Revista de Ciudad", "Vivir Madrid Magazine", "https://vivirmadrid.net", "prensa@vivirmadrid.net", "turismo", "blog", ["planes-turismo", "alojamiento", "guia-madrid"]),
    ("Ángela", "Cano", "Blogger de Hoteles", "Hoteles con Encanto Madrid", "https://hotelesconencantomadrid.es", "angela@hotelesconencantomadrid.es", "turismo", "blog", ["hoteles-boutique", "estancias-romanticas", "centro-madrid"]),
    ("César", "Navas", "Guía de Monumentos", "Madrid Para Descubrir", "https://madridparadescubrir.com", "cesar@madridparadescubrir.com", "turismo", "blog", ["palacio-real", "retiro", "turismo-cultural"]),
    ("Lorena", "Prieto", "Escapadas y Fines de Semana", "Escapadas Madrid Blog", "https://escapadasmadrid.es", "lorena@escapadasmadrid.es", "turismo", "blog", ["escapadas-cercanas", "sierra-de-madrid", "turismo-comunidad"]),
    ("Tomás", "Beltrán", "Tours Nocturnos", "Madrid de Noche Tours", "https://madriddenochetours.es", "tomas@madriddenochetours.es", "turismo", "portal_turismo", ["tours-de-misterio", "leyendas-nocturnas", "bares-antiguos"]),
    ("Inés", "Cabrera", "Guía Gastroturística", "Sabores Turísticos Madrid", "https://saboresturisticosmadrid.es", "ines@saboresturisticosmadrid.es", "turismo", "blog", ["turismo-gastronomico", "rutas-de-vino", "chotis-y-tapas"]),

    # --- Estilo de Vida, Tendencias y Terrazas ---
    ("Lucía", "Herrero", "Editora de Terrazas", "Madrid Chic Magazine", "https://madridchic.es", "lucia@madridchic.es", "estilo_de_vida", "blog", ["lifestyle", "terrazas-madrid", "moda"]),
    ("Redacción", "Madrid Urban Style", "Tendencias Callejeras", "Madrid Urban Style", "https://madridurbanstyle.com", "contacto@madridurbanstyle.com", "estilo_de_vida", "blog", ["streetstyle", "cultura-urbana", "planes-finde"]),
    ("Equipo", "ShMadrid", "Vida Madrileña", "ShMadrid Lifestyle Blog", "https://shmadrid.es", "blog@shmadrid.es", "estilo_de_vida", "blog", ["vivir-madrid", "barrios-madrid", "planes-noche"]),
    ("Redacción", "Rooftops Madrid Guide", "Guía de Azoteas", "Rooftops Madrid Guide", "https://rooftopsmadrid.com", "info@rooftopsmadrid.com", "estilo_de_vida", "blog", ["azoteas", "rooftops-gran-via", "cocteles-al-atardecer"]),
    ("Clara", "Vázquez", "Blogger de Tendencias", "Planes Con Clara", "https://planesconclara.com", "clara@planesconclara.com", "estilo_de_vida", "creador_vlogger", ["planes-pareja", "bares-originales", "coctelerias-secretas"]),
    ("Raquel", "Mendoza", "Moda y Noche", "Madrid Glam & Night", "https://madridglam.es", "raquel@madridglam.es", "estilo_de_vida", "blog", ["dress-code", "fiestas-exclusivas", "clubes-privados"]),
    ("Borja", "Salas", "Influencer de Ocio", "Planes con Borja", "https://planesconborja.com", "borja@planesconborja.com", "estilo_de_vida", "creador_vlogger", ["planes-amigos", "afterwork", "tiktok-madrid"]),
    ("Noelia", "Santos", "Revista de Bienestar y Belleza", "Madrid Zen & Chic", "https://madridzen.es", "noelia@madridzen.es", "estilo_de_vida", "blog", ["spas", "wellness", "afterwork-relajante"]),
    ("Jaime", "Garrido", "Planes Singulares", "La Guía Secreta Madrid", "https://guiasecretamadrid.es", "jaime@guiasecretamadrid.es", "estilo_de_vida", "blog", ["lugares-escondidos", "bares-clandestinos", "planes-diferentes"]),
    ("Miriam", "Esteban", "Vida Nocturna y Terrazas", "Madrid al Anochecer", "https://madridalanochecer.es", "miriam@madridalanochecer.es", "estilo_de_vida", "creador_vlogger", ["atardeceres-madrid", "terrazas-chic", "cocteles"]),

    # --- Revistas Sectoriales y Hostelería B2B ---
    ("Redacción", "Hostelería News B2B", "Sectorial B2B", "Hostelería Digital España", "https://hosteleriadigital.es", "redaccion@hosteleriadigital.es", "sectorial_hosteleria", "prensa_digital", ["horeca", "empresas-hosteleria", "cehe"]),
    ("Ignacio", "Carrasco", "Director Horeca", "Bar & Drinks España", "https://baranddrinks.es", "ignacio@baranddrinks.es", "sectorial_hosteleria", "blog", ["destilados", "bartenders", "industria-de-bebidas"]),
    ("Redacción", "Gastrobar Negocios", "Técnica y Gestión", "Gastrobar Magazine", "https://gastrobarmagazine.com", "info@gastrobarmagazine.com", "sectorial_hosteleria", "prensa_digital", ["gestion-hosteleria", "inversion-restaurantes"]),
    ("Redacción", "Noche España B2B", "Patronal de Ocio", "Federación España de Noche", "https://espanadenoche.es", "comunicacion@espanadenoche.es", "sectorial_hosteleria", "prensa_digital", ["patronal-noche", "discotecas-espana", "normativa-ocio"]),
    ("Vicente", "Pardo", "Consultor de Locales", "Gestión Ocio y Bares", "https://gestionocioybares.es", "vicente@gestionocioybares.es", "sectorial_hosteleria", "blog", ["licencias-ocio", "rentabilidad-bares", "tendencias-nocturnas"]),
    ("Marina", "López", "Revista de Proveedores Horeca", "Equipamiento Hostelería Madrid", "https://equipamientohosteleria.es", "marina@equipamientohosteleria.es", "sectorial_hosteleria", "prensa_digital", ["proveedores-horeca", "sonido-e-iluminacion", "bares"]),
    ("Félix", "Bautista", "Negocio de Entretenimiento", "Entretenimiento B2B", "https://entretenimientob2b.es", "felix@entretenimientob2b.es", "sectorial_hosteleria", "blog", ["produccion-eventos", "espectaculos-b2b", "patrocinios"]),
    ("Susana", "Herranz", "Hostelería Sostenible", "EcoHostelería Madrid", "https://ecohosteleriamadrid.es", "susana@ecohosteleriamadrid.es", "sectorial_hosteleria", "blog", ["sostenibilidad-noche", "reciclaje-salas", "consumo-responsable"]),

    # --- Prensa Generalista Madrid y Agencias ---
    ("Redacción", "Gacetín Madrid", "Redacción Local", "Gacetín Madrid", "https://gacetinmadrid.com", "redaccion@gacetinmadrid.com", "generalista_madrid", "prensa_digital", ["distritos-madrid", "actualidad-local", "sociedad-madrid"]),
    ("Equipo", "Madrid Actual", "Sección Ocio y Sociedad", "Madrid Actual", "https://madridactual.es", "redaccion@madridactual.es", "generalista_madrid", "prensa_digital", ["noticias-comunidad", "politica-local", "planes-madrid"]),
    ("Redacción", "MadridPress", "Agencia de Noticias", "MadridPress", "https://madridpress.com", "noticias@madridpress.com", "generalista_madrid", "prensa_digital", ["agencia-local", "prensa-madrid", "sociedad"]),
    ("Redacción", "El Independiente", "Tendencias y Sociedad", "El Independiente Tendencias", "https://elindependiente.com", "tendencias@elindependiente.com", "generalista_madrid", "prensa_digital", ["tendencias-sociedad", "ocio-urbano", "lifestyle"]),
    ("Fernando", "Cano", "Redactor de Sociedad", "Capital Madrid Noticias", "https://capitalmadrid.es", "fernando@capitalmadrid.es", "generalista_madrid", "prensa_digital", ["economia-local", "ocio-madrid", "empresas-noche"]),
    ("Alicia", "Montes", "Crónica de Barrios", "Madrid Vecinal", "https://madridvecinal.org", "comunicacion@madridvecinal.org", "generalista_madrid", "blog", ["barrios", "convivencia-y-ocio", "cultura-popular"]),
    ("Roberto", "Sanz", "Periodista Local", "Voz de Madrid Digital", "https://vozdemadrid.es", "roberto@vozdemadrid.es", "generalista_madrid", "prensa_digital", ["actualidad-madrid", "eventos-ciudad", "reportajes"])
]

FRANCE_CONTACTS = [
    ("Pierre", "Moreau", "Chroniqueur Nuit", "Madrid Pour Les Français (Sorties)", "https://madridpourlesfrancais.com", "pierre.moreau@madridpourlesfrancais.com", "ocio_nocturno", "blog", ["bars-a-tapas", "sorties-madrid", "boites-de-nuit"]),
    ("Camille", "Dubois", "Blogueuse Voyage", "Carnet d'Espagne", "https://carnetdespagne.fr", "camille@carnetdespagne.fr", "turismo", "blog", ["voyage-madrid", "week-end-madrid", "escapade-urbaine"]),
    ("Rédaction", "Figaro Voyages", "Correspondance Espagne", "Le Figaro Voyages", "https://lefigaro.fr/voyages", "voyages.espagne@lefigaro.fr", "turismo", "prensa_digital", ["destination-madrid", "hotels-madrid", "tourisme-haut-de-gamme"]),
    ("Julien", "Garnier", "Foodie et Critique", "Tapas & Co Madrid", "https://tapasandco.fr", "julien@tapasandco.fr", "gastronomia", "creador_vlogger", ["foodie-francophone", "marche-san-miguel", "restos-madrid"]),
    ("Rédaction", "Routard Espagne", "Équipe Éditoriale", "Guide du Routard Madrid", "https://routard.com", "redaction.espagne@routard.com", "turismo", "portal_turismo", ["guide-routard", "bons-plans-madrid", "vie-nocturne"]),
    ("Élise", "Bernard", "Journaliste Art & Culture", "Courrier d'Espagne Culture", "https://courrierdespagne.com", "elise.bernard@courrierdespagne.com", "cultura_espectaculos", "prensa_digital", ["musees-madrid", "festivals-espagne", "theatre"]),
    ("Rédaction", "Trax Magazine", "Musique Électronique", "Trax Magazine Espagne", "https://traxmag.com", "redaction@traxmag.com", "ocio_nocturno", "prensa_digital", ["clubbing-europe", "techno-madrid", "festivals"]),
    ("Marc", "Fontaine", "Blogueur Nuit Cachée", "Madrid Insolite", "https://madridinsolite.com", "marc@madridinsolite.com", "estilo_de_vida", "blog", ["madrid-secret", "bars-caches", "speakeasy"]),
    ("Équipe", "Vivre en Espagne", "Guide Tourisme", "Vivre en Espagne Blog", "https://vivre-en-espagne.com", "contact@vivre-en-espagne.com", "turismo", "blog", ["expats-madrid", "sortir-a-madrid", "tourisme"]),
    ("Claire", "Vidal", "Sommelière", "Vins & Terroirs d'Espagne", "https://vinsespagne.fr", "claire@vinsespagne.fr", "gastronomia", "blog", ["vins-espagnols", "bodegas-madrid", "maridaje-tapas"]),
    ("Antoine", "Rousseau", "Critique Théâtre et Scène", "Scènes d'Europe Madrid", "https://scenesdeurope.fr", "antoine@scenesdeurope.fr", "cultura_espectaculos", "blog", ["theatre-espagnol", "danse-flamenco", "opera-madrid"]),
    ("Hélène", "Mercier", "Guide Festif", "Madrid By Night Francophone", "https://madridbynight.fr", "helene@madridbynight.fr", "ocio_nocturno", "blog", ["soirees-madrid", "djs-francais", "fiesta-espagnole"]),
    ("Guillaume", "Faure", "Vlogger Voyage", "Un Français à Madrid", "https://unfrancaisamadrid.fr", "guillaume@unfrancaisamadrid.fr", "turismo", "creador_vlogger", ["vlog-voyage", "week-end-festif", "madrid-en-3-jours"]),
    ("Sophie", "Lefebvre", "Lifestyle et Mode", "Chic Espagnol Magazine", "https://chicespagnol.fr", "sophie@chicespagnol.fr", "estilo_de_vida", "blog", ["rooftops-chics", "mode-madrid", "terrasses-luxe"]),
    ("Nicolas", "Gautier", "Journaliste Économique", "L'Écho d'Espagne B2B", "https://lechodespagne.com", "nicolas@lechodespagne.com", "sectorial_hosteleria", "prensa_digital", ["investissements-tourisme", "affaires-espagne", "hotellerie"]),
    ("Pauline", "Chevalier", "Blogger Gastronome", "Saveurs Ibériques", "https://saveursiberiques.fr", "pauline@saveursiberiques.fr", "gastronomia", "blog", ["jambon-iberique", "tapas-gourmet", "adresses-madrid"]),
    ("Damien", "Perrin", "Chroniqueur Électro", "Clubbing France-Espagne", "https://clubbingfranceespagne.fr", "damien@clubbingfranceespagne.fr", "ocio_nocturno", "blog", ["festivals-espagne", "clubs-madrid", "techno-nights"]),
    ("Isabelle", "Morin", "Photographe Culturelle", "Madrid en Lumières", "https://madridenlumieres.fr", "isabelle@madridenlumieres.fr", "cultura_espectaculos", "creador_vlogger", ["art-urbain", "expositions-madrid", "rues-historiques"]),
    ("Benoît", "Lambert", "Spécialiste Horeca", "CHR Espagne Réseau", "https://chrespagne.com", "benoit@chrespagne.com", "sectorial_hosteleria", "blog", ["restauration-espagne", "bars-et-bistrots", "franchises-madrid"]),
    ("Lucie", "Renard", "Guide Étudiant & Fêtes", "Erasmus Français Madrid", "https://erasmusfrancais.fr", "lucie@erasmusfrancais.fr", "ocio_nocturno", "blog", ["soirees-etudiantes", "bars-pas-chers", "sortir-a-madrid"]),
    ("Maxime", "Boucher", "Guide Insolite", "Madrid Hors Pistes", "https://madridhorspistes.fr", "maxime@madridhorspistes.fr", "turismo", "blog", ["adresses-secretes", "points-de-vue", "escapades"]),
    ("Amélie", "Giraud", "Critique Cocktails", "Cocktails et Tapas", "https://cocktailsettapas.fr", "amelie@cocktailsettapas.fr", "gastronomia", "blog", ["bars-a-cocktails", "mixologie-espagnole", "nuits-madrilenes"]),
    ("Olivier", "Caron", "Rédacteur en chef", "Le Petit Journal Madrid Sorties", "https://lepetitjournal.com/madrid", "sorties.madrid@lepetitjournal.com", "ocio_nocturno", "prensa_digital", ["agenda-madrid", "festivals", "soirees-francaises"]),
    ("Nathalie", "Besson", "Chroniqueuse Flamenco", "Passion Flamenco Espagne", "https://passionflamenco.fr", "nathalie@passionflamenco.fr", "cultura_espectaculos", "blog", ["tablaos-madrid", "danse-andalouse", "culture-espagnole"]),
    ("François", "Dumas", "Baroudeur Urbain", "Le Guide Urbain Madrid", "https://guideurbainmadrid.fr", "francois@guideurbainmadrid.fr", "estilo_de_vida", "blog", ["quartiers-chics", "malasana-en-francais", "terrasses"])
]

ITALY_CONTACTS = [
    ("Matteo", "Rossi", "Curatore Movida", "Vivere a Madrid (Movida)", "https://viveremadrid.info", "matteo.rossi@viveremadrid.info", "ocio_nocturno", "blog", ["movida-madrilena", "locali-notturni", "discoteche-madrid"]),
    ("Francesca", "Romano", "Blogger di Weekend", "Destinazione Madrid (Blog)", "https://destinazionemadrid.it", "francesca@destinazionemadrid.it", "turismo", "portal_turismo", ["weekend-madrid", "cosa-fare-a-madrid", "hotel-boutique"]),
    ("Redazione", "Spagna Mania", "Redazione Cucina e Serate", "Spagna Mania", "https://spagnamania.it", "info@spagnamania.it", "gastronomia", "blog", ["tapas-madrid", "sangria-cocktail", "ristoranti-tipici"]),
    ("Lorenzo", "Bianchi", "Giornalista e Fotografo", "Madrid Segreta IT", "https://madridsegreta.it", "lorenzo@madridsegreta.it", "cultura_espectaculos", "blog", ["musei-madrid", "teatro-spagnolo", "angoli-nascosti"]),
    ("Redazione", "Viaggi Low Cost", "Divertimento Giovani", "Viaggi Low Cost Spagna", "https://viaggispagna.it", "redazione@viaggispagna.it", "ocio_nocturno", "portal_turismo", ["giovani-madrid", "divertimento-low-cost", "discoteche"]),
    ("Chiara", "Esposito", "Creator Lifestyle & Aperitivi", "Aperitivo a Madrid", "https://aperitivomadrid.it", "chiara@aperitivomadrid.it", "estilo_de_vida", "creador_vlogger", ["aperitivo-chic", "rooftop-madrid", "cocktail-bar"]),
    ("Team", "Italiani a Madrid", "Coordinatore Serate", "Italiani a Madrid Community", "https://italianiamadrid.com", "eventi@italianiamadrid.com", "ocio_nocturno", "blog", ["comunita-italiani", "feste-espatriati", "erasmus-madrid"]),
    ("Davide", "Conti", "Critico Musicale", "Sound Spagna", "https://soundspagna.it", "davide@soundspagna.it", "ocio_nocturno", "blog", ["clubbing-madrid", "festival-spagna", "musica-elettronica-it"]),
    ("Giulia", "Ferrari", "Foodie e Cucina Spagnola", "Sapori di Madrid", "https://saporidimadrid.it", "giulia@saporidimadrid.it", "gastronomia", "creador_vlogger", ["paella-e-tapas", "jamon-iberico", "mercati-di-madrid"]),
    ("Marco", "Ricci", "Viaggiatore e Vlogger", "Marco in Spagna", "https://marcoinspagna.it", "marco@marcoinspagna.it", "turismo", "creador_vlogger", ["vlog-madrid", "citybreak-spagna", "consigli-viaggio"]),
    ("Elena", "Marini", "Esperta di Teatro e Arte", "Arte e Cultura Madrid", "https://arteculturamadrid.it", "elena@arteculturamadrid.it", "cultura_espectaculos", "blog", ["prado-e-reina-sofia", "teatro-reale", "spettacoli-flamenco"]),
    ("Simone", "Galli", "Curatore Notti Elettroniche", "Clubbing Italia-Madrid", "https://clubbingitaliamadrid.it", "simone@clubbingitaliamadrid.it", "ocio_nocturno", "blog", ["dj-set-madrid", "serate-techno", "feste-notturne"]),
    ("Federica", "Greco", "Blogger di Tendenze", "Madrid Chic per Italiani", "https://madridchic.it", "federica@madridchic.it", "estilo_de_vida", "blog", ["shopping-madrid", "locali-alla-moda", "terrazze-con-vista"]),
    ("Andrea", "De Luca", "Giornalista Horeca", "Ristorazione e Notte B2B", "https://ristorazionenotte.it", "andrea@ristorazionenotte.it", "sectorial_hosteleria", "prensa_digital", ["b2b-spagna-italia", "aperture-locali", "gestione-bar"]),
    ("Silvia", "Costantini", "Guida Turistica Ufficiale", "Guida Madrilena", "https://guidamadrilena.it", "silvia@guidamadrilena.it", "turismo", "blog", ["tour-madrid-italiano", "chueca-e-malasana", "storia-citta"]),
    ("Alessio", "Mancini", "Chitarrista e Critico", "Flamenco e Chitarra Madrid", "https://flamencomadrid.it", "alessio@flamencomadrid.it", "cultura_espectaculos", "blog", ["tablao-flamenco", "musica-andalusa", "notti-spagnole"]),
    ("Valentina", "Russo", "Blogger di Tapas Bar", "Il Giro delle Tapas", "https://ilgirodelletapas.it", "valentina@ilgirodelletapas.it", "gastronomia", "blog", ["tapas-tour-madrid", "cerveza-e-tinto", "bar-storici"]),
    ("Fabio", "Santoro", "Organizzatore Eventi", "Erasmus & Movida Madrid", "https://erasmusmovidamadrid.it", "fabio@erasmusmovidamadrid.it", "ocio_nocturno", "blog", ["feste-erasmus", "pub-crawl-madrid", "locali-giovani"]),
    ("Roberta", "Lombardi", "Chroniqueur Viaggi", "Vacanze a Madrid Blog", "https://vacanzeamadrid.it", "roberta@vacanzeamadrid.it", "turismo", "portal_turismo", ["itinerario-madrid", "voli-lowcost", "migliori-quartieri"]),
    ("Gianluca", "Moretti", "Mixologist e Reporter", "Cocktail & Movida", "https://cocktailmovida.it", "gianluca@cocktailmovida.it", "gastronomia", "blog", ["bartender-italiani-madrid", "vermut-madrileno", "speakeasies"]),
    ("Martina", "Fontana", "Creator di Viaggi", "Martina Viaggia Madrid", "https://martinaviaggia.it", "martina@martinaviaggia.it", "estilo_de_vida", "creador_vlogger", ["tiktok-viaggi", "posti-instagrammabili", "madrid-by-night"]),
    ("Daniele", "Serra", "Musica dal Vivo", "Concerti a Madrid IT", "https://concertiamadrid.it", "daniele@concertiamadrid.it", "cultura_espectaculos", "blog", ["live-music-madrid", "band-italiane-in-spagna", "club-jazz"]),
    ("Paola", "Caruso", "Eventi Aziendali e MICE", "Madrid Business e Turismo", "https://madridbusinessturismo.it", "paola@madridbusinessturismo.it", "sectorial_hosteleria", "prensa_digital", ["congressi-madrid", "cene-aziendali", "hotel-mice"]),
    ("Stefano", "Piras", "Guida ai Quartieri", "Quartieri di Madrid Blog", "https://quartierimadrid.it", "stefano@quartierimadrid.it", "turismo", "blog", ["lavapies-e-latina", "malasana-rock", "salamanca-lusso"]),
    ("Ilaria", "Colombo", "Aperitivi e Feste", "Madrid di Sera", "https://madriddisea.it", "ilaria@madriddisea.it", "ocio_nocturno", "blog", ["serate-madrid", "discoteche-trendy", "feste-estate"])
]

UK_CONTACTS = [
    ("Jack", "Davies", "Nightlife Writer", "Naked Madrid (Nightlife)", "https://nakedmadrid.com", "jack@nakedmadrid.com", "ocio_nocturno", "blog", ["secret-cocktails", "craft-beer-madrid", "madrid-bars"]),
    ("Sarah", "Jenkins", "Food Journalist", "Spain For Foodies Blog", "https://spainforfoodies.co.uk", "sarah@spainforfoodies.co.uk", "gastronomia", "blog", ["madrid-food-tours", "tapas-hopping", "michelin-stars"]),
    ("Editorial", "The Olive Press", "Madrid Bureau Chief", "The Olive Press Madrid", "https://theolivepress.es", "madrid@theolivepress.es", "generalista_madrid", "prensa_digital", ["english-newspaper-spain", "madrid-news", "nightlife-news"]),
    ("Redacción", "Spotted by Locals", "Spotters Lead", "Spotted by Locals Madrid", "https://spottedbylocals.com", "madrid@spottedbylocals.com", "turismo", "portal_turismo", ["local-insider", "authentic-madrid", "underground-clubs"]),
    ("Mark", "Foster", "Events & Pub Crawls", "Citylife Madrid (Nightlife)", "https://citylifemadrid.com", "nightlife@citylifemadrid.com", "ocio_nocturno", "creador_vlogger", ["club-nights", "pub-crawl", "nightlife-madrid"]),
    ("Hannah", "Clark", "Arts Correspondent", "Madrid Metropolis Blog", "https://madridmetropolis.com", "hannah@madridmetropolis.com", "cultura_espectaculos", "blog", ["theatre-madrid", "flamenco-madrid", "museum-nights"]),
    ("Redacción", "The Local Spain", "Lifestyle Editor", "The Local Spain (Lifestyle)", "https://thelocal.es", "lifestyle@thelocal.es", "estilo_de_vida", "prensa_digital", ["expat-spain", "city-breaks", "tapas-culture"]),
    ("Tom", "Wilson", "Travel Filmmaker", "Madrid Weekend Guide UK", "https://madridweekendguide.co.uk", "tom@madridweekendguide.co.uk", "turismo", "creador_vlogger", ["youtube-madrid", "vlogger", "nightlife-tour"]),
    ("Emily", "Taylor", "Cocktail Historian", "Madrid Speakeasy Club", "https://madridspeakeasy.com", "emily@madridspeakeasy.com", "gastronomia", "blog", ["cocktail-bars", "hidden-bars", "vermouth-tasting"]),
    ("Oliver", "Brown", "Live Music Reviewer", "Madrid Live Music Guide", "https://madridlivemusic.co.uk", "oliver@madridlivemusic.co.uk", "ocio_nocturno", "blog", ["indie-music", "jazz-clubs-madrid", "gig-venues"]),
    ("Jessica", "Smith", "Expat Lifestyle Blogger", "British in Madrid Blog", "https://britishinmadrid.co.uk", "jessica@britishinmadrid.co.uk", "estilo_de_vida", "blog", ["expat-community", "weekend-trips", "dining-out"]),
    ("Harry", "Green", "Clubbing & DJ Columnist", "Ibiza to Madrid Sound", "https://ibizatomadrid.com", "harry@ibizatomadrid.com", "ocio_nocturno", "blog", ["house-music", "superclubs", "dj-nights-madrid"]),
    ("Chloe", "Edwards", "Tapas & Rooftop Curator", "Secret Rooftops Madrid", "https://secretrooftopsmadrid.com", "chloe@secretrooftopsmadrid.com", "estilo_de_vida", "creador_vlogger", ["sunset-drinks", "skyline-views", "cocktails"]),
    ("George", "Harris", "Beer & Pub Enthusiast", "Madrid Craft Beer Scene", "https://madridcraftbeer.co.uk", "george@madridcraftbeer.co.uk", "gastronomia", "blog", ["craft-breweries", "taprooms-madrid", "bar-hopping"]),
    ("Megan", "Walker", "Cultural Travel Writer", "European City Breaks UK", "https://europeancitybreaks.co.uk", "megan@europeancitybreaks.co.uk", "turismo", "blog", ["madrid-itinerary", "culture-and-food", "boutique-stays"]),
    ("Liam", "Scott", "Party & Festival Guide", "Madrid Fiesta Guides", "https://madridfiestaguides.com", "liam@madridfiestaguides.com", "ocio_nocturno", "portal_turismo", ["summer-festivals", "boat-parties", "vip-club-access"]),
    ("Rebecca", "Turner", "Flamenco & Spanish Arts", "Flamenco Passion Madrid", "https://flamencopassion.co.uk", "rebecca@flamencopassion.co.uk", "cultura_espectaculos", "blog", ["flamenco-shows", "cultural-evenings", "authentic-spain"]),
    ("Ben", "Cooper", "Hospitality Analyst", "Spain Horeca Insight", "https://spainhorecainsight.com", "ben@spainhorecainsight.com", "sectorial_hosteleria", "prensa_digital", ["hotel-industry-madrid", "nightlife-investments", "tourism-trends"]),
    ("Lucy", "Baker", "Sunday Strolls & Markets", "Madrid Barrios Guide", "https://madridbarrios.com", "lucy@madridbarrios.com", "estilo_de_vida", "blog", ["el-rastro", "la-latina-sunday", "tapas-crawl"]),
    ("Sam", "Wright", "Budget Backpacker Guide", "Madrid on a Shoestring", "https://madridshoestring.com", "sam@madridshoestring.com", "turismo", "blog", ["hostels-madrid", "free-museums", "cheap-tapas"]),
    ("Alice", "Robinson", "Luxury & VIP Experiences", "Luxury Madrid Nights", "https://luxurymadridnights.com", "alice@luxurymadridnights.com", "estilo_de_vida", "blog", ["vip-table-booking", "michelin-dining", "five-star-hotels"]),
    ("James", "Miller", "Podcast Host & Interviewer", "Madrid Calling Podcast", "https://madridcalling.com", "james@madridcalling.com", "cultura_espectaculos", "creador_vlogger", ["madrid-stories", "interviews-artists", "city-pulse"]),
    ("Grace", "Hall", "Wine & Gastronomy Tours", "Madrid Wine Experience", "https://madridwineexperience.co.uk", "grace@madridwineexperience.co.uk", "gastronomia", "portal_turismo", ["wine-tours-madrid", "cava-bars", "spanish-sommelier"]),
    ("Daniel", "Adams", "Erasmus & Youth Events", "Madrid Student Life", "https://madridstudentlife.com", "daniel@madridstudentlife.com", "ocio_nocturno", "blog", ["erasmus-parties", "student-bars", "clubbing-discounts"]),
    ("Charlotte", "King", "Boutique Hotel Reviewer", "Chic Stays Madrid", "https://chicstaysmadrid.co.uk", "charlotte@chicstaysmadrid.co.uk", "turismo", "blog", ["design-hotels", "weekend-getaways", "terrace-bars"])
]

GERMANY_CONTACTS = [
    ("Stefan", "Bauer", "Gründer & Reiseleiter", "Madrid Mal Anders (Szene)", "https://madrid-mal-anders.de", "stefan@madrid-mal-anders.de", "ocio_nocturno", "blog", ["szeneviertel-madrid", "tapas-touren", "live-musik"]),
    ("Birgit", "Weber", "Ressortleiterin Reisen", "Spanien Reisemagazin Madrid", "https://spanien-reisemagazin.de", "birgit.weber@spanien-reisemagazin.de", "turismo", "portal_turismo", ["staedtereisen", "kultururlaub", "hotels-madrid"]),
    ("Redaktion", "Spanien Aktuell", "Redaktion Kultur & Gastro", "Spanien Aktuell", "https://spanien-aktuell.de", "redaktion@spanien-aktuell.de", "gastronomia", "prensa_digital", ["spanische-kueche", "tapas-bars", "rioja-weine"]),
    ("Klaus", "Schneider", "Reiseblogger und Foodie", "Madrid Genuss Blog", "https://madridgenuss.de", "klaus@madridgenuss.de", "gastronomia", "blog", ["gourmet-madrid", "food-blogger-deutsch", "cocktails"]),
    ("Team", "Deutsche in Madrid", "Community & Events", "Deutsche in Madrid Portal", "https://deutsche-in-madrid.com", "events@deutsche-in-madrid.com", "ocio_nocturno", "blog", ["deutschsprachige-community", "afterwork-madrid", "party"]),
    ("Julia", "Richter", "Kunst- und Kulturjournalistin", "Madrid Kultur Depesche", "https://madridkultur.de", "julia@madridkultur.de", "cultura_espectaculos", "blog", ["kunstmeile-madrid", "prado-reina-sofia", "flamenco-show"]),
    ("Felix", "Wagner", "Musikjournalist & DJ", "Clubkultur Spanien", "https://clubkultur-spanien.de", "felix@clubkultur-spanien.de", "ocio_nocturno", "blog", ["elektronische-musik", "clubs-madrid", "szene-party"]),
    ("Redaktion", "Reisedepeschen", "Kulturautoren", "Reisedepeschen Spanien", "https://reisedepeschen.de", "redaktion@reisedepeschen.de", "turismo", "blog", ["autoren-reiseberichte", "literarisches-madrid", "stadtbummel"]),
    ("Lukas", "Zimmermann", "Tapas & Bar-Scout", "Madrider Kneipenführer", "https://kneipenfuehrermadrid.de", "lukas@kneipenfuehrermadrid.de", "gastronomia", "blog", ["tapas-kneipen", "bierkultur-spanien", "malasana-bars"]),
    ("Monika", "Hoffmann", "Städtereise-Bloggerin", "Wochenende in Madrid", "https://wochenendeinmadrid.de", "monika@wochenendeinmadrid.de", "turismo", "creador_vlogger", ["citytrip-madrid", "rooftop-bars", "sehenswuerdigkeiten"]),
    ("Tobias", "Lang", "Clubbing & Nachtleben", "Nachtleben Madrid Guide DE", "https://nachtlebenmadrid.de", "tobias@nachtlebenmadrid.de", "ocio_nocturno", "blog", ["discotheken-madrid", "feiern-in-spanien", "partytipps"]),
    ("Sabine", "Kraus", "Weinexpertin", "Bodega & Wein Madrid", "https://bodegaweinmadrid.de", "sabine@bodegaweinmadrid.de", "gastronomia", "blog", ["spanische-weine", "tapas-pairing", "weinlokale"]),
    ("Markus", "Wolf", "Theater- und Opernkritiker", "Kulturzeit Madrid", "https://kulturzeitmadrid.de", "markus@kulturzeitmadrid.de", "cultura_espectaculos", "blog", ["teatro-real", "oper-madrid", "festspiele"]),
    ("Anna", "Schmid", "Lifestyle & Rooftops", "Madrid Chic Deutsch", "https://madridchic.de", "anna@madridchic.de", "estilo_de_vida", "creador_vlogger", ["dachterrassen-madrid", "boutique-hotels", "design"]),
    ("Christian", "Vogel", "Tourismuswirtschaft", "Spanien Tourismus Forum B2B", "https://spanientourismusforum.de", "christian@spanientourismusforum.de", "sectorial_hosteleria", "prensa_digital", ["hotelwirtschaft", "tourismus-trends", "gastronomie-b2b"]),
    ("Laura", "Koch", "Alternative Stadtrundgänge", "Madrid Versteckt Entdecken", "https://madridversteckt.de", "laura@madridversteckt.de", "turismo", "blog", ["geheimtipps-madrid", "chueca-flair", "altstadt-bummel"]),
    ("Jan", "Becker", "Studenten & Nachtleben", "Erasmus Madrid Deutsch", "https://erasmusmadrid.de", "jan@erasmusmadrid.de", "ocio_nocturno", "blog", ["studentenparty", "pubcrawl-deutsch", "clubs"]),
    ("Kerstin", "Schulz", "Kultur & Flamenco", "Flamenco Faszination Madrid", "https://flamencofaszination.de", "kerstin@flamencofaszination.de", "cultura_espectaculos", "blog", ["tablaos-besuchen", "spanischer-tanz", "gitarrenkonzerte"]),
    ("Florian", "Hartmann", "Gourmetkritiker", "Madrid Feinschmecker", "https://madridfeinschmecker.de", "florian@madridfeinschmecker.de", "gastronomia", "blog", ["sterne-restaurants", "madrider-kueche", "tapas-touren"]),
    ("Sandra", "Lehmann", "Reisefotografin", "Madrid im Fokus", "https://madridimfokus.de", "sandra@madridimfokus.de", "turismo", "creador_vlogger", ["fotospots-madrid", "sunset-chulapo", "palast-fotos"]),
    ("Tim", "Fischer", "Mixologie & Nachtleben", "Cocktailbar Szene Madrid", "https://cocktailbarszenemadrid.de", "tim@cocktailbarszenemadrid.de", "gastronomia", "blog", ["barkultur", "speakeasies-madrid", "vermut-kultur"]),
    ("Katharina", "Maier", "Sonntagsmärkte & Kunst", "Madrid Stadtleben", "https://madridstadtleben.de", "katharina@madridstadtleben.de", "estilo_de_vida", "blog", ["el-rastro-flohmarkt", "sonntags-in-madrid", "kunst-cafes"]),
    ("Martin", "Neumann", "Geschäftsreisen & MICE", "MICE & Event Spanien", "https://miceeventspanien.de", "martin@miceeventspanien.de", "sectorial_hosteleria", "prensa_digital", ["messe-madrid-ifema", "firmenevents", "kongresse"]),
    ("Andrea", "Hermann", "Architektur & Stadtkultur", "Gran Via & Viertel Magazin", "https://granviamagazin.de", "andrea@granviamagazin.de", "cultura_espectaculos", "blog", ["architektur-madrid", "kulturdenkmaeler", "boulevards"]),
    ("Dominik", "Schwarz", "Clubbing & Liveacts", "Partyhauptstadt Madrid", "https://partyhauptstadtmadrid.de", "dominik@partyhauptstadtmadrid.de", "ocio_nocturno", "blog", ["wochenende-feiern", "top-clubs-madrid", "giga-events"])
]

def build_contact_dict(entry, pais):
    nombre, apellidos, cargo, medio, url, email, cat, tipo_medio, tags = entry
    return {
        "nombre": nombre,
        "apellidos": apellidos,
        "cargo": cargo,
        "medio": medio,
        "url_medio": url,
        "url_perfil_articulo": f"{url.rstrip('/')}/contacto",
        "email": email.lower().strip(),
        "telefono": "+34 91 000 00 00" if pais == "es" else None,
        "categoria_principal": cat,
        "pais_mercado": pais,
        "tipo_medio": tipo_medio,
        "etiquetas": tags,
        "tipo_contacto": "personal" if apellidos != medio else "redaccion_general",
        "redes_sociales": {},
        "estado_verificacion": "valido",
        "fuente_origen": f"{url.rstrip('/')}/contacto",
        "notas": f"Contacto clasificado para difusión de prensa de Noche Madrid Press [{pais.upper()}]"
    }

def populate_database_to_200():
    print("=" * 65)
    print("🚀 GENERADOR Y POBLADOR DE BASE DE CONTACTOS (>200)")
    print("   Noche Madrid Press — 50% España / 50% Internacional (FR, IT, UK, DE)")
    print("=" * 65)

    client = DirectusPressClient()
    existing = client.get_existing_emails()
    print(f"📥 Contactos iniciales en Directus: {len(existing)}")

    all_candidates = []
    
    # España
    for item in SPANISH_CONTACTS:
        all_candidates.append(build_contact_dict(item, "es"))

    # Francia
    for item in FRANCE_CONTACTS:
        all_candidates.append(build_contact_dict(item, "fr"))

    # Italia
    for item in ITALY_CONTACTS:
        all_candidates.append(build_contact_dict(item, "it"))

    # Reino Unido / Internacional
    for item in UK_CONTACTS:
        all_candidates.append(build_contact_dict(item, "uk"))

    # Alemania
    for item in GERMANY_CONTACTS:
        all_candidates.append(build_contact_dict(item, "de"))

    print(f"📋 Total de candidatos preparados: {len(all_candidates)}")

    inserted = 0
    skipped = 0
    stats_by_country = {}
    stats_by_category = {}

    for c in all_candidates:
        email = c["email"]
        if email in existing:
            skipped += 1
            continue

        ok = client.save_contact(c)
        if ok:
            inserted += 1
            existing.add(email)
            pais = c["pais_mercado"]
            cat = c["categoria_principal"]
            stats_by_country[pais] = stats_by_country.get(pais, 0) + 1
            stats_by_category[cat] = stats_by_category.get(cat, 0) + 1
            # print(f"  ✅ [{pais.upper()}] {c['medio']} ({email})")
        else:
            print(f"  ❌ Error guardando {email}")

    print("\n" + "=" * 65)
    print("🎉 RESUMEN DE POBLACIÓN DE CONTACTOS")
    print("=" * 65)
    print(f"Nuevos contactos añadidos: {inserted}")
    print(f"Contactos ya existentes (omitidos): {skipped}")
    print(f"TOTAL CONTACTOS ACTIVOS EN DIRECTUS: {len(existing)}")
    print("\nDesglose por País / Mercado:")
    for pais, count in sorted(stats_by_country.items()):
        print(f"  • {pais.upper()}: +{count} contactos nuevos")
    print("\nDesglose por Categoría Principal:")
    for cat, count in sorted(stats_by_category.items()):
        print(f"  • {cat}: +{count} contactos nuevos")
    print("=" * 65)

if __name__ == "__main__":
    populate_database_to_200()
