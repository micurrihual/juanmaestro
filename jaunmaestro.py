import os
cliente=[]

while True:
    try: 
        print('Juan Maestro App')
        print('1 Registrar Cliente')
        print('2 Sucripcion')
        print('3 Consultar datos cliente')
        print('4 Salir')
        op=int(input('Ingrese opción: '))

        # Registro op1

        if op =='1':
                xrun=input('--INGRESAR RUN SIN DIGITO VERIFICADOR NI PUNTOS : --')
                if xrun.isnumeric() and (xrun>=4000000 and (xrun <=99999998)):
                    pass
                xdireccion=input('-- INGRESE SU DIRECCION : -- ')
                xcomuna=input('-- INGRESE SU COMUNA DONDE VIVE : --')
                xnombre=input('-- INGRESAR NOMBRE COMPLETO: -- ')
                xcorreo=input('-- INGRESE CORREO : --')
                if "@" in xcorreo:
                        pass
                xedad=int(input('-- INNGRESE SU EDAD : --'))
                if xedad>=1 and xedad<=109:
                        pass
                xgenero=input('Ingrese su genero [F] o [M]: ')
                if xgenero.upper() == "F" or xgenero.upper() == "M":
                        pass
                xnumero=input('-- INGRESE SU NUMERO DE CELULAR : --')
                tipo=input('-- INGRESE SU TIPO DE SUSCRIPCION [PREMIUM], [GOLD], [SILVER]: --]')
                if tipo.upper() == "PREMIUM" or tipo.upper == "GOLD" or tipo.upper == "SILVER":
                    pass
    except Exception as e:

        print ("Algún dato es incorrecto...:", e)
        input ("Pulse una tecla")