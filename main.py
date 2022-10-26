# Importo librerias
import random
from Series import Serie
import os.path


# 1) Procesar el archivo de texto generos.txt para crear un vector que contenga los nombres de los mismos (Únicamente los nombres y en el mismo orden en el que se encuentran en el archivo).
def process_txt(vec):
    # Debemos abrir el archivo
    m = open("generos.txt", mode='rt', encoding="utf8")
    for linea in m:
        if linea.strip():
            vec.append(linea)


def main():
    # Generamos el vector con los generos de las series
    vec_gen = []
    process_txt(vec_gen)
    print(vec_gen)


if __name__ == '__main__':
    main()
