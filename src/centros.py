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
'''leer_centros: recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve una lista de tuplas de
tipo CentroSanitario(str, str, Coordenada(float, float), str, int, bool, bool) conteniendo todos los datos
almacenados en el fichero. Note que, aunque en el fichero la latitud y la longitud se almacenan de
forma independiente, en la lista resultado deben almacenarse como una Coordenada(float, float).
2. calcular_total_camas_centros_accesibles: recibe una lista de tuplas de tipo CentroSanitario, y
produce como salida un entero correspondiente al número total de camas de los centros sanitarios
accesibles para discapacitados.
3. obtener_centros_con_uci_cercanos_a: recibe una lista de tuplas de tipo CentroSanitario, una tupla
de tipo Coordenada que representa un punto, y un float que representa un umbral de distancia, y
produce como salida una lista de tuplas (str, str, Coordenada(float, float)) con el nombre, la localidad
y las coordenadas de los centros situados a una distancia de las coordenadas dadas como parámetro
menor o igual que el umbral dado. Observe la Figura 3 para entender mejor el resultado de la función.
Figura 3: Radio de centros con UCI buscados
'''