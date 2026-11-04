"""
Descarga las 3 fotos (licencia Unsplash, uso libre) a mascotas/static/mascotas/img/
Ejecutar UNA vez, con internet:   python descargar_fotos.py
"""
import os
import urllib.request

FOTOS = {
    'perro.jpg':    ('1601543574606-1d8a714787f9', 1400),   # Sander Mathlener
    'gato.jpg':     ('1530153892876-56d69b38e5c1', 800),    # Jason Leung
    'cachorro.jpg': ('1565366665956-2b7500a3f901', 800),    # Tamás Tokos
}
DESTINO = os.path.join('mascotas', 'static', 'mascotas', 'img')
os.makedirs(DESTINO, exist_ok=True)

for nombre, (foto_id, ancho) in FOTOS.items():
    url = f'https://images.unsplash.com/photo-{foto_id}?auto=format&fit=crop&w={ancho}&q=70'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r, open(os.path.join(DESTINO, nombre), 'wb') as f:
            f.write(r.read())
        print('Descargada:', nombre)
    except Exception as e:
        print('ERROR con', nombre, '->', e)
print('Listo. Reinicia el servidor y recarga con Ctrl+F5.')
