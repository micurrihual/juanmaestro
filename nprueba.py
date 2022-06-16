patente = []

año = []

marca = []

modelo = []

gas = []

ob = []

lista = ['d', 'b', 'e', 'h', 'D', 'B', 'E', 'H']

opt=0

 

while opt!=4:

    print("ServiExpress")

    print("*****************")

    print("1.-Registrar Automobil")

    print("2.-Registrar Mantenimiento")

    print("3.-Consultar Automovil")

    opt = input()  

      

    if opt==1:

        try:

            print("Ingrese Patente")

            x = input()

            if  len(x)==6:

                print("patente valida")

                patente.append(x)

        except:

            print("valor invalido")

        try:

            print("Ingrese Año")

            x = input()

            if x >=1900 or x<=2021:

                print("valor valida")

                año.append(x) 

        except:

            print("Valor Invalido")

        try:

            print("Ingrese Marca")

            x=input()

            if len(x)!=0:

                marca.append(x)           

        except:

                print("valor invalido")

        try:   

            print("Ingrese Modelo")   

            x=input()

            if len(x)==0:

                modelo.append(x)   

        except:

            print("valor invalido")

        try:

            x= input("Tipo de vehículo - bencina, diesel, eléctrico, híbrido ")

            if lista==x:

                gas.append(x)

        except:

            print("valor invalido")

       

       

    if opt==2:

        x = input("Ingrese Patente para encontrar Resultado")

        if patente == x:

            patente.extend(x)

    if opt==3:

        print(f" {patente} {año} {marca} {modelo} {gas} ")

    if opt==4:

        break