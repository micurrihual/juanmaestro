n=0
nombre=[];apellido=[]
while True:
    nom=input("ingresar nombre: ")
    nombre.append(nom)
    ape=input("ingrese apellido: ")
    apellido.append(ape)
    n=n+1
    print(f"esta es {n}")
    print(nombre)
    print(apellido)
    if n==3:
        break
for i in range(n):
    print(f"{nombre[i]} {apellido[i]}")
