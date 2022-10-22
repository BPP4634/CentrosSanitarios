from collections import namedtuple
from math import sin, cos, sqrt, atan2, radians
from math import sqrt

Coordenada = namedtuple('Coordenada', 'latitud, longitud')

def lee_coordenadas(archivo):
    coordenadas = []
    with open(archivo, encoding='utf-8') as f:
        next(f)
        for linea in f:
            linea = linea.split(";")
            latitud = float(linea[2])
            longitud = float(linea[3])
            coordenada = Coordenada(latitud,longitud)
            coordenadas.append(coordenada)
        return coordenadas

def calcular_distancia(cor1,cor2):
    return sqrt(abs((cor2.latitud-cor1.latitud)/(cor2.longitud-cor1.longitud)))

def calcular_media_coordenadas(coordenadas):
    latitudes = []
    longitudes = []
    for coordenada in coordenadas:
        latitudes.append(coordenada.latitud)
        longitudes.append(coordenada.longitud)
    return Coordenada(sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes))

def distancia_harvesine(coord_a, coord_b):
    radio_tierra = 6373.0
    latitud_a, longitud_a = radians(coord_a.latitud), radians(coord_a.longitud)
    latitud_b, longitud_b = radians(coord_b.latitud), radians(coord_b.longitud)    
    inc_lat  = latitud_b - latitud_a
    inc_long = longitud_b - longitud_a
    a = sin(inc_lat / 2)**2 + cos(latitud_a) * cos(latitud_b) * sin(inc_long / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radio_tierra * c