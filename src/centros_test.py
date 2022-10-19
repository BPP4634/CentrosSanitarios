from centros import *

def main():
    DATOS = lee_datos('./data/centrosSanitarios.csv')
    print(DATOS[:3])
    print(calcular_total_camas_centros_accesibles(DATOS))
    centroscercanos = (obtener_centros_con_uci_cercanos_a(DATOS,Coordenada(36,-1.4),200))
    print(centroscercanos)
    generar_mapa(centroscercanos)

if __name__ == '__main__':
    main()