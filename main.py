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
        line = m.readline().strip('\n')
        vec.append(line)
    # Cerrar el archivo
    m.close()


#2) Procesar el archivo de texto series.csv para generar un vector de registros de series con el siguiente formato:

def cargar_registros(vec_regs):
    #Primero abrimos el archivo de series_aed
    m = open("series_aed.csv", mode='rt', encoding='utf8')


def main():
    # Generamos el vector con los generos de las series
    vec_gen = []
    process_txt(vec_gen)
    print(vec_gen)


if __name__ == '__main__':
    main()
