import os

patente=["AA1000 or BBBB10"]
marca=["chevrolet"]
modelo=["auto"]
año=["entre 1900 a 2021"]
tipo=["bencina "]
lista = ['d', 'b', 'e', 'h', 'D', 'B', 'E', 'H']
registro=["12/05/22"]
ficha=[patente,marca,modelo,año,tipo,registro]

while True:
    try:
        os.system("cls")
        opcion = int(input("1 Registrar Automovil\n2)Registro de mantenimiento\n3) Consultar Automovil\n4) Cerrar sesion \n"))
        if opcion==1:
            xpatente=input("ingrese su patente")
            while True:
                if len(xpatente)== 6 and xpatente[0:2].isalpha() and xpatente[2:6].isnumeric():
                    a=1
                    break
                elif len(xpatente)== 6 and xpatente[0:4].isalpha() and xpatente[4:6].isnumeric():
                    a=1
                    break
                else:
                    xpatente=input("ingrese su patente valida")
            while True:
                if a==1:
                    patente.append(xpatente)
                    break
            xmarca=input("-- ingrese la marca de su vehiculo: --")
            while True:
                if len(xmarca)!=0:
                    xmarca=xmarca.upper()
                    marca.append(xmarca)
                    break
                else:
                    xmarca=input("--ingrese la marca del vehiculo valida-- ")
            xmodelo=input("--ingrese la modelo del vehiculo--")
            while True:
                if len(xmodelo)!=0:
                    xmodelo=xmodelo.upper()
                    modelo.append(xmodelo)
                    break
                else:
                    xmodelo=input("-- ingrese la marca de su vehiculo--")
            xaño=int(input("ingrese el año de fabrica"))
            while True:
                if xaño<1900 or xaño>2021:
                    xaño=int(input("ingrese el año de fabrica valido"))
                else:
                    año.append(xaño)
                    break
            xtipo=input("ingrese el tipo de vehiculo")
            while True:
                if len(xtipo)!=0:
                    tipo.append(xtipo)
                    break
                else:
                    xtipo_vehiculo=input("ingrese el tipo de vehiculo valido")
            xregistro=0+xregistro
            registro.append(xregistro)
            print(ficha)
            input()
        if opcion==2:
                bus=input("indique la patente que esta buscando \n")
                buscador=patente.index(bus)
                print(f"antiguo registro {registro[buscador]}")
                xregistro=input("indique la nueva fecha de registro")
                xregistro="-"+xregistro
                registro[buscador]=registro[buscador] +xregistro
        if opcion==3:
            try:
                bus=input("indique la patente que buscara  \n")
                buscador=patente.index(bus)
                print(f"{ficha[0][buscador]}|{ficha[1][buscador]}|{ficha[2][buscador]}|{ficha[3][buscador]}|{ficha[4][buscador]}|{ficha[5][buscador]}")
                input("presione enter para continuar")
            except:
                print("ingrese una patente correcta")
        if opcion==4:
            break
        if opcion<1 or opcion>4:
            print("indique una opcion correcta\npresione enter para continuar...")
    except:
        os.system("cls")
        input("indique una opcion correcta\npresione enter para continuar...")
os.system("cls")
print("recuerde que tienque cerrar sesion \n\n presione enter para continuar...")

