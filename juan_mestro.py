print('menu principal')
print('1-ingrese')
print('2-modifique')

while True:
    try:
        a=int(input('ingrese la opcion: '))
        if a==1 or a==2:
            break
    except: input('ingrese opcion valida¡')


rut=list();edad=list();nombre=list()
persona=[rut,edad,nombre]

if a==1:
    while True:
        while True:
            try:
                xrut=int(input('ingrese rut, sin digito ni puntos: '))
                if len(str(xrut))>6 and len(str(xrut))<9:
                    rut.append(xrut)
                    input('todo bien')
                    break

            except Exception as e:
                    input('ingresar un rut valido')
        while True:
            try:
                xedad=int(input('ingrese edad: '))
                if xedad>0 and xedad<111:
                    edad.append(xedad)
                    input('todo bien')
                    break
            except:
                    input('ingrese edad valida')

        print(persona)

        c=input('salir=2 , seguir=otra tecla')
        if c==2:
            break

elif a==2:
    b=input('que quiere modificar 1-rut 2-edad')
    if b==1:
        try:
            xrun=input('ingrese el rut ')
            i=run.index(xrun)
        except: input("rut no encontrado")

        d=input('que quiere modificar? 1-rut 2-edad')
        if d==1:
            pass
