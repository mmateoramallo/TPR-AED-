from series import *
import random
import os.path
import pickle


# FUNCIONES AUXILIARES ----------------------------------------------------------------------------------
def menu():
    print('Bienvenido al Sistema de Gestión de Series: ')
    print('1- CARGUE EN UN VECTOR LOS TIPOS DE GÉNEROS DE SERIES. ')
    print('2- GENERAR VECTOR DE REGISTROS DE SERIES. ')
    print('3.- MOSTRAR SERIES QUE TENGAN DURACIÓN EN MINUTOS ENTRE \'A\' Y \'B\'. MOSTRAR PROMEDIO Y GUARDAR.')
    print('4.- GENERAR VECTOR DE CONTEO POR GÉNERO. MOSTRAR NOMBRE DEL GÉNERO EN LUGAR DEL CÓDIGO. ')
    print('5.- GENERAR ARCHIVO BINARIO ALMACENANDO Nª, NOMBRE DEL GÉNERO Y CANTIDAD DE REGISTROS.')
    print('6.- MOSTRAR ARCHIVO BINARIO DE REGISTROS.')
    print('7.- MOSTRAR SI EXISTE SERIE DE TÍTULO \'TIT\'. SI ESTÁ AUMENTAR EN 1 VOTO. SINO, MOSTRAR MENSAJE.')
    print('0.- SALIR DEL PROGRAMA.')


def validar_rango(mensaje, li, ls):
    n = int(input(mensaje))
    while n < li or n > ls:
        n = int(input(mensaje))
        if n < li or n > ls:
            print('Error. Usted está intentando ingresar un número fuera del rango válido.')
    return n


# PUNTO 1 ------------------------------------------------------------------------------------------------

def generar_vector_generos(vector_registros, archivo1):
    contador_generos = 0
    m = open(archivo1, 'rt')
    generos = m.readlines()
    for genero in generos:
        genero = genero[:-1]
        vector_registros.append(genero)
        contador_generos += 1
    print(f'Se han cargado exitosamente su vector de géneros, para un total de {contador_generos} géneros.')


# PUNTO 2 ------------------------------------------------------------------------------------------------
def tokenizar(linea, vector_generos):
    token = linea.split('|')
    poster_link = token[0]
    series_title = token[1]
    runtime_of_series = token[2]
    certificate = token[3]
    runtime_of_episodes = token[4]
    runtime_of_episodes = int(runtime_of_episodes[:2])
    # runtime_of_episodes = int(runtime_of_episodes)
    genre = token[5]
    for i in range(len(vector_generos)):
        if genre == vector_generos[i]:
            genre = i
    IMDB_rating = token[6]
    Overwiew = token[7]
    No_of_Vote = token[12]

    serie = Serie(poster_link, series_title, runtime_of_series, certificate,
                  runtime_of_episodes, genre, IMDB_rating, Overwiew, No_of_Vote)

    return serie


def insercion_binaria_por_numero_de_votos(vector_registros, registro):
    n = len(vector_registros)
    izq, der = 0, n-1
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


def cargar_vector_registros(archivo2, vector_registros, vector_generos):
    if not os.path.exists(archivo2):
        print('El archivo', archivo2, 'no existe. Serciórese de que exista primero.')
        return

    m = open(archivo2, "rt")
    tam = os.path.getsize(archivo2)

    while m.tell() < tam:
        # Leer la lista proveniente del archivo menos la primera fila correspondiente a los campos:
        lista = m.readlines()[1:]
        contador_falso = 0
        contador_verdadero = 0
        for linea in lista:
            serie = tokenizar(linea[:-1], vector_generos)
            if not serie.runtime_of_episodes == '':
                insercion_binaria_por_numero_de_votos(vector_registros, serie)
                contador_verdadero += 1
            if serie.runtime_of_episodes == '':
                contador_falso += 1
    # print(f'Se omitieron: {contador_falso} series.')
    # print(f'Se ha cargado exitosamente su vector de registros, con {contador_verdadero} series.')


def mostrar_vector_registros(vector_registros):
    for serie in vector_registros:
        print(serie)

# PUNTO 3 ------------------------------------------------------------------------------------------------


# PUNTO 4 ------------------------------------------------------------------------------------------------


# PUNTO 5 ------------------------------------------------------------------------------------------------


# PUNTO 6 ------------------------------------------------------------------------------------------------


# PUNTO 7 ------------------------------------------------------------------------------------------------


# FUNCIÓN PRINCIPAL -----------------------------------------------------------------------------------------



def main():
    menu()
    archivo1 = 'generos.txt'
    archivo2 = 'series_aed.csv'
    vector_registros = []
    vector_generos = []
    opc = -1
    bandera_1 = False
    while opc != 0:
        opc = validar_rango('Ingrese una opción válida por favor: ', 0, 7)
        if opc == 1 and not bandera_1:
            generar_vector_generos(vector_generos, archivo1)
            print(vector_generos)
            bandera_1 = True
        elif opc == 1 and bandera_1:
            print('Error. Sólo puede generar el vector de géneros una única vez cuando ejecuta el programa.')
        elif opc != 1 and bandera_1:
            if opc == 2:
                cargar_vector_registros(archivo2, vector_registros, vector_generos)
                mostrar_vector_registros(vector_registros)
                print('Se ha cargado exitosamente su vector de registros.')
        elif not bandera_1 and opc in (2, 3, 4, 5, 6, 7):
            print('Error. Primero cargue el vector de géneros antes de utilizar otras opciones.')
    else:
        print('¡Gracias por usar nuestro programa!')



if __name__ == '__main__':
    main()
