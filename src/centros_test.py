from centros import *

def main():
    DATOS = lee_datos('./data/centrosSanitarios.csv')
    print(DATOS[:3])
    print(calcular_total_camas_centros_accesibles(DATOS))
    centroscercanos = (obtener_centros_con_uci_cercanos_a(DATOS,Coordenada(36,-1.4),0.4))
    print(centroscercanos)
    generar_mapa(centroscercanos)
    centroscercanosh = (obtener_centros_con_uci_cercanos_a_haversine(DATOS,Coordenada(36,-1.4),400))
    print(centroscercanosh)
    generar_mapa_haversine(centroscercanosh)

if __name__ == '__main__':
    main()