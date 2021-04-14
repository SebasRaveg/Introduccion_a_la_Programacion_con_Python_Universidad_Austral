# -*- coding utf-8 -*-

def peso(masa, gravedad = 9.8):
    "Formula del peso"
    return masa * gravedad

#Parametros opcionales
print("Peso en la tierra --> ", peso(10))
print("Peso en la luna --> ", peso(10, 1.63))

#Parametros con palabras claves (o argumentos nombrados)
print("Peso en la luna --> ", peso(10, gravedad = 1.63))
print("Peso en la luna --> ", peso(masa = 10, gravedad = 1.63))
print("Peso en la luna --> ", peso(gravedad = 1.63, masa = 10))

#Esta opcion no es valida: Los parametros posicionales no pueden ir despues de un keybord 
#print("Peso de la luna --> ", peso(masa = 10, 1.63))}
#SyntaxError: positional argument follows keyword argument

#Lista de parametros
def suma_numeros(*args):
    "Suma los numeros pasados por parametro"
    return sum(args)
print("6 + 7 + 8 = ", suma_numeros(*[6,7,8]) #Enpaquetados
#print("6 + 7 + 8 = ", suma_numeros(6,7,8))  #Desenpaquetados

#Diccionario de parametros
def imprimir_ticket(*args, **kwargs):
    "Imprime el ticket de una compra"
    print("Detalle ticket")

    for item, precio in kwargs.items():
        print(item, ":" , precio)