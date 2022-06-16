
lista=[]
while True:
    while True:
        numero=int(input("ingrese un numero entero: "))
        if numero > 0 and numero < 1501:
            break
    lista.append(numero)
    lista.sort()
    print(lista)
