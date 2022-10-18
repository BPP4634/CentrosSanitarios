from centros import *

def main():
    DATOS = lee_datos('./data/centrosSanitarios.csv')
    print(DATOS[:3])
    print(calcular_total_camas_centros_accesibles(DATOS))

if __name__ == '__main__':
    main()