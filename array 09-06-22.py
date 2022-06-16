import numpy as np
import random
arreglo = np.array([1,2,3,4,5])


print(arreglo)

a= np.ones((3,3))
print(a)

a=a*2
print(a)
suma=a.sum()
print(suma)

print(a.ndim)

b=np.linspace(0,100,3)
print(b)
print("")
print("")

c=np.zeros((3,3))


for i in range(3):
    for e in range(3):
        ran=random.randint(0,100)
        c[i][e]=c[i][e]+ran
        acum        
print(c)

prom=c.size()
