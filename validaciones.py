

while True:

    a=input("ingresar una contraseña alfanumerica")
    if len(a)==4:
        if a[0:1].isalpha():

            if a[0:4].isnumeric():
                print('esta listo')
                break
            else:
                print('no es numerico')

        else:
            print('no es una letra')

    else:
        print('largo invalido')
