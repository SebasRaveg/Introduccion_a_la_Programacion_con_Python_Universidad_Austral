# Numeros del 0 al 9
for i in range(10):
    print(i)

# Se recorren los caracteres del String
for i in 'Hola Mundo':
    print(i)

# Contador de 10 devuelve 10
def contador(n):
    c = 0
    for i in range(n):
        c += 1
    return c
contador(10)

# Recorre los numeros de la lista sumandolos
def sumatoria(numeros):
    acum = 0
    for n in numeros:
        acum += n
    return acum
sumatoria([1,2,3,4,5])

# Imprime la tabla de multiplicar de un numero
def tabla_multiplicar(numero):
    "Imprime la tabla de multiplicar"
    for indice in [1,2,3,4,5,6,7,8,9,10]:
        print(f"{numero} * {indice} = {numero * indice}")
tabla_multiplicar(2)    