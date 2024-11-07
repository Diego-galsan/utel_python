
print('************************************************************************************************')
print('*                               Sistema de validaciones Python Utel                            *')
print('************************************************************************************************')


edad = input('Hola, ingresa tu edad ')

if edad.isnumeric():
    pass
else:
    print('Valor ingresado no valido, por favor corriga su respuesta')
    exit()

edad = int(edad)

if edad > 150:
    print('Woooow, cuanto has vivido!!!')
elif (edad <18) and (edad>0):
    print('Eres demasiado joven para este curso.')
elif edad <=0:
    print('No puedes tener 0 años ni edad negativo.')
else:
    print('Felicidades, estas en los rangos de edad adecuados. Toma tu premio !!!!!1')