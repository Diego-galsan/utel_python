


def mi_primera_funcion():
    """Esta es mi función que no hace nada."""
    pass

def imprime():
    """Esta funcion contiene una funcion print dentro que imprime
     lo que esta ya previamente escrito. """
    print('Hola estoy dentro de una función.')

def opera():
    r = 1+1
    return(r)


print('Estas son pruebas de funciones en python.')

mi_primera_funcion()
imprime()
print(opera())


print()
input()
type()
int(1.5)
str(5)
float(10)
list()
dict()


import random 

help(random.randrange)
help(mi_primera_funcion)
help(imprime)
random.randrange(0,10,3)

import pandas as pd

help(pd.DataFrame)


edad = 16
genero = 'Masculino'

def funcion_compleja():
    edad2 = 22
    if edad < 18:
        print('Es menor de edad ',edad)

funcion_compleja()
print(edad2)




def opera(parametro1=1,parametro2=1): #Función que recibe dos parametros.
    """ Función que recibe dos parametros y los suma """
    return(parametro1+parametro2)


aleatorio1 = random.randrange(1,11)
aleatorio2 = random.randrange(50,101)
print(aleatorio1,aleatorio2)


opera(aleatorio1,aleatorio2)







def alumno_info(nombre,edad=18,sexo='F'):
    """
    nombre: Parametro obligatorio
    edad: Parametro opcional
    sexo: Parametro opcional
    """
    print(f'Nombre del alumno: {nombre} ',f'edad: {edad} ',f'sexo: {sexo}')

alumno_info('Ernesto',32,'M')