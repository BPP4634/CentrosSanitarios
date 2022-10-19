from collections import namedtuple
from coordenadas import *

CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenada, estado, num_camas, acceso_minusvalidos, tiene_uci')

def lee_datos(archivo):
    centros = []
    with open(archivo, encoding='utf-8') as f:
        next(f)
        for linea in f:
            linea = linea.split(";")
            nombre = linea[0]
            localidad = linea[1]
            coordenada = Coordenada(float(linea[2]),float(linea[3]))
            estado = linea[4]
            num_camas = int(linea[5])
            acceso_minusvalidos = bool(linea[6])
            tiene_uci = bool(linea[7])
            centros.append(CentroSanitario(nombre, localidad, coordenada, estado, num_camas, acceso_minusvalidos, tiene_uci))
        return centros

def calcular_total_camas_centros_accesibles(centros):
    camas = []
    for centro in centros:
        if centro.acceso_minusvalidos == True:
            camas.append(centro.num_camas)
    return sum(camas)

def obtener_centros_con_uci_cercanos_a(centros, coor,n):
    centroscerca = []
    for centro in centros:
        if calcular_distancia(centro.coordenada, coor) <=n:
            centroscerca.append((centro.nombre,centro.localidad,centro.coordenada))
    return centroscerca