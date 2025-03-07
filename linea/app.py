import funciones
import argparse

def main(m, b):
    X = [x/10.0 for x in range (1,101,5)]
    Y= [funciones.calcular_y(x,m,b) for x in X]
    print(X)
    print(Y)
    coordenadas = list(zip(X,Y))
    print(coordenadas)
    funciones.grafica_linea(X,Y,m,b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calcula las coordenas de una linea recta')
    parser.add_argument('-m', type= float, 
    help='Pendiente de la linea', default=2.0)
    parser.add_argument('-b', type= float, 
    help='Interseccion em y', default=3.0)
    args = parser.parse_args()
    main(args.m, args.b)
    main (2,3)