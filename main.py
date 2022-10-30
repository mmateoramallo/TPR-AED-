# Importo librerias
import random
from Series import Serie
import os.path


# Menu
def mostrar_menu():
    print()
    print('Bienvenido al Sistema de Gestión de Series: ')
    print('1- CARGUE EN UN VECTOR LOS TIPOS DE GÉNEROS DE SERIES. ')
    print('2- GENERAR VECTOR DE REGISTROS DE SERIES. ')
    print('3.- MOSTRAR SERIES QUE TENGAN DURACIÓN EN MINUTOS ENTRE \'A\' Y \'B\'. MOSTRAR PROMEDIO Y GUARDAR.')
    print('4.- GENERAR VECTOR DE CONTEO POR GÉNERO. MOSTRAR NOMBRE DEL GÉNERO EN LUGAR DEL CÓDIGO. ')
    print('5.- GENERAR ARCHIVO BINARIO ALMACENANDO Nª, NOMBRE DEL GÉNERO Y CANTIDAD DE REGISTROS.')
    print('6.- MOSTRAR ARCHIVO BINARIO DE REGISTROS.')
    print('7.- MOSTRAR SI EXISTE SERIE DE TÍTULO \'TIT\'. SI ESTÁ AUMENTAR EN 1 VOTO. SINO, MOSTRAR MENSAJE.')
    print('0.- SALIR DEL PROGRAMA.')
    print()


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

def insercion_binaria_por_numero_de_votos(vector_registros, registro):
    n = len(vector_registros)
    izq, der = 0, n - 1
    pos = n

    while izq <= der:
        c = (izq + der) // 2
        if registro.No_of_Vote == vector_registros[c].No_of_Vote:
            pos = c
            break
        if registro.No_of_Vote > vector_registros[c].No_of_Vote:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        vector_registros[pos:pos] = [registro]


def cargar_registros(vec_regs, vec_gen):
    # Primero abrimos el archivo de series_aed
    m = open("series_aed.csv", mode='rt', encoding='windows-1252')
    # Establecemos un contadar, para validar que no se procese el encabezado
    c = 0
    # Recorremos el archivo
    for linea in m:
        if 0 < c <= 10:
            # En este punto ya estamos procesando las lineas del archivo, almacenamos la
            # linea como un array, separando las palabras
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
            No_of_Vote = txt_line[12]
            indice = 0
            # Verifico que tenga duracion
            if Runtime_of_Episodes != '':
                # Eliminamos el min
                for i in range(len(Runtime_of_Episodes)):
                    if Runtime_of_Episodes[i] == ' ':
                        indice = i
                Runtime_of_Episodes = Runtime_of_Episodes[:indice]
                # Obtengo el codigo del genero
                for i in range(len(vec_gen)):
                    if Genre == vec_gen[i]:
                        Genre = i
                serie = Serie(Poster_Link, Series_Title, Runtime_of_Series, Certificate, Runtime_of_Episodes, Genre, IMDB_Rating, Overwiew, No_of_Vote)

                # Agrego los elementos
                insercion_binaria_por_numero_de_votos(vec_regs, serie)
        c += 1


    # Cerrar el archivo
    m.close()


def main():
    # Generamos el vector con los generos de las series
    vec_gen = []
    # Generamos el vector de registros
    vec_regs = []
    op = -1

    while op != 0:
        # Volvemos a mostrar el menu y solicitamos una opcion al usuario
        mostrar_menu()
        op = int(input('Ingres su opcion deseada: '))
        if op == 1:
            print('-' * 21, 'Procesar Archivo de Texto', '-' * 21)
            process_txt(vec_gen)
            print(vec_gen)
        elif op == 2:
            print('-' * 21, 'CARGANDO VECTOR DE REGISTROS', '-' * 21)
            cargar_registros(vec_regs, vec_gen)
            # Recorremos el vector para mostrar las series que se cargaron en el mismo
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


if __name__ == '__main__':
    main()
