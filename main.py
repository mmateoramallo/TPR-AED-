# Importo librerias
import random
from Series import Serie
import os.path


# Menu
def mostrar_menu():
    print('Bienvenido al Sistema de Gestión de Series: ')
    print('1- CARGUE EN UN VECTOR LOS TIPOS DE GÉNEROS DE SERIES. ')
    print('2- GENERAR VECTOR DE REGISTROS DE SERIES. ')
    print('3.- MOSTRAR SERIES QUE TENGAN DURACIÓN EN MINUTOS ENTRE \'A\' Y \'B\'. MOSTRAR PROMEDIO Y GUARDAR.')
    print('4.- GENERAR VECTOR DE CONTEO POR GÉNERO. MOSTRAR NOMBRE DEL GÉNERO EN LUGAR DEL CÓDIGO. ')
    print('5.- GENERAR ARCHIVO BINARIO ALMACENANDO Nª, NOMBRE DEL GÉNERO Y CANTIDAD DE REGISTROS.')
    print('6.- MOSTRAR ARCHIVO BINARIO DE REGISTROS.')
    print('7.- MOSTRAR SI EXISTE SERIE DE TÍTULO \'TIT\'. SI ESTÁ AUMENTAR EN 1 VOTO. SINO, MOSTRAR MENSAJE.')
    print('0.- SALIR DEL PROGRAMA.')


# 1) Procesar el archivo de texto generos.txt para crear un vector que contenga los nombres de los mismos (Únicamente los nombres y en el mismo orden en el que se encuentran en el archivo).
def process_txt(vec):
    # Debemos abrir el archivo
    m = open("generos.txt", mode='rt', encoding="utf8")
    t = os.path.getsize("generos.txt")
    # Recorremos el archivo
    while m.tell() < t:
        # Almacenamos la linea que estamos procesando, y luego mediante la funcion strip, eliminamos el caracter de diagonal invertida
        # line = m.readline().strip('\n')
        # Leemos la linea y luego le eliminamos el caracter backslash n para poder almacenar el genero en el vector
        linea = m.readline()
        linea = linea[:-1]
        vec.append(linea)
    # Cerrar el archivo
    m.close()


# 2) Procesar el archivo de texto series.csv para generar un vector de registros de series con el siguiente formato:
def cargar_registros(vec_regs):
    # Primero abrimos el archivo de series_aed
    m = open("series_aed.csv", mode='rt')
    # Establecemos un contadar, para validar que no se procese el encabezado
    c = 0
    # Recorremos el archivo
    for linea in m:
        if c > 0 and c <= 10:
            # En este punto ya estamos procesando las lineas del archivo, almacenamos la linea como un array, separando las palabras
            txt_line = linea.split('|')
            # Cargamos los campos, del array txt_line
            Poster_Link = txt_line[0]
            Series_Title = txt_line[1]
            Runtime_of_Series = txt_line[2]
            Certificate = txt_line[3]
            Runtime_of_Episodes = txt_line[4]
            Genre = txt_line[5]
            IMDB_Rating = txt_line[6]
            Overwiew = txt_line[7]

            # Instanciamos la clase
            serie = Serie(Poster_Link, Series_Title, Runtime_of_Series, Certificate, Runtime_of_Episodes, Genre, IMDB_Rating, Overwiew, None)
            #Agregamos al vector
            vec_regs.append(serie)
        c += 1


def main():
    # Generamos el vector con los generos de las series
    vec_gen = []
    # Generamos el vector de registros
    vec_regs = []

    # Mostramos el menu y solicitamos una opcion al usuario
    mostrar_menu()
    op = int(input('Ingres su opcion deseada: '))

    while op != 0:
        if op == 1:
            print('-' * 21, 'Procesar Archivo de Texto', '-' * 21)
            process_txt(vec_gen)
        elif op == 2:
            print('-' * 21, 'CARGANDO VECTOR DE REGISTROS', '-' * 21)
            cargar_registros(vec_regs)
            #Recorremos el vector para mostrar las series que se cargaron en el mismo
            for i in vec_regs:
                print(i)
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass

        # Volvemos a mostrar el menu y solicitamos una opcion al usuario
        mostrar_menu()
        op = int(input('Ingres su opcion deseada: '))


if __name__ == '__main__':
    main()
