'''Archivo con las funciones necesarias de la Aplicacion Libro Web'''
import csv

def lee_archivos_csv(archivo:str)->list:
    '''Lee un archivo CSV y lo convierte en una lista de diccionarios'''
    with open(archivo, 'r', encoding='utf8') as f:
        return [X for X in csv.DictReader(f)]
    
def crea_diccionario_titulos(lista:list)->dict:
    '''Crea un diccionario con los titulos como calve y el resto de los datos como valores'''
    return {X['titulo']:X for X in lista}

def busca_en_titulo(lista, palabra)->list:
    '''Busca palabra en el titulo de la lista de diccionarios'''
    lista = []
    for titulo, libro in diccionario.items():
        if 'rebels' in titulo.lower():
            lista.append(libro)
    return lista

if __name__ == '__main__':
    archivo = 'booklists2000.csv'
    lista_libros = lee_archivos_csv(archivo)
    diccionario_libros = crea_diccionario_titulos(lista_libros)
    resultado = busca_en_titulo(diccionario_libros, 'Rebels')
    print(resultado)
