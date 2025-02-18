import string
import unicodedata
from random import choice
import funciones as fn
import argparse
import os

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Función principal del juego Ahorcado
    '''
    #cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    #cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    #obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5# 5 oportunidades de fallar
    p = choice(palabras)# elegimos una palabra al azar
    abcdarios = {letra: letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    while o>0:
        fn.despliega_plantilla(plantillas, o)
        o =fn.adivina_letra(abcdarios, p, letras_adivinadas, o)
        if p == ''.join([letra if letra in letras_adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra')
            break
    fn.despliega_plantilla(plantillas, o)
    print (F"La palabra es {p}")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    descripcion = 'Juego del Ahorcado'
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras a adivinar', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print(f'El archivo {archivo} no existe')
    else:    
        main (archivo)
    #archivo = ('./datos/pg15532.txt')
    
