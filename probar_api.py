"""
Script para demostrar la API REST (sin instalar nada extra).

Uso (con el servidor corriendo en otra consola):
    python probar_api.py TU_USUARIO TU_CONTRASENA
"""
import json
import sys
import urllib.request
import urllib.error

BASE = 'http://127.0.0.1:8000/api'


def llamar(metodo, ruta, datos=None, token=None):
    cuerpo = json.dumps(datos).encode() if datos is not None else None
    req = urllib.request.Request(BASE + ruta, data=cuerpo, method=metodo)
    req.add_header('Content-Type', 'application/json')
    if token:
        req.add_header('Authorization', 'Token ' + token)   # así se envía el token
    try:
        with urllib.request.urlopen(req) as r:
            texto = r.read().decode()
            return r.status, json.loads(texto) if texto else ''
    except urllib.error.HTTPError as e:
        texto = e.read().decode()
        return e.code, json.loads(texto) if texto else ''


def mostrar(titulo, resultado):
    estado, datos = resultado
    print('\n>>', titulo)
    print('   Estado HTTP:', estado)
    print('   Respuesta  :', datos)


if len(sys.argv) != 3:
    print('Uso: python probar_api.py USUARIO CONTRASENA')
    sys.exit(1)

usuario, clave = sys.argv[1], sys.argv[2]

mostrar('GET sin token (debe dar 401)', llamar('GET', '/mascotas/'))
mostrar('GET con token inválido (debe dar 401)', llamar('GET', '/mascotas/', token='abc123'))
mostrar('Login con clave incorrecta (debe dar 400)', llamar('POST', '/login/', {'username': usuario, 'password': 'mala'}))

estado, datos = llamar('POST', '/login/', {'username': usuario, 'password': clave})
mostrar('Login correcto (entrega el token)', (estado, datos))
if estado != 200:
    sys.exit('No se pudo iniciar sesión, revisa usuario y contraseña.')
token = datos['token']

mascota = {'nombre': 'Firulais', 'especie': 'Perro', 'raza': 'Poodle', 'edad': 3, 'peso': '8.5',
           'nombre_dueno': 'Juan Pérez', 'telefono_dueno': '912345678', 'observaciones': 'Vacunas al día'}

mostrar('POST con datos inválidos (debe dar 400)',
        llamar('POST', '/mascotas/', {**mascota, 'nombre': 'A', 'edad': 99, 'telefono_dueno': 'abc'}, token))
estado, creada = llamar('POST', '/mascotas/', mascota, token)
mostrar('POST crear mascota (debe dar 201)', (estado, creada))
id_nuevo = creada['id']

mostrar('GET listar mascotas (200)', llamar('GET', '/mascotas/', token=token))
mostrar('GET una mascota por id (200)', llamar('GET', '/mascotas/%d/' % id_nuevo, token=token))
mostrar('GET id inexistente (debe dar 404)', llamar('GET', '/mascotas/99999/', token=token))

mostrar('PUT actualizar mascota (200)',
        llamar('PUT', '/mascotas/%d/' % id_nuevo, {**mascota, 'nombre': 'Firu', 'edad': 4}, token))
mostrar('PUT con datos inválidos (400)',
        llamar('PUT', '/mascotas/%d/' % id_nuevo, {**mascota, 'peso': '0'}, token))

input('\nRevisa en phpMyAdmin que la mascota existe y presiona ENTER para eliminarla...')
mostrar('DELETE eliminar mascota (204)', llamar('DELETE', '/mascotas/%d/' % id_nuevo, token=token))
mostrar('DELETE otra vez (debe dar 404)', llamar('DELETE', '/mascotas/%d/' % id_nuevo, token=token))
