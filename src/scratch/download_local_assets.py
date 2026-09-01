import urllib.request
import os

news_dir = '/Users/dailmarin/Developer/madridlivepress/public/images/news'
press_dir = '/Users/dailmarin/Developer/madridlivepress/public/images/press'
os.makedirs(news_dir, exist_ok=True)
os.makedirs(press_dir, exist_ok=True)

# Curated high-resolution editorial nightlife, concert, theatre and press images
news_images = {
    'dos-millones-turistas.jpg': 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?q=80&w=1200&auto=format&fit=crop',
    'tardeo-madrid.jpg': 'https://images.unsplash.com/photo-1517457373958-b7bdd4587205?q=80&w=1200&auto=format&fit=crop',
    'mado-orgullo.jpg': 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?q=80&w=1200&auto=format&fit=crop',
    'bad-bunny-residencia.jpg': 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=1200&auto=format&fit=crop',
    'imex-frankfurt.jpg': 'https://images.unsplash.com/photo-1511578314322-379afb476865?q=80&w=1200&auto=format&fit=crop',
    'enlacolasilencio.jpg': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?q=80&w=1200&auto=format&fit=crop',
    'alejandro-zamarro.jpg': 'https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?q=80&w=1200&auto=format&fit=crop',
    'denuncias-ruido.jpg': 'https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?q=80&w=1200&auto=format&fit=crop',
    'impacto-economico.jpg': 'https://images.unsplash.com/photo-1585829365295-ab7cd400c167?q=80&w=1200&auto=format&fit=crop',
    'conciertos-otono.jpg': 'https://images.unsplash.com/photo-1516307365426-bea591f05011?q=80&w=1200&auto=format&fit=crop',
    'residencias-artisticas.jpg': 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=1200&auto=format&fit=crop',
    'controladores-acceso.jpg': 'https://images.unsplash.com/photo-1574391884720-bbc3740c59d1?q=80&w=1200&auto=format&fit=crop',
}

press_images = {
    'abc-clipping.jpg': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?q=80&w=800&auto=format&fit=crop',
    'elmundo-clipping.jpg': 'https://images.unsplash.com/photo-1585829365295-ab7cd400c167?q=80&w=800&auto=format&fit=crop',
    'hosteltur-clipping.jpg': 'https://images.unsplash.com/photo-1511578314322-379afb476865?q=80&w=800&auto=format&fit=crop',
    'telemadrid-clipping.jpg': 'https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?q=80&w=800&auto=format&fit=crop',
    'cadenaser-clipping.jpg': 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?q=80&w=800&auto=format&fit=crop',
    'europapress-clipping.jpg': 'https://images.unsplash.com/photo-1495020689067-958852a7765e?q=80&w=800&auto=format&fit=crop',
}

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in news_images.items():
    filepath = os.path.join(news_dir, name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as out:
            out.write(resp.read())
        print(f'Saved news image: {name}')
    except Exception as e:
        print(f'Error downloading {name}:', e)

for name, url in press_images.items():
    filepath = os.path.join(press_dir, name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(filepath, 'wb') as out:
            out.write(resp.read())
        print(f'Saved press image: {name}')
    except Exception as e:
        print(f'Error downloading {name}:', e)

print('Local image assets created successfully.')
