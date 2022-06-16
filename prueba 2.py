import os
patente=list();marca=list();modelo=list();añof=list();tipo=list();fecha=list();obs=list()
ficha=[patente,marca,modelo,añof,tipo,fecha]
while True:
    os.system('cls')
    print("  MENU PRINCIPAL")
    print("")
    print("1.	Registrar automóvil")
    print("2.	Registro Mantenimiento")
    print("3.	Consultar Automóvil ")
    print("4.	Salir")
    n=int(input("Ingrese Opcion: "))
    if n >0 and n <5:
        if n==1:
            os.system('cls')
            while True:
                a=input("INGRESAR PATENTE: ")
                if a in patente:
                    input("PATENTE YA REGISTRADA")
                else:
                    if len(a)==6:
                        if a[0:4].isalpha():
                            if a[4:6].isnumeric():
                                patente.append(a)
                                break
                        else:
                            if a[0:1].isalpha():
                                if a[2:5].isnumeric():
                                    patente.append(a)
                                    break
                                else:
                                    input('Los Caracteres no corresponden a una Patente')
            while True:
                b=input("INGRESE LA MARCA: ")
                if b.strip()=="":
                    input("ingresar una marca")
                else:
                    marca.append(b)
                    break
            while True:
                c=input("INGRESE MODELO: ")
                if c.strip()=="":
                    input("ingresar un modelo")
                else:
                    modelo.append(c)
                    break
            while True:
                d=input("INGRESE AÑO DE FABRICACION: ")
                if d.isnumeric() and int(d)>1899 and int(d)<2021:
                    añof.append(d)
                    break
                else:
                    input("ingresar año correcto")
            while True:
                e=input("INGRESE TIPO DE VEHICULO   BENCINA:B, DIESEL:D, ELECTRICO:E, HIBRIDO:H: ")
                if e=='b' or e=='B' or e=='d' or e=='D' or e=='e' or e=='E' or e=='h' or e=='H':
                    tipo.append(e)
                    break
                else:
                    input("ingresar tipo de vehiculo correcto")
                print("")
            print("REGISTRO INICIAL DEL AUTOMOVIL.")
            while True:
                f=input("ingrese fecha actual: ")
                if f.strip()!="":
                    fecha.append(f)
                    break
                else:
                    input("ingresar fecha correcta")
            while True:
                g=input("ingresar observaciones: ")
                if g.strip()!="":
                    obs.append(g)

                    break

        if n==2:
            os.system('cls')
            try:
                print("")
                pat=input("INGRESE PATENTE: ")
                i=patente.index(pat)
                print("")
                print("INGRESAR NUEVO REGISTRO:")
                fech1=input("ingresar nueva fecha: ")
                fecha[i]=fecha[i]+" "+obs[i]+"\n"
                obs2=input("ingrese nueva observacion: ")
                fech1=fech1+" "+obs2+"\n"
                fecha[i]=fecha[i]+fech1
                input("Precione una tecla para continuar")
            except:
                input("PATENTE NO ENCONTRADA")
                input("Presione una tecla para Continuar")


        if n==3:
            os.system('cls')
            try:
                print("")
                pat=input("INGRESE PATENTE BUSCADA: ")
                i=patente.index(pat)
                print("")
                print(f" PATENTE:{ficha[0][i]}\n MARCA:{ficha[1][i]}\n MODELO:{ficha[2][i]}\n AÑO FABRICACION:{ficha[3][i]}\n TIPO VEHICULO:{ficha[4][i]}\n REGISTRO:\n{ficha[5][i]}")
                print("")
                input("Precione una tecla para continuar")
            except:
                input("PATENTE NO ENCONTRADA")
                input("Presione una tecla para Continuar")

        if n==4:
            os.system('cls')
            print("")
            print("FIN DEL PROGRAMA")
            print("HASTA LUEGO......")
            break
