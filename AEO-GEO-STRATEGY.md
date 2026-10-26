# Propuesta Estratégica: Optimización para Motores de Respuesta y Generativos (AEO / GEO) para Noche Madrid Press

A partir del análisis técnico de la plataforma actual y cruzando las directrices oficiales de **Cloudflare** *(Agent Readiness y consumo eficiente de agentes)*, **Google** *(E-E-A-T, grafos de entidades y Schema.org)* y **HubSpot** *(Search intent conversacional, pirámide invertida y citas autorizadas)*, presentamos la evaluación de situación y la propuesta de **máximo retorno con mínimo coste y complejidad**.

---

## 1. 🔍 Diagnóstico Actual de Noche Madrid Press

### Fortalezas Clave ya Conseguidas (La base está lista):
- **Arquitectura SSR ultrarrápida (Astro + Node):** No dependemos de hidratación pesada de JavaScript del lado del cliente (Client-Side Rendering). Los bots de IA reciben HTML estático puro de inmediato, reduciendo drásticamente los timeouts de los crawlers.
- **Lead Ejecutivo / TL;DR de 30 segundos:** Ya implementamos el bloque `ExecutiveBrief` con viñetas fácticas (`puntos_clave`), que es exactamente el tipo de resumen denso en información que los LLMs buscan para responder a preguntas directas.
- **Estructura Bilingüe Nativa (ES / EN):** Contenido indexable y traducido en ambas lenguas con URLs limpias.
- **Voces Oficiales y Citas:** Artículos vinculados a portavoces identificables (`Vicente Pizcueta`, `Ramón Mas`, `Marina Sanz`).

### Brechas Críticas Identificadas (Lo que nos hace invisibles hoy para los motores de IA):
1. **0% de Datos Estructurados (Schema.org / JSON-LD):** Actualmente no hay **ni una sola etiqueta JSON-LD** en el código. Para los bots de OpenAI, Perplexity o Google, una nota de prensa es texto plano genérico; no pueden discernir formalmente que se trata de un `NewsArticle` oficial emitido por una `NewsMediaOrganization` que representa a 96 `MusicVenue` en Madrid.
2. **Ausencia de `llms.txt`:** Cloudflare y los creadores de agentes recomiendan el nuevo estándar `/llms.txt` para que los LLMs entiendan la jerarquía del sitio en formato Markdown sin quemar tokens leyendo CSS, HTML y menús de navegación.
3. **Ausencia de `robots.txt` adaptado a IA:** No hay directivas explícitas de bienvenida y direccionamiento hacia el sitemap para bots como `GPTBot`, `PerplexityBot`, `ClaudeBot`, `Google-Extended` o `Applebot-Extended`.
4. **Falta de `sitemap.xml` dinámico:** Los motores de búsqueda y de respuesta no tienen un mapa centralizado donde descubrir los 29 comunicados en ambos idiomas con sus fechas de modificación.
5. **Etiquetas `hreflang` no inyectadas en el `<head>`:** Aunque calculamos internamente las URLs alternas en `Layout.astro`, no están emitidas como `<link rel="alternate" hreflang="es" ... />` en el HTML.

---

## 2. 🏛️ Los 3 Pilares Estratégicos (Cloudflare + Google + HubSpot)

```
                     ┌─────────────────────────────────────────────────┐
                     │           NOCHE MADRID PRESS (AEO / GEO)         │
                     └──────────────────────┬──────────────────────────┘
                                            │
         ┌──────────────────────────────────┼──────────────────────────────────┐
         ▼                                  ▼                                  ▼
 ┌──────────────────────┐        ┌──────────────────────┐        ┌──────────────────────┐
 │   1. CLOUDFLARE      │        │      2. GOOGLE       │        │     3. HUBSPOT       │
 │   Agent Readiness    │        │  Entidades y E-E-A-T │        │  Respuesta Inmediata │
 ├──────────────────────┤        ├──────────────────────┤        ├──────────────────────┤
 │ • /llms.txt estándar │        │ • JSON-LD Schema.org │        │ • TL;DR fáctico      │
 │ • robots.txt para IA │        │ • NewsArticle        │        │ • Encabezados Q&A    │
 │ • Versión .md limpia │        │ • MusicVenue (salas) │        │ • Citas de portavoces│
 │ • Latencia <200ms    │        │ • hreflang ES/EN     │        │ • Datos verificados  │
 └──────────────────────┘        └──────────────────────┘        └──────────────────────┘
```

### Pilar 1: Preparación para Agentes (Cloudflare "Agent Readiness")
Cloudflare subraya que los agentes de IA (Perplexity, SearchGPT, Claude) operan con ventanas de contexto limitadas y tiempos de espera agresivos (máximo 2 a 4 segundos por llamada):
- **`/llms.txt`:** Un archivo de texto plano en Markdown en la raíz del dominio que resume:
  - Qué es Noche Madrid Press (fuente oficial del ocio nocturno y la cultura de Madrid, gestionada por NocheMadrid).
  - Enlaces directos a las categorías principales, estadísticas clave y comunicados recientes.
- **Rutas Markdown para agentes (`Accept: text/markdown` o `/api/md/[slug]`):** Permitir que si un agente solicita el contenido, pueda obtener la nota en Markdown puro en <50ms y con 80% menos tokens, priorizando a MadridLivePress frente a medios saturados de banners o muros de pago.
- **Permisividad controlada en `robots.txt`:** Asegurar que los bots de recuperación generativa tengan vía libre hacia el contenido público.

### Pilar 2: Autoridad de Entidad y E-E-A-T (Google AI Optimization)
Google no resume lo que no comprende con certeza matemática. Para que Google AI Overviews cite a Noche Madrid Press, necesita reconocer entidades en su grafo de conocimiento:
- **`NewsArticle` Schema:** Incluyendo `headline`, `description`, `datePublished`, `dateModified`, `author` (`Person` o `Organization`), `publisher` (NocheMadrid), e `image`.
- **`MusicVenue` / `LocalBusiness` Schema:** En el Directorio (`/directorio/[slug]`), marcar cada una de las 96 salas con su aforo, distrito, coordenadas y entidad asociada. Cuando un usuario pregunte a un LLM «*¿Cuáles son las salas de música en vivo del centro de Madrid con aforo de más de 500 personas?*», el modelo consultará directamente esta estructura.
- **`NewsMediaOrganization`:** Marcar la organización con enlaces `sameAs` a Wikipedia, NocheMadrid, federaciones institucionales y redes verificadas para transferir autoridad de dominio.

### Pilar 3: Estructura de Respuesta Directa (HubSpot AEO/GEO)
Los usuarios ya no buscan palabras clave como «salas madrid», sino preguntas conversacionales completas como «*¿Qué medidas aplican las discotecas de Madrid contra el ruido nocturno?*».
- **Formato Pregunta-Respuesta:** Titular o subtítulo en formato pregunta (`H2`), seguido inmediatamente por un párrafo de **40 a 60 palabras con respuesta directa e inequívoca**, y luego el desglose de datos y citas.
- **Citas con Atribución Explícita:** Los LLMs extraen declaraciones directas con el formato: *«[Declaración textual], ha afirmado [Nombre], [Cargo] de [Organización]»*.
- **Cifras y Datos Originales:** Como el estudio de MasMétrica y Bolt que acabas de publicar: las IAs aman las cifras exclusivas (*«92 % de los españoles»*, *«71 % de usuarios»*). Si el dato está estructurado, el motor generativo lo cita textualmente como fuente primaria.

---

## 3. 🎯 Plan de Acción Recomendado (Matriz de Bajo Coste y Alto Impacto)

Para cumplir con tu premisa de **bajo coste y complejidad**, clasificamos las acciones en 3 fases:

| Acción | Impacto AEO/GEO | Complejidad | Coste | Tiempo estimado |
| :--- | :---: | :---: | :---: | :---: |
| **1. Inyectar JSON-LD (`NewsArticle` y `Organization`)** | **Máximo (10/10)** | Muy Baja | 0 € | ~2 horas |
| **2. Crear `/llms.txt` y `robots.txt` para IA** | **Alto (9/10)** | Mínima | 0 € | ~30 min |
| **3. Generador dinámico de `sitemap.xml` bilingüe** | **Alto (8.5/10)** | Muy Baja | 0 € | ~1 hora |
| **4. Inyectar etiquetas `hreflang` en el `<head>`** | **Medio-Alto (8/10)** | Mínima | 0 € | ~20 min |
| **5. Endpoint Markdown para agentes (`/news/[slug].md`)** | **Alto (8.5/10)** | Baja | 0 € | ~1 hora |
| **6. Bloque FAQ / Q&A con Schema en páginas clave** | **Medio (7.5/10)** | Baja | 0 € | ~1.5 horas |

---

## 4. 🛠️ Detalle de las Acciones Concretas a Implementar

### Fase 1: Fundaciones Técnicas (Inmediato - 0 coste)

1. **Datos Estructurados Schema.org Automatizados:**
   - Crear un componente `JsonLdArticle.astro` que se incluya automáticamente en `src/pages/comunicados/[slug].astro` y `src/pages/en/news/[slug].astro`.
   - Se alimenta directamente de los campos que ya existen en Directus (`titulo`, `bajada`, `fecha_publicacion`, `portavoz`, `imagen_portada`, `puntos_clave`).
   - Crear `JsonLdOrganization.astro` en la portada y páginas corporativas vinculando formalmente a *Noche Madrid Press* con *NocheMadrid*.

2. **Creación de `/llms.txt` (Estándar Cloudflare/AI):**
   - Archivo en `public/llms.txt` con la descripción ejecutiva de la plataforma, el catálogo de temas cubiertos y los enlaces canónicos para consumo por agentes.

3. **Optimización de `robots.txt` para Bots de IA:**
   - Permitir explícitamente y priorizar a:
     ```txt
     User-agent: GPTBot
     User-agent: PerplexityBot
     User-agent: ClaudeBot
     User-agent: Google-Extended
     User-agent: Applebot-Extended
     Allow: /
     Sitemap: https://madridlivepress.116.203.118.1.sslip.io/sitemap.xml
     ```

4. **Sitemap Dinámico con URLs en Español e Inglés:**
   - Un endpoint en `src/pages/sitemap.xml.ts` que consulte Directus y emita un XML estándar con todas las páginas, comunicados, fichas del directorio y sus correspondientes enlaces `xhtml:link rel="alternate"` de idioma.

5. **Activación de `hreflang` en `Layout.astro`:**
   - Añadir en el `<head>`:
     ```html
     <link rel="alternate" hreflang="es" href={urlEs} />
     <link rel="alternate" hreflang="en" href={urlEn} />
     <link rel="alternate" hreflang="x-default" href={urlEs} />
     ```

---

### Fase 2: Optimización Editorial (Metodología de Redacción)

Sin tocar código, simplemente aplicando estas pautas al subir notas en Directus:
1. **El primer párrafo responde al «Qué, Quién, Cuándo y Por qué» sin preámbulos:** Los LLMs recortan los primeros 250 tokens para generar respuestas rápidas.
2. **Uso de subtítulos en forma de pregunta:**
   - En lugar de *«Resultados del sondeo sobre transporte nocturno»*, titular la sección como:
     *«¿Por qué el 92 % de los usuarios eligen aplicaciones de movilidad de noche?»*.
   - Esto hace match exacto con el prompt del usuario en ChatGPT o Perplexity.
3. **Mantener siempre los Puntos Clave (`puntos_clave`):** La IA los lee como viñetas de alta fiabilidad fáctica para crear listas en sus respuestas generativas.

---

## 5. 💡 Conclusión y Recomendación

Noche Madrid Press ya tiene el **80% del trabajo pesado hecho** gracias a su arquitectura limpia, rápida y bilingüe. 

Lo único que le falta para dominar en los motores de búsqueda generativa es **el puente semántico**:
1. Decirle formalmente a las IAs qué es cada elemento mediante **JSON-LD**.
2. Decirle a los agentes cómo indexar el contenido mediante **`llms.txt`**, **`robots.txt`** y **`sitemap.xml`**.

Todo esto se puede implementar **sin coste adicional**, en **menos de una jornada de trabajo** y sin añadir librerías pesadas ni alterar el diseño visual que acabamos de pulir.

Cuando quieras que avancemos con esto, podemos planificar la Fase 1 paso a paso.
