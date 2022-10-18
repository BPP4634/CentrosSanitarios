from collections import namedtuple
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


'''2. calcular_media_coordenadas: recibe una lista de Coordenada(float, float), y devuelve una
Coordenada(float, float) cuya latitud es la media de las latitudes de la lista y cuya longitud es la media
de las longitudes de la lista.'''