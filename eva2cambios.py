import os
os.system('cls')

total = 0

ejecutar= True
while ejecutar:
    print("1.Tres leches $9.000\n2.Chocolate $12.000\n3.Milhojas crema $16.000\n4.Siguiente paso")
    opcion = int(input("Ingrese opcion:"))
    cantidad = int(input("Ingrese cantidad de tortas:"))
    if opcion==1:
        total += 9000*cantidad
    elif opcion==2:
        total += 12000*cantidad
    elif opcion==3:
        total +=16000*cantidad
    elif opcion>3:
        print("Siguiente paso...")
        ejecutar = False
    

ejecutar = True
while ejecutar:
    opcion = int(input("¿Desea agragar Pastelitos?\n1.si\n2.no\n"))
    if opcion==1:  
        opcion2 = int(input("1.Chilenitos $500\n2.Merengue Manjar $600\n3.Donas sabores $700\n4.Siguiente paso\n"))
        cantidadp = int(input("Ingrese cantidad de pastelitos:"))
        if opcion2==1:
            total += 500*cantidadp
        elif opcion2==2:
            total += 600*cantidadp
        elif opcion2==3:
            total += 700*cantidadp
        elif opcion2>3:
            print("Siguiente paso...")
            ejecutar = False
    if opcion==2:
            print("Siguiente paso...")
            ejecutar =False

ejecutar = True
while ejecutar:
    opcion = int(input("¿Desea agragar un pack?\n1.si\n2.no\n"))
    if opcion==1:  
        opcion2 = int(input("1.Pack empanadas queso $2.500\n2.Pack empanadas pino $3.000\n3.Pack pizcitas $3.500\n4.Siguiente paso\n"))
        if opcion2==1:
            total += total+2500
        elif opcion2==2:
            total += total+3000
        elif opcion2==3:
            total += total+3500
        elif opcion2>3:
            print("Siguiente paso...")
            ejecutar = False
    if opcion==2:
            print("Siguiente paso...")
            ejecutar =False

ejecutar = True
while ejecutar:
    nombre = input("Ingrese Nombre:")
    if len(nombre)>0:
        ejecutar =False
    else: 
        print("Debe ingresar su nombre...")

ejecutar = True
while ejecutar:
    telefono = input("Ingrese telefono:")
    if len(telefono)==8:
        ejecutar = False
    else:
        print("Telefono debe tener 8 caracteres...")
       
        
ejecutar = True
while ejecutar:
    propina = 0.1 
    opcion = int(input("¿Desea agregar propina al despachador?\n1.si\n2.no\n"))
    if opcion==1:
        total += propina*total
        ejecutar =False
    elif opcion==2:
        total = total
        print("Finalizar...")
        ejecutar = False

print(f"Nombre es:{nombre}")
print(f"Telefono es:{telefono}")
print(f"Total es:{total}")