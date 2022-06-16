import os
run=list();nombre=list();edad=list();nota=list()
alumno=[run,nombre,edad,nota]

while True:

    print("1- AGREGAR ALUMNO")
    print("2- CONSULTAR POR RUN")
    print("3- ELIMINAR POR RUN")
    print("4- ACTUALIZAR DATOS ALUMNOS")
    print("5- LISTAR TODOS LOS ALUMNOS")
    n=int(input("Ingrese Opcion: "))
    if n >0 and n <6:
        if n==1:
            while True:
                try:
                    print("")
                    print("   ingresar alumnos  ")
                    print(".......................")
                    try:
                        while True:
                            xrun=input("ingrese Run sin digito verificador: ")
                            if len(xrun)>6 and len(xrun)<9 and xrun.isnumeric():
                                i= xrun in run
                                if i==False:
                                    break
                                else:
                                    input("rut repetido")
                    except Exception as e:
                        input("rut repetido",e)

                    run.append(xrun)
                    while True:
                        xnombre=input("ingrese Nombre: ")
                        if len(xnombre)>2 and len(xnombre)<101:
                            break
                    nombre.append(xnombre)
                    try:
                        while True:
                            xedad=input("ingrese edad: ")
                            if xedad.isnumeric() and xedad>0 and xedad<131:
                                break
                    except Exception as e:
                        edad.append(xedad)
                    while True:
                        xnota=input("ingrese nota con decimal: ")
                        a=xnota.count(".")
                        if a==1:
                            xnota2=float(xnota)
                            if xnota2>=1.0 and xnota2<=7.0:
                                break

                    nota.append(xnota2)
                except Exception as e:
                    print("algun dato es incorrecto ",e)



                ex=(input("Salir=2 , cuaquier caracter para continuar: "))
                if ex=="2":
                    break
                    os.system('cls')

        elif n==2:
            os.system('cls')
            try:
                print("")
                print("Busqueda por Rut")
                print("................")
                xrun=input("ingrese un rut: ")
                i=run.index(xrun)
                print(f"{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}")
                input("Precione una tecla para continuar")
            except:
                input("Rut no encontrado en la lista")
                input("Presione una tecla para Continuar")

        elif n==3:
            os.system('cls')
            try:
                print("")
                print("Eliminar por Rut")
                print("................")
                xrun=input("ingrese un rut a eliminar: ")
                i=run.index(xrun)
                run.pop(i);nombre.pop(i);edad.pop(i);nota.pop(i)
                l=len(run)
                x=0
                while x<=l:
                    print(f"{alumno[0][x]} {alumno[1][x]} {alumno[2][x]} {alumno[3][x]}")
                    x=x+1
            except: input("Rut no encontrado en la lista")

            input("Presione una tecla para Continuar")
        elif n==4:
                    os.system('cls')
                    try:
                        print("Actualizar dato de alumnos")
                        print("................")
                        xrun=input("ingrese un rut: ")
                        i=run.index(xrun)
                        print(f"{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}")
                        print('Que desea modificar?')
                        print('')
                        op=int(input('Run=0 - Nombre=1 - Edad=2 - Nota=3: '))
                        print('')
                        if op==0:
                            try:
                                while True:
                                    zrun=input("ingrese Nuevo Run sin digito verificador: ")
                                    if len(zrun)>6 and len(zrun)<9 and zrun.isnumeric():
                                        e= zrun in run
                                        if e==False:
                                            break
                                        else:
                                            input("rut repetido")
                            except Exception as e:
                                input("rut repetido",e)
                                run[i]=zrun

                            print(f"{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}")
                        if op==1:
                            while True:
                                znombre=input("ingrese Nuevo Nombre: ")
                                if len(znombre)>2 and len(znombre)<101:
                                    break
                            nombre[i]=znombre
                        if op==2:
                            try:
                                while True:
                                    zedad=input("Ingrese Nueva edad: ")
                                    if zedad.isnumeric() and zedad>0 and zedad<131:
                                        break
                            except Exception as e:
                                edad[i]=zedad
                        if op==3:
                            while True:
                                znota=input("ingrese nota con decimal: ")
                                a=znota.count(".")
                                if a==1:
                                    znota2=float(znota)
                                    if znota2>=1.0 and znota2<=7.0:
                                        break
                            nota[i]=znota2

                        print("Listado de alumnos")
                        print("................")
                        l=len(run)
                        x=0
                        while x<=l-1:
                            print(f"{alumno[0][x]} {alumno[1][x]} {alumno[2][x]} {alumno[3][x]}")
                            x=x+1

                    except: input("sin alumnos en la lista")

        elif n==5:
            os.system('cls')
            try:
                print("")
                print("Listado de alumnos")
                print("................")
                l=len(run)
                x=0
                while x<=l-1:
                    print(f"{alumno[0][x]} {alumno[1][x]} {alumno[2][x]} {alumno[3][x]}")
                    x=x+1
            except : print("sin alumnos en la lista")

            input("Presione una tecla para Continuar")


    else:
        print("")
        print("opcion elegida es incorrecta")
        input("precione una tecla para continuar")
    os.system("cls")
