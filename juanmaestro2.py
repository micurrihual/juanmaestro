    #print('Juan Maestro App')
    #print('1 Registrar Cliente')
    #print('2 Sucripcion')
    #print('3 Consultar datos cliente')
    #print('4 Salir')
    #op=input('Ingrese opción: ')
import os 
os.system('cls')
nombre=list();run=list();edad=list();celular=list();direccion=list();comuna=list();correo=list();genero=list()
cliente=[nombre,run,edad,celular,direccion,comuna,genero]
ejecutar=True
while ejecutar:
    try:
        print('Juan Maestro App')
        print('1.Registrar Cliente \ 2. Suscripcion \ 3. Consultar datos cliente \ 4. Salir')
        opp = int(input("ingrese su opcion:"))
        if opp<1 or opp>3:
            os.system ("cls")
            print("opcion debe ser entre 1 y 3...")
        else:
            os.system ("cls")
            ejecutar=False
    except:
        os.system ("cls")
        print("debe ingresar correctamente la opcion")
if opp==1:
    xnombre=input('Ingresar Nombre : ')
    xrun=input('Ingresar Run :')
    xedad=int(input('Ingresar edad :'))
    xcelular=input('Ingresar numero de celular :')
    xdireccion=input('Ingrese direccion : ')
    xcorreo=input('ingrese correo :')
    xgenero=input('Ingrese su genero [M] o [F]: ')

