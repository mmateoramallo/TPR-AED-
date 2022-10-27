# Importo librerias
import random
from Series import Serie
import os.path


# 1) Procesar el archivo de texto generos.txt para crear un vector que contenga los nombres de los mismos (Únicamente los nombres y en el mismo orden en el que se encuentran en el archivo).
def process_txt(vec):
    # Debemos abrir el archivo
    m = open("generos.txt", mode='rt', encoding="utf8")
    t = os.path.getsize("generos.txt")
    # Recorremos el archivo
    while m.tell() < t:
        #Almacenamos la linea que estamos procesando, y luego mediante la funcion strip, eliminamos el caracter de diagonal invertida
        #line = m.readline().strip('\n')
        #Leemos la linea y luego le eliminamos el caracter backslash n para poder almacenar el genero en el vector
        linea = m.readline()
        linea = linea[:-1]
        vec.append(linea)
    # Cerrar el archivo
    m.close()


#2) Procesar el archivo de texto series.csv para generar un vector de registros de series con el siguiente formato:

def cargar_registros(vec_regs):
    #Primero abrimos el archivo de series_aed
    m = open("series_aed.csv", mode='rt')
    #Establecemos un contadar, para validar que no se procese el encabezado
    c = 0
    #Recorremos el archivo
    for linea in m:
        if c > 0:
            #En este punto ya estamos procesando las lineas del archivo, almacenamos la linea como un array, separando las palabras
            txt_line = linea.split('|')
            #print(txt_line)


        c += 1



def main():
    # Generamos el vector con los generos de las series
    vec_gen = []
    #Generamos el vector de registros
    vec_regs = []


    process_txt(vec_gen)
    print(vec_gen)

    cargar_registros(vec_regs)



if __name__ == '__main__':
    main()
