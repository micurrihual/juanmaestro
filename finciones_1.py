#sin argumentos y soin retorno
def saludar():
    print('hola')

saludar()


#sin argumentos y con retorno
def sumar():
    a=int(input('ingerese valor'))
    b=int(input('ingerese valor'))
    c=a+b
    return c
s=sumar()
print(s)

#con argumentos y sin retorno

def sumar(a,b):
    c=a+b
    print(f'la suma de {a} + {b} = {c}')


x=int(input('ingrese valor'))
y=int(input('ingrese valor'))
sumar(x,y)


# con argumentos y con retorno
def sumar(a,b):
    return a+b



x=int(input('ingrese valor'))
y=int(input('ingrese valor'))
sumar(x,y)


#funciones especiales

def varios_valores(*args):


varios_valores(1,4,5,'crist')