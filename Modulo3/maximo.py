# -*- coding utf-8 -*-

def maximo_2(a,b):
    "Devuelve el maximo entre a y b"
    maximo = a
    if b > a:
        maximo = b
    return maximo

def maximo_3(a,b,c):
    "Devuelve el maximo entre a, b y c"
    return maximo_2(a, maximo_2(b,c))

print ("Maximo 2: ",maximo_2(2,5))
print ("Maximo 3: ",maximo_3(6,1,5))
