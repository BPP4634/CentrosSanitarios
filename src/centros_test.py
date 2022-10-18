from centros import *

def main():
    DATOS = lee_datos('./data/centrosSanitarios.csv')
    print(DATOS[:3])

if __name__ == '__main__':
    main()