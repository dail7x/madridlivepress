import os
import math
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = '/System/Library/Fonts/HelveticaNeue.ttc'

def draw_monogram(draw, x, y, scale=1.0):
    """Draws the geometric N monogram with red live dot from favicon.svg"""
    s = scale
    # Left pillar
    draw.rounded_rectangle([x + 25*s, y + 26*s, x + 35*s, y + 74*s], radius=2*s, fill=(250, 250, 250, 255))
    # Diagonal beam
    draw.polygon([
        (x + 25*s, y + 26*s),
        (x + 35*s, y + 26*s),
        (x + 75*s, y + 74*s),
        (x + 65*s, y + 74*s)
    ], fill=(250, 250, 250, 255))
    # Right pillar
    draw.rounded_rectangle([x + 65*s, y + 26*s, x + 75*s, y + 74*s], radius=2*s, fill=(250, 250, 250, 255))
    # Outer red pulse glow
    draw.ellipse([x + 68*s, y + 11*s, x + 90*s, y + 33*s], fill=(225, 29, 72, 90))
    # Live signal dot (Vermilion #E11D48)
    draw.ellipse([x + 72*s, y + 15*s, x + 86*s, y + 29*s], fill=(225, 29, 72, 255))

def create_smooth_mask(width, height, fade_start=420, fade_end=880):
    """Generates an ultra-smooth vignette mask in mode 'L'"""
    mask = Image.new('L', (width, height))
    mask_pixels = mask.load()
    
    for y in range(height):
        # Vertical attenuation near bottom for metadata readability
        if y > 490:
            y_factor = 1.0 - 0.75 * ((y - 490) / (height - 490))
        elif y < 130:
            y_factor = 0.88 + 0.12 * (y / 130)
        else:
            y_factor = 1.0

        for x in range(width):
            if x < fade_start:
                base_val = 0
            elif x < fade_end:
                t = (x - fade_start) / (fade_end - fade_start)
                base_val = (1 - math.cos(t * math.pi)) / 2 * 235
            else:
                base_val = 235
            
            final_val = int(base_val * y_factor)
            mask_pixels[x, y] = max(0, min(255, final_val))
            
    return mask

def create_og_image(base_img_path, output_png_path, output_jpg_path, config):
    width, height = 1200, 630
    
    # Solid deep charcoal background (#08090D)
    dark_bg = Image.new('RGBA', (width, height), (8, 9, 13, 255))

    # Load and scale photo
    base_img = Image.open(base_img_path).convert('RGBA')
    img_w, img_h = base_img.size
    
    # Scale to cover height 630
    scale = height / img_h
    new_w = int(img_w * scale)
    new_h = height
    if new_w < width:
        # Scale to cover width if too narrow
        scale = width / img_w
        new_w = width
        new_h = int(img_h * scale)
        
    resized_photo = base_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create canvas for photo shifted to the right
    photo_canvas = Image.new('RGBA', (width, height), (8, 9, 13, 255))
    paste_x = width - new_w + config.get('offset_x', 0)
    paste_y = (height - new_h) // 2
    photo_canvas.paste(resized_photo, (paste_x, paste_y))

    # Mask blending
    fade_start = config.get('fade_start', 420)
    fade_end = config.get('fade_end', 880)
    mask = create_smooth_mask(width, height, fade_start, fade_end)
    composite = Image.composite(photo_canvas, dark_bg, mask)

    # Drawing layer for text & vector elements
    vector_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(vector_layer)

    # 1. Subtle Outer Frame & Swiss Grid
    border_color = (255, 255, 255, 35)
    grid_color = (255, 255, 255, 14)
    
    draw.rectangle([28, 28, width - 28, height - 28], outline=border_color, width=1)
    draw.line([(80, 28), (80, height - 28)], fill=grid_color, width=1)
    draw.line([(80, 528), (width - 80, 528)], fill=border_color, width=1)

    # 2. Typography
    font_badge = ImageFont.truetype(FONT_PATH, 15, index=1)
    font_brand = ImageFont.truetype(FONT_PATH, 20, index=1)
    font_brand_sub = ImageFont.truetype(FONT_PATH, 13, index=0)
    font_desc = ImageFont.truetype(FONT_PATH, 21, index=0)
    font_meta = ImageFont.truetype(FONT_PATH, 13, index=1)
    font_url = ImageFont.truetype(FONT_PATH, 14, index=1)

    # 3. Top Header: Monogram + Brand
    draw_monogram(draw, 100, 56, scale=0.72)
    draw.text((185, 70), "NOCHE MADRID PRESS", font=font_brand, fill=(255, 255, 255, 255))
    draw.text((185, 96), "SALA DE PRENSA OFICIAL · GABINETE DE MEDIOS", font=font_brand_sub, fill=(161, 161, 170, 230))

    # 4. Live Badge Pill
    badge_x = 105
    badge_y = 152
    badge_text = config['badge'].upper()
    bbox = font_badge.getbbox(badge_text)
    badge_w = (bbox[2] - bbox[0]) + 44
    badge_h = 32

    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=16, fill=(225, 29, 72, 45), outline=(225, 29, 72, 220), width=1)
    draw.ellipse([badge_x + 12, badge_y + 11, badge_x + 22, badge_y + 21], fill=(225, 29, 72, 255))
    draw.text((badge_x + 29, badge_y + 7), badge_text, font=font_badge, fill=(255, 255, 255, 255))

    # 5. Main Title & Description Handling
    is_hero_title = config.get('hero_title_only', False)

    if is_hero_title:
        # Extra large title, NO subtitle (specifically requested for NOTAS DE PRENSA)
        font_hero_title = ImageFont.truetype(FONT_PATH, 66, index=1)
        draw.text((105, 235), config['title'], font=font_hero_title, fill=(255, 255, 255, 255))
    else:
        font_bold_title = ImageFont.truetype(FONT_PATH, 54, index=1)
        title = config['title']
        title_y = 206
        lines = []
        words = title.split(' ')
        current_line = ""
        for w in words:
            test_line = f"{current_line} {w}".strip()
            bbox = font_bold_title.getbbox(test_line)
            if bbox[2] - bbox[0] > 600:
                lines.append(current_line)
                current_line = w
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line)

        for line in lines[:2]:
            draw.text((105, title_y), line, font=font_bold_title, fill=(255, 255, 255, 255))
            title_y += 62

        # Subtitle / Description
        desc = config.get('desc', '')
        if desc:
            desc_y = title_y + 16
            desc_lines = []
            desc_words = desc.split(' ')
            curr_desc = ""
            for dw in desc_words:
                test_desc = f"{curr_desc} {dw}".strip()
                bbox = font_desc.getbbox(test_desc)
                if bbox[2] - bbox[0] > 560:
                    desc_lines.append(curr_desc)
                    curr_desc = dw
                else:
                    curr_desc = test_desc
            if curr_desc:
                desc_lines.append(curr_desc)

            for dline in desc_lines[:2]:
                draw.text((105, desc_y), dline, font=font_desc, fill=(212, 212, 216, 240))
                desc_y += 32

    # 6. Bottom Metadata & Domain
    footer_y = 554
    meta_tag = config['meta'].upper()
    draw.text((105, footer_y + 4), meta_tag, font=font_meta, fill=(161, 161, 170, 240))

    # Website domain pill
    site_domain = "nochemadridpress.com"
    site_bbox = font_url.getbbox(site_domain)
    site_w = site_bbox[2] - site_bbox[0] + 32
    site_h = 30
    site_x = width - 85 - site_w
    site_y = footer_y - 2

    draw.rounded_rectangle([site_x, site_y, site_x + site_w, site_y + site_h], radius=6, fill=(20, 22, 30, 220), outline=(255, 255, 255, 60), width=1)
    draw.text((site_x + 16, site_y + 6), site_domain, font=font_url, fill=(255, 255, 255, 255))

    # Final composite
    final_rgba = Image.alpha_composite(composite, vector_layer)
    final_rgb = final_rgba.convert('RGB')
    
    # Save PNG & optimized JPG
    final_rgb.save(output_png_path, format='PNG', optimize=True)
    final_rgb.save(output_jpg_path, format='JPEG', quality=93, optimize=True)
    print(f"Generated: {output_png_path} ({os.path.getsize(output_png_path)} bytes)")
    print(f"Generated: {output_jpg_path} ({os.path.getsize(output_jpg_path)} bytes)")

configs = [
    {
        # Image 1: Authentic Madrid Gran Vía / Plaza Callao / Edificio Carrión with Schweppes neon and crowds
        'base': '/Users/dailmarin/.gemini/antigravity-ide/brain/e849b870-1612-4d69-a061-c4d491ec3ae1/madrid_granvia_night_1793056594029.jpg',
        'png': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-main.png',
        'jpg': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-main.jpg',
        'badge': 'SALA DE PRENSA OFICIAL · LIVE',
        'title': 'NOCHE MADRID PRESS',
        'desc': 'Sala de prensa virtual internacional de la noche, el ocio cultural y los espacios asociados de Madrid.',
        'meta': 'RED OFICIAL DE OCIO Y CULTURA · GABINETE OFICIAL DE COMUNICACIÓN',
        'fade_start': 380,
        'fade_end': 860,
        'offset_x': 0
    },
    {
        # Image 2: Authentic press microphones lined up on press desk, NO people, NO subtitle, ONLY "NOTAS DE PRENSA"
        'base': '/Users/dailmarin/.gemini/antigravity-ide/brain/e849b870-1612-4d69-a061-c4d491ec3ae1/press_microphones_table_1793056637033.jpg',
        'png': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-comunicados.png',
        'jpg': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-comunicados.jpg',
        'badge': 'COMUNICADOS OFICIALES',
        'title': 'NOTAS DE PRENSA',
        'hero_title_only': True,
        'meta': 'GABINETE DE PRENSA · ARCHIVO MULTIMEDIA · LIBRE USO EDITORIAL',
        'fade_start': 480,
        'fade_end': 900,
        'offset_x': 50
    },
    {
        # Image 3: Majestic Madrid concert hall/theatre, NO "96 salas" anywhere
        'base': '/Users/dailmarin/.gemini/antigravity-ide/brain/e849b870-1612-4d69-a061-c4d491ec3ae1/noche_madrid_venues_1793055483338.jpg',
        'png': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-directorio.png',
        'jpg': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-directorio.jpg',
        'badge': 'DIRECTORIO OFICIAL DE ESPACIOS',
        'title': 'RED DE ESPACIOS ASOCIADOS',
        'desc': 'Salas de conciertos, teatros musicales y discotecas de Madrid. Fichas técnicas, aforos y contactos de prensa.',
        'meta': 'FICHAS TÉCNICAS · AFOROS VERIFICADOS · CONTACTOS DE PRENSA',
        'fade_start': 380,
        'fade_end': 860,
        'offset_x': 0
    },
    {
        # Image 4: Authentic Spanish Noche Madrid Sala de Prensa Accreditation Pass, reporter gear and lanyard
        'base': '/Users/dailmarin/.gemini/antigravity-ide/brain/e849b870-1612-4d69-a061-c4d491ec3ae1/noche_madrid_acreditacion_1793056662396.jpg',
        'png': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-recursos.png',
        'jpg': '/Users/dailmarin/Developer/madridlivepress/public/images/og/og-recursos.jpg',
        'badge': 'ACREDITACIONES & RECURSOS',
        'title': 'RECURSOS Y ACREDITACIONES',
        'desc': 'Pases de prensa profesional, dossiers de investigación, B-roll en 4K y banco de imágenes oficial para medios.',
        'meta': 'ACCESO PROFESIONAL · DERECHOS EDITORIALES · MEDIA CRM',
        'fade_start': 520,
        'fade_end': 950,
        'offset_x': 200
    }
]

for cfg in configs:
    create_og_image(cfg['base'], cfg['png'], cfg['jpg'], cfg)
