
def a_funcion(x):
    result = 0

    if x > 0 and x < 5:
        result = x ** 2
    elif x >= 5 and x < 10:
        pass
    else:
        result = (x ** 4) + 1
    return result
a_funcion(2)
a_funcion(7)
a_funcion(12)

def es_primo(numero):

   resultado = True

   for divisor in range(2, numero):

       if (numero % divisor) == 0:

           resultado = False

           break

   return resultado
es_primo(13)