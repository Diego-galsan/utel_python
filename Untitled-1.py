
print('************************************************************************************************')
print('*                            Sistema de registro de datos Python Utel                          *')
print('************************************************************************************************')

while True:

    name = input('Ingrese su nombre completo: ')
    edad = input("Ingrese su edad: ")
    email = input('Ingrese su email: ')
    tel = input('Ingrese su teléfono: ')

    print('\n Registro de '+name+' de edad '+edad+' ha sido guardado exitosamente.')


    with open('resgistro.txt','a') as archivo:
        archivo.write('Nombre: {}'.format(name))
        archivo.write(f',Edad: {edad}')
        archivo.write(f',Email: {email}')
        archivo.write(f',Tel: {tel}')
    
    opc = input('Quieres agregar otro registro y/n')

    if opc=='n':
        break
    

    print('************************************************************************************************')


