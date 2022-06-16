import os
while True:



    a=input("ingresar PATENTE: ")
    if len(a)==6:
        if a[0:4].isalpha():
            if a[4:6].isnumeric():
                if a[0:1]!='a'and a[0:1]!='A'and a[0:1]!='e'and a[0:1]!='E'and a[0:1]!='i' and a[0:1]!='I'and a[0:1]!='o'and a[0:1]!='O'and a[0:1]!='u'and a[0:1]!='U'and a[0:1]!='m'and a[0:1]!='M'and a[0:1]!='n' and a[0:1]!='N'and a[0:1]!='ñ'and a[0:1]!='Ñ'and a[0:1]!='q'and a[0:1]!='Q':

                    input(f'la patente es:{a}, MAYOR al año 2006')
                else:
                    input('Numeracion Invalida para tipo de patente y Año')

        else:
            input('Los Caracteres no corresponden a una Patente')

        if a[0:2].isalpha():
            if a[2:5].isnumeric():
                if a[0:1]!='i'and a[0:1]!='I'and a[0:1]!='q' and a[0:1]!='Q'and a[0:1]!='ñ' and a[0:1]!='Ñ':
                    input(f'la patente es:{a}, MENOR al año 2006')
                else:
                    input('Numeracion Invalida para tipo de patente y Año')
                #break


        else:
            input('Los Caracteres no corresponden a una Patente')


    else:
        print('largo invalido')
        input('Los Caracteres no corresponden a una Patente')
    os.system('cls')
