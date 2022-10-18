from coordenadas import *

def main():
    DATOS = lee_datos('./data/centrosSanitarios.csv')
    print(DATOS[:3])
    print(calcular_distancia(DATOS[0],DATOS[1]))
    print(calcular_media_coordenadas(DATOS[:3]))

if __name__ == '__main__':
    main()