

print('')

nombre=list();apellido=list()

for x in range(3):
    a=input('ingrese nombre: ')
    nombre.append(a)
    b=input('ingresar apellido: ')
    apellido.append(b)
largo=len(nombre)

print('')

#listado de nombre y apellido como se ingreso
for x in range(largo):
    print(f'{nombre[x]} {apellido[x]}')

    #ordenar por apellido
print('')
for apellidos, nombres in sorted(zip(apellido, nombre)):
    print(apellidos, nombres)

#    orderar por nombre
print('')
for nombres, apellidos in sorted(zip(nombre, apellido)):
    print(nombres, apellidos)
