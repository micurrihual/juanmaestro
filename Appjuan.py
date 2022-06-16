 #Celular 
#Tipo: Premium – Gold – Silver 
#Suscripciones por defecto debe ser “suscrito”
#OP 2: Suscripción 
#OP 3: Consultar Datos Cliente 
#Salir 
from logging import exception
import os

nombre=list();run=list();edad=list();celular=list();direccion=list();comuna=list();correo=list();genero=list()
cliente=[nombre,run,edad,celular,direccion,comuna,genero]
while True:
    os.system('cls')
    print('Juan Maestro App')
    print('1 Registrar Cliente')
    print('2 Sucripcion')
    print('3 Consultar datos cliente')
    print('4 Salir')
    op=input('Ingrese opción: ')
    if op =='1':
        while True:
            try:
                xnombre=input('Ingresar Nombre : ')
                xrun=input('Ingresar Run :')
                xedad=int(input('Ingresar edad :'))
                xcelular=input('Ingresar numero de celular :')
                xdireccion=input('Ingrese direccion : ')
                xcomuna=input('ingrese comuna :')
                xcorreo=input('ingrese correo :')
                xgenero=input('Ingrese su genero [M] o [F]: ')
                if xrun.isnumeric() and len(xrun)==2:
                    if len(xnombre)>=3 and xnombre<=100:
                        if xedad>=0 and xedad<=110: 
                            if len(xdireccion)>=3 and xdireccion<=20:
                                if len(xcomuna)>=3 and xcomuna<=15:
                                    if len(xcorreo)>=2 and xcorreo<=20:
                                        if xcelular.isnumeric() and len(xcelular)==6:
                                            break;

                input ("Algún dato no cumple con lo solicitado...")

            except Exception as e:
             print ("Algún dato es incorrecto...:", e)
             input ("Pulse una tecla")
        #Fuera de la lista
        run.append(xrun);nombre.append(xnombre);edad.append(xedad);celular.append(xcelular);direccion.append(xdireccion)
        comuna.append(xcomuna);correo.append(xcorreo);genero.append(xgenero)

        input ("Dato ingresa correctamente...pulse una tecla para continuar...")
        

    elif op=="3":
        try:
            xrun = input ("Ingrese Run: ")
            i = run.index(xrun)

            print (f"{cliente[0][i]} {cliente[1][i]} {cliente[2][i]} {cliente[3][i]}")
            input ("Pulse una tecla para continuar...")
      
        except:

            input ("Run no existe en la lista")
        
    elif op == "4":
        break
  
    else:
        input("Opcion no valida...pulse para continuar")