import sesion10 as mil

cali = []
for i in range(5):
    calificaciones = input('Introduzca las calificaciones')
    if calificaciones.isdigit():
        cali.append(float(calificaciones))
    else:
        print(f'Calificacion {i} no es un número.')
print('El promedio es ',mil.promedio2(cali))
    

