import csv
import random

with open('asistentes.csv') as fh:
    asistentes = csv.reader(fh)

    lista_asistentes = list(asistentes)
    # print(lista_asistentes)
    random.shuffle(lista_asistentes)
    respuesta = 'y'
    while respuesta != 'x' and len(lista_asistentes) > 0:
        ganador = lista_asistentes.pop()
        print('El ganador es: {}'.format(ganador))        
        print('X para salir, enter para seleccionar otro ganador: ')
        respuesta = raw_input()
