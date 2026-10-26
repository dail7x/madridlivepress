# Sistema de Bots de Prospección y Segmentación de Prensa — Noche Madrid Press

Sistema automatizado para rastrear, extraer, validar, segmentar y sincronizar contactos de prensa, medios digitales especializados, blogs independientes, vloggers y creadores de contenido (nacionales e internacionales) en **Directus** y con exportación directa a **CSV para difusión (Brevo, Mailchimp, etc.)**.

---

## 1. Estructura de Segmentación

Los contactos se clasifican en **Directus** en la colección `contactos_prensa` mediante dos ejes principales:

### A. Categoría Temática (`categoria_principal`)
* `ocio_nocturno`: Discotecas, salas de fiesta, música electrónica, festivales, clubes, tardeo.
* `gastronomia`: Restaurantes, bares de copas, coctelerías, sumillería, tapas, foodies.
* `turismo`: Portales turísticos, escapadas urbanas, hoteles, viajes a Madrid.
* `cultura_espectaculos`: Cartelera teatral, musicales, artes escénicas, conciertos, exposiciones.
* `estilo_de_vida`: Lifestyle, moda, planes originales, terrazas, tendencias urbanas.
* `sectorial_hosteleria`: Revistas B2B, patronales, proveedores Horeca, empresas de ocio.
* `generalista_madrid`: Secciones de Madrid y Sociedad en diarios y agencias de noticias.

### B. País y Mercado Objetivo (`pais_mercado`)
* `es`: España (Madrid / Nacional)
* `fr`: Francia (Mercado francófono: Le Petit Journal Madrid, Madrid Pour Les Français, Courrier d'Espagne...)
* `it`: Italia (Mercado italiano: Vivere a Madrid, Destinazione Madrid...)
* `uk`: Reino Unido / Internacional en inglés (Naked Madrid, Citylife Madrid, Madrid No Frills, Devour Madrid...)
* `de`: Alemania / DACH (Madrid Mal Anders, Spanien Reisemagazin...)

### C. Tipo de Medio (`tipo_medio`)
* `blog`: Blogs especializados independientes (ej. Madrid Cool Blog, Naked Madrid, Madrid Diferente).
* `creador_vlogger`: Creadores de contenido, vloggers gastronómicos y curadores de planes (ej. Con El Morro Fino, Madrid Low Cost, Citylife).
* `portal_turismo`: Guías de viajes y escapadas (ej. Destinazione Madrid, Devour Madrid).
* `prensa_digital`: Revistas y diarios digitales especializados.

---

## 2. Ejecución de los Bots

### Requisitos previos
El entorno virtual se encuentra en la raíz del proyecto `.venv`:
```bash
source .venv/bin/activate
```

### Ejecutar prospección bajo demanda
```bash
# Prospectar todos los medios y blogs configurados
python src/bots/run_bots.py

# Filtrar por mercado internacional (ej. solo Francia, Reino Unido o Italia)
python src/bots/run_bots.py --mercado fr
python src/bots/run_bots.py --mercado uk
python src/bots/run_bots.py --mercado it

# Filtrar por categoría temática
python src/bots/run_bots.py --categoria ocio_nocturno
python src/bots/run_bots.py --categoria gastronomia

# Filtrar solo blogs independientes o creadores
python src/bots/run_bots.py --tipo-medio blog
python src/bots/run_bots.py --tipo-medio creador_vlogger

# Modo simulación (Dry Run, no guarda en Directus)
python src/bots/run_bots.py --dry-run
```

---

## 3. Exportación a CSV para Campañas (Brevo / Mailchimp)

El script `export_press_list.py` descarga los contactos filtrados desde Directus y genera archivos CSV con codificación UTF-8 con BOM (compatible con Excel y plataformas de email marketing):

```bash
# Exportar TODOS los contactos
python src/bots/export_press_list.py

# Exportar solo contactos de un mercado específico (ej. Reino Unido)
python src/bots/export_press_list.py --mercado uk

# Exportar solo contactos de Francia
python src/bots/export_press_list.py --mercado fr

# Exportar solo una categoría temática (ej. Ocio Nocturno)
python src/bots/export_press_list.py --categoria ocio_nocturno

# Exportar por tipo de medio (ej. solo creadores de contenido)
python src/bots/export_press_list.py --tipo-medio creador_vlogger
```

Los archivos se guardan en la carpeta `src/bots/exports/` con nombres como:
`contactos_prensa_uk_20261026_224656.csv`

---

## 4. Configurar el Cron en el Servidor (Automático)

Para que el servidor ejecute automáticamente la prospección de forma periódica:

1. El script ejecutable está en: `src/bots/cron_runner.sh`.
2. En el servidor donde está alojado el proyecto o Directus, edita el crontab:
   ```bash
   crontab -e
   ```
3. Añade la siguiente línea para ejecutarlo todos los lunes a las 06:00 AM:
   ```cron
   0 6 * * 1 /ruta/al/proyecto/src/bots/cron_runner.sh
   ```
4. Los registros de cada ejecución se guardarán en `src/bots/cron.log`.
