
def suma_n(n):
    "Suma los numeros de 1 a n"
    result = 0
    x = n

    while x > 0:
        result += x
        x -= 1
    return result
suma_n(5)

def ciclo_infinito():
    "Imprime el numero 1 infinitas veces"
    i = 1

    while i <= 10:
        print(i, end=" ")
ciclo_infinito() 

n=2
h=0
while n<=110:
    print (n)
    h += n
    n +=1
print (h)

def contador(n):
    s = 0
    
    for n in range(10):
        s += n
    return s
contador(n)





