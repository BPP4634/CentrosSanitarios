from collections import namedtuple
from coordenadas import *
from mapas import *

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

def obtener_centros_con_uci_cercanos_a_haversine(centros, coor,n):
    centroscerca = []
    for centro in centros:
        if distancia_harvesine(centro.coordenada, coor) <=n:
            centroscerca.append((centro.nombre,centro.localidad,centro.coordenada))
    return centroscerca

def generar_mapa(centros):
    coor = []
    for centro in centros:
        coor.append(centro[2])
    print(coor)
    media = calcular_media_coordenadas(coor)
    mapa = crea_mapa(media.latitud,media.longitud)
    for centro in centros:
        marcador = crea_marcador(centro[2].latitud,centro[2].longitud,centro[0])
        marcador.add_to(mapa)
    mapa.save('./out/mapa.html')

def obtener_centros_con_uci_cercanos_a_haversine(centros, coor,n):
    centroscerca = []
    for centro in centros:
        if distancia_harvesine(centro.coordenada, coor) <=n:
            centroscerca.append((centro.nombre,centro.localidad,centro.coordenada))
    return centroscerca

def generar_mapa_haversine(centros):
    coor = []
    for centro in centros:
        coor.append(centro[2])
    print(coor)
    media = calcular_media_coordenadas(coor)
    mapa = crea_mapa(media.latitud,media.longitud)
    for centro in centros:
        marcador = crea_marcador(centro[2].latitud,centro[2].longitud,centro[0])
        marcador.add_to(mapa)
    mapa.save('./out/mapa_haversine.html')

'''4. generar_mapa: recibe una lista de tuplas (str, str, Coordenada(float, float)) con el nombre, la
localidad y las coordenadas de los centros, y una cadena que representa la ruta de un fichero html,
y genera y graba en este fichero un mapa con los centros geolocalizados.
Para implementar la función generar_mapa ayúdese de las funciones auxiliares que se
implementan en el módulo mapas.py. Además, tenga en cuenta que:
1. Primero debe crear un mapa. Use la media de las coordenadas de los centros para centrar el
mapa.
2. Después debe ir creando marcadores y añadiéndolos al mapa. Una vez creado el marcador,
use marcador.add_to(mapa) para añadirlo al mapa.
3. Una vez añadidos todos los marcadores, guarde el mapa en el archivo html con
mapa.save(fichero).
El resultado deber ser un fichero con un mapa similar al de la Figura 4.
Figura 4: Mapa con centros de salud geolocalizados
RETO
La fórmula de la distancia euclídea empleada en este proyecto no es la más adecuada cuando se quieren
calcular distancias entre dos puntos del globo terrestre, ya que no tiene en cuenta la curvatura de la tierra.
Para calcular la distancia entre dos puntos del globo terrestre se usa una aproximación que viene dada por
la fórmula de Haversine1. Implemente una función distancia_harvesine para que en el proyecto se hagan
unos cálculos más realistas.
1 https://es.wikipedia.org/wiki/F%C3%B3rmula_del_haversine
'''