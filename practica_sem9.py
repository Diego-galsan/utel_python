

def promedio(nombre,cal1,cal2):
    """ Función que calcula el promedio del alumno """
    promedio = (int(cal1)+int(cal2))/2
    return(promedio)


def ingresa(numero=1):
    """ Funcíon quie ingresa los datos del alumnno. """
    lista = []
    for i in range(numero):
        nombre = input('Nombre: ')
        cal1 = input('Calificación 1 ')
        cal2 = input('Calificación 2 ')
        lista.append([nombre,cal1,cal2])
        print(nombre, promedio(nombre,cal1,cal2))

    
numero_alumnos = int(input('Ingrese el número de alumnos'))

ingresa(numero_alumnos)

    