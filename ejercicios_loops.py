
#Ejercicio 1
#palabra = input('Ingrese una palabra')

#for i in range(10):
#    print(i,palabra)


#Ejercicio 2
#numero = input('Ingrese un número ') 

#for i in range(1,int(numero)+1):
#    for j in range(i):
#        print('*',end='')
#    print('\n')




#Ejercicios while
#palabras = ''

#while palabras!='salir':
#    print('El password no es la correcta')
#    palabras = input('Ingrese su password ')
    

jugador1 = input('Introduce tu edad ')
edad = 0
while edad != jugador1:
    edad = input('Jugador 2 adivina la edad')
    if edad<jugador1:
        print('Te faltan años')
    elif edad>jugador1:
        print('Te pasaste de años')
print('Lograste adivinar la edad. Felicidades.')



