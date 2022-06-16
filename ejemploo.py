import os
os.system('cls')


ejecutar=True
while ejecutar:
    try:
        print("--eliga el tamaño de la pizza--")
        print("1.pizza familiar $8.000\n2.pizza grande $12.000\n3.pizza familiar con borde de queso $16.000")
        opcionpi = int(input("ingrese su opcion:"))
        if opcionpi<1 or opcionpi>3:
            os.system ("cls")
            print("opcion debe ser entre 1 y 3...")
        else:
            os.system ("cls")
            ejecutar=False
    except:
        os.system ("cls")
        print("debe ingresar correctamente la opcion")
if opcionpi==1:
    pizza=8000 
    pizzat="pizza familiar" 
elif opcionpi==2:
    pizza=12000
    pizzat="pizza grande"
elif opcionpi==3:
    pizza=16000
    pizzat="pizza familiar con borde de queso"
ejecutar=True
while ejecutar:
    try:
        cantidadp = int(input("cuantas pizzas quiere:"))
    except:
        os.system ("cls")
        print("ingrese correctamente la cantidad de pizzas")
    else:
        os.system ("cls")
        ejecutar=False
ejecutar=True        
pizza=pizza*cantidadp
while ejecutar:
    try:
        print("--desea agregar palitos de ajo--")
        print("1.porcion de 4 palitos $3.000\n2.porcion de 6 palitos $5.000\n3.porcion de 12 palitos $8.500\n4.no")
        opcionpa = int(input("ingrese su opcion:"))
        if opcionpa<1 or opcionpa>4:
            os.system ("cls")
            print("opcion debe ser entre 1 y 4...")
        else:
            os.system ("cls")
            ejecutar=False
    except:
        os.system ("cls")
        print("debe ingresar correctamente la opcion")
if opcionpa==1:
    palitos=3000
    palitost="porcion de 4 palitos"
elif opcionpa==2:
    palitos=5000
    palitost="porcion de 6 palitos"
elif opcionpa==3:
    palitos=8500
    palitost="porcion de 12 palitos"
elif opcionpa==4:
    palitos=0
    palitost="nada"
ejecutar=True

while ejecutar:
    try:
        cantidada = int(input("cuantas porciones quiere:"))
    except:
        os.system ("cls")
        print("ingrese correctamente la cantidad de porciones")
    else:
        os.system ("cls")
        ejecutar=False
ejecutar=True
palitos=palitos*cantidada
while ejecutar:
    try:
        print("--desea agregar bebida--")
        print("1.bebida 1.5L $2.000\n2.bebida 2L $2.500\n3.bebida 3L $3.000\n4.no")
        opcionb = int(input("ingrese su opcion:"))
        if opcionb<1 or opcionb>4:
            os.system ("cls")
            print("opcion debe ser entre 1 y 4...")
        else:
            os.system ("cls")
            ejecutar=False
    except:
        os.system ("cls")
        print("debe ingresar correctamente la opcion")
if opcionb==1:
    bebida=2000
    bebidat="bebida 1.5L"
elif opcionb==2:
    bebida=2500
    bebidat="bebida 2L"
elif opcionb==3:
    bebida=3000
    bebidat="bebida 3L"
elif opcionb==4:
    bebida=0
    bebidat="nada"
ejecutar=True
while ejecutar:
    try:
        cantidadb = int(input("cuantas bebidas quiere:"))
    except:
        os.system ("cls")
        print("ingrese correctamente la cantidad de porciones")
    else:
        os.system ("cls")
        ejecutar=False
bebida=bebida*cantidadb
ejecutar=True
while ejecutar:

    nombre=input("Ingrese nombre del cliente: ")
    largon=len(nombre)
    if largon==0:
        os.system ("cls")
        print("ingrese correctamente el nombre del cliente")
    else:
        os.system ("cls")
        ejecutar=False

ejecutar=True
while ejecutar:

    direccion=input("Ingrese direccion del cliente: ")
    largod=len(direccion)
    if largod==0:
        os.system ("cls")
        print("ingrese correctamente la direccion del cliente")
    else:
        os.system ("cls")
        ejecutar=False
total=pizza+palitos+bebida
ejecutar=True
while ejecutar:
    telefono=input("Ingrese numero de telefono: ")
    largot=len(telefono)

    if largot==8 and telefono.find("+")<0 and telefono.find("-")<0:
        os.system ("cls")
        ejecutar=False
    else:
        os.system ("cls")
        print("ingrese correctamente el telefono del cliente")


ejecutar=True
while ejecutar:
    try:
        print("--desea agregar propina--")
        print("1.Si\n2.No")
        opcion = int(input("ingrese su opcion:"))
        if opcion<1 or opcion>2:
            os.system ("cls")
            print("opcion debe ser entre 1 y 2...")
        else:
            os.system ("cls")
            ejecutar=False
    except:
        os.system ("cls")
        print("debe ingresar correctamente la opcion")
ejecutar=True
if opcion==1:
    propina=total*0.1
    total=total*1.1
    
    respuestat="si agrego propina"
elif opcion==2:
    propina=0
    total=total+0
    respuestat="no agrego propina"

print("---Detalles de la compra---")
print(f"nombre cliente:{nombre}")
print(f"direccion del cliente:{direccion}")
print(f"telefono del cliente:{telefono}")
print(f"usted compro {cantidadp} {pizzat} ={pizza}")
print(f"palitos de ajo compro {cantidada} {palitost} ={palitos}")
print(f"bebidas compro{cantidadb} {bebidat} = {bebida} ")
print(f"y usted {respuestat} ({propina})")
print(f"total de la compra es {total}")
