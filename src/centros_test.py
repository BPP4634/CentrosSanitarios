from centros import *

def main():
    DATOS = lee_datos('./data/centrosSanitarios.csv')
    print(DATOS[:3])
    print(calcular_total_camas_centros_accesibles(DATOS))
    print(obtener_centros_con_uci_cercanos_a(DATOS,Coordenada(36,-1.4),200))

if __name__ == '__main__':
    main()