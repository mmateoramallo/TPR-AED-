from Series import *
import random
import os.path
import pickle
from Generos_Series import *


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
    indice = 0
    token = linea.split('|')
    poster_link = token[0]
    series_title = token[1]
    runtime_of_series = token[2]
    certificate = token[3]
    runtime_of_episodes = token[4]
    for i in range(len(runtime_of_episodes)):
        if runtime_of_episodes[i] == ' ':
            indice = i

    runtime_of_episodes = runtime_of_episodes[:indice]
    # runtime_of_episodes = int(runtime_of_episodes)
    genre = token[5]
    for i in range(len(vector_generos)):
        if genre == vector_generos[i]:
            genre = i
    iMDB_rating = token[6]
    overwiew = token[7]
    no_of_Vote = int(token[12])
    if runtime_of_episodes != "":
        runtime_of_episodes = int(runtime_of_episodes)
        serie = Serie(poster_link, series_title, runtime_of_series, certificate,
                      runtime_of_episodes, genre, iMDB_rating, overwiew, no_of_Vote)
    else:
        serie = None

    return serie


def insercion_binaria_por_numero_de_votos(vector_registros, registro):
    n = len(vector_registros)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vector_registros[c].no_of_Vote == registro.no_of_Vote:
            pos = c
            break
        if registro.no_of_Vote > vector_registros[c].no_of_Vote:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vector_registros[pos:pos] = [registro]

def cargar_vector_registros(archivo2, vector_registros, vector_generos):
    if not os.path.exists(archivo2):
        print('El archivo', archivo2, 'no existe. Serciórese de que exista primero.')
        return

    m = open(archivo2, mode="rt", encoding="windows-1252")
    tam = os.path.getsize(archivo2)

    while m.tell() < tam:
        c = 1
        # Leer la lista proveniente del archivo menos la primera fila correspondiente a los campos:
        lista = m.readlines()[1:]
        contador_falso = 0
        contador_verdadero = 0
        for linea in lista:
            serie = tokenizar(linea[:-1], vector_generos)
            if serie:
                insercion_binaria_por_numero_de_votos(vector_registros, serie)
                contador_verdadero += 1
            else:
                contador_falso += 1
            # if serie:
            #     contador_falso += 1

            c += 1

    print()
    print(f'Se omitieron: {contador_falso} series.')
    print()
    print(f'Se ha cargado exitosamente su vector de registros, con {contador_verdadero} series.')


def mostrar_vector_registros(vector_registros):
    for serie in vector_registros:
        print(serie)


# PUNTO 3 ------------------------------------------------------------------------------------------------
def to_string(registro):
    cadena = ''
    cadena += registro.poster_link
    cadena += '|'
    cadena += registro.series_title
    cadena += '|'
    cadena += registro.runtime_of_series
    cadena += '|'
    cadena += registro.certificate
    cadena += '|'
    cadena += str(registro.runtime_of_episodes)
    cadena += '|'
    cadena += str(registro.genre)
    cadena += '|'
    cadena += registro.iMDB_rating
    cadena += '|'
    cadena += registro.overwiew
    cadena += '|'
    cadena += registro.no_of_Vote
    return cadena


def mostrar_y_generar_vector_punto_3(vector_registros, vector_punto_3, a, b):
    contador_serie = 0
    acumulador_serie = 0
    for serie in vector_registros:
        if a <= serie.runtime_of_episodes <= b:
            print(serie)
            contador_serie += 1
            acumulador_serie += serie.runtime_of_episodes
            vector_punto_3.append(serie)
    if contador_serie != 0:
        promedio = round((acumulador_serie / contador_serie), 2)
    else:
        promedio = 0
        print('No existen series que coincidan en nuestros registros, con los limites de tiempo que usted ingreso')
    print(f'La duración promedio de las series que usted eligió es de: {promedio} minutos.')
    return vector_punto_3


def crear_archivo(archivo3, vector_punto_3):
    if len(vector_punto_3) == 0:
        print('El vector de registros cargado está vacío, primero seleccione la opción 1.')
        return

    header = 'Poster_Link' + '|' + 'Series_Title' + '|' + 'Runtime_of_Series' + '|' + 'Certificate' + \
             '|' + 'Runtime_of_Episodes' + '|' + 'Genre' + '|' + 'IMDB_Rating' + '|' + 'Overview' + \
             '|' + 'No_of_Votes'

    m = open(archivo3, "wt", encoding='UTF-8')

    m.write("{}\n".format(header))
    for serie in vector_punto_3:
        serie.no_of_Vote = str(serie.no_of_Vote)
        linea = to_string(serie)
        m.write("{}\n".format(linea))
    m.close()


# PUNTO 4 ------------------------------------------------------------------------------------------------
def cont_ser_por_gen(vector_registros, vec_cont):
    # Recorremos el vector de registros, y el de series
    for i in range(len(vector_registros)):
        # Contamos uno mas en el casillero correspondiente al codigo del genero en el vector de registros
        vec_cont[vector_registros[i].genre] += 1


def show_cont(vec_cont, vector_generos):
    # Recorro el vector de conteo
    for i in range(len(vec_cont)):
        print('-' * 15, '>Hay', vec_cont[i], 'series del genero:', vector_generos[i])


# PUNTO 5 ------------------------------------------------------------------------------------------------
def generate_vec(vec_cont, vec_generos, file_name):
    # Genramos el archivo
    m = open(file_name, 'wb')
    # Recorremos el vector de conteo para instanciar luego la clase
    # Generos_Series para poder obtener del vector los valores
    for i in range(len(vec_cont)):
        # Cargamos los datos del registro
        id_gen = i
        nombre_gen = vec_generos[i]
        cant = vec_cont[i]
        # Intanciamos la clase
        gen_serie = Gen_ser(id_gen, nombre_gen, cant)
        # Hacemos dump de los datos del registro al archivo binario
        pickle.dump(gen_serie, m)
    # Cerramos el archivo
    m.close()


# PUNTO 6 ------------------------------------------------------------------------------------------------
# 6) Mostrar el archivo generado en el punto 5.

def show_file(file_name):
    # Abrimos el archivo
    m = open(file_name, 'rb')
    t = os.path.getsize(file_name)
    # Recorremos el archivo
    while m.tell() < t:
        # Hacemos un load de la informacion cargada en el archivo
        gen_ser = pickle.load(m)
        print(gen_ser)

    # Cerramos el archivo
    m.close()


# PUNTO 7 ------------------------------------------------------------------------------------------------
# 7) Buscar si en el vector de series se encuentra una serie con el campo
# Series_Title igual a tit, siendo tit un valor que se carga por teclado.
# Si se encuentra incrementar su número de votos en uno. Si no se encuentra mostrar un mensaje.
def search_tit(vec_registros):
    tit = input('Ingrese el titulo de la serie que usted desea buscar: ')
    se_encontro = False
    for i in vec_registros:
        if i.series_title == tit:
            # Declaramos que el numero de votos sea un int
            i.no_of_Vote = int(i.no_of_Vote)
            # Incrementamos su numero de votos en uno
            i.no_of_Vote += 1
            print('*' * 21, 'El registro modificado fue', '*' * 21)
            # Lo volvemos un string
            i.no_of_Vote = str(i.no_of_Vote)
            print(i)
            se_encontro = True
            # Cortamos el ciclo para que deje de buscar
            break

    if not se_encontro:
        print('*' * 21, 'No se encontro la serie', tit, '*' * 21)


# FUNCIÓN PRINCIPAL -----------------------------------------------------------------------------------------


def main():
    print()
    print()

    archivo1 = 'generos.txt'
    archivo2 = 'series_aed.csv'
    archivo3 = 'series2.aed.csv'

    filen_name = 'series.dat'

    vector_registros = []
    vector_generos = []
    vector_punto_3 = []

    opc = -1
    bandera_1 = False
    # Verificar si se cargo el vector de conteo
    hay_conts = False
    gen_file = False

    while opc != 0:
        print()
        print()
        menu()
        opc = validar_rango('Ingrese una opción válida por favor: ', 0, 7)
        print()
        print()
        if opc == 1 and not bandera_1:
            generar_vector_generos(vector_generos, archivo1)
            bandera_1 = True
        elif opc == 1 and bandera_1:
            print('Error. Sólo puede generar el vector de géneros una única vez cuando ejecuta el programa.')
        elif opc != 1 and bandera_1:
            if opc == 2:
                cargar_vector_registros(archivo2, vector_registros, vector_generos)
                # mostrar_vector_registros(vector_registros)
                print()
                print('Enhorabuena. Ya puede usar el resto de opciones.')
            elif opc == 3:

                a = validar_rango('Ingrese una duración mínima de su serie: ', 0, 10000)
                b = validar_rango('Ingrese una duración máxima de su serie: ', 0, 10000)

                vector_punto_3 = mostrar_y_generar_vector_punto_3(vector_registros, vector_punto_3, a, b)

                decision = input('¿Desea generar un archivo con los registros mostrados en el punto 3?: S/N ')
                if decision == 's' or decision == 'S':
                    crear_archivo(archivo3, vector_punto_3)
                    print(f'Enhorabuena, ha creado su archivo {archivo3}.')
                else:
                    print('Ud. eligió no crear el archivo del punto 3. Siga usando el programa si desea.')
            elif opc == 4:
                if vector_registros:
                    print()
                    # 4) Generar un vector de conteo en el que se pueda determinar la cantidad
                    # de series por cada uno de los géneros posibles, haciendo uso del vector de
                    # registros de series y del vector de géneros del punto 1. Mostrar los resultados
                    # visualizando el nombre del género en lugar del código representado.
                    vec_cont = [0] * 23
                    # LLamamos a la funcion para contar series por genero
                    cont_ser_por_gen(vector_registros, vec_cont)
                    # Llamamos a la funcion para mostrar el contador
                    show_cont(vec_cont, vector_generos)
                    print(vec_cont)
                    print()
                    hay_conts = True
                    print()
                else:
                    print('Cargue primero el vector de registros')
            elif opc == 5:
                if hay_conts:
                    print()
                    generate_vec(vec_cont, vector_generos, filen_name)
                    print('*' * 21, 'Archivo Generado Correctamente', '*' * 21)
                    print()
                    gen_file = True
                else:
                    print('Cargue Primero el vector de conteo mediante la opcion 4')
            elif opc == 6:
                if gen_file:
                    print()
                    show_file(filen_name)
                    print()
                else:
                    print('Cargue primero el Archivo Binario mediante la opcion 5')
            elif opc == 7:
                # Verifico que el vector de registros este cargado:
                if vector_registros:
                    search_tit(vector_registros)
                else:
                    print('*' * 21, 'Primero Carge el vector de registros si no quiere que explote!!', '*' * 21)

        elif not bandera_1 and opc in (2, 3, 4, 5, 6, 7):
            print('Error. Primero cargue el vector de géneros antes de utilizar otras opciones.')
    else:
        print('¡Gracias por usar nuestro programa!')


if __name__ == '__main__':
    main()
