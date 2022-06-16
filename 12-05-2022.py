lista=[1,3,5] #la lsita es base 0
print(a[1])
n=len(lista) # largo de la lista
lista.append("fin") # agrega un dato al final
print(lista[n-1]) # imprime el ultimo dato de la lista
lista.extend([2,0]) # extiende la lista con otra lista
lista.append([2,0]) # ingresa el dato en texto
print(lista)
lista.insert(1,2)# inserta dato en la lista, el primer valor es el indice de la lista (insert(indice,dato))
print(lista)
lista.insert(250,2)# inserta dato en la lista al final,se puede indicar un indice mayor que el existente (insert(indice,dato))
print(lista)
lista.remove(5)#remueve el "DATO" no el indice
print(lista)
lista.pop()#elimina el ultoimo registro
lista.pop(2)#elimina un dato segun el indice
lista.reverse()#  te reversa la lista de cambia el orden al contrario
x#ordena de menor a mayor
numeros=list()#declara lista con nimbre numeros
numeros=[]# declara lista con nombtre
