cont=0
cont1=0
while True:
    num=int(input("ingresa un numero entero"))
    if num%2==0:
        cont=cont+1
    else:
        cont1=cont1+1
    parar=int(input("para finalizar ingresar: 1"))
    if parar==1:
        print(f"la cantidad de numero pares es:{cont} y la camtidad de impares son:{cont1}")
        break
