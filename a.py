l=int(input('INGRESAR CANTIDAD DE NOMBRES : '))
nom=list()
ape=list()
for i in range(l):
    n=input('ingresar nombre....: ')
    a=input('ingresar apellido..: ')
    nom.append(n)
    ape.append(a)

for i in range(l):
    print(f'{nom[i]} {ape[i]}')

#mostrar en orden alfabetico por apellido
nom_com=list()
for i in range(l):
    aux=ape[i]+' '+nom[i]
    nom_com.append(aux)
nom_com.sort()
print('lista ordenada')
for i in range(l): 
    print(f'{nom_com[i]}')

