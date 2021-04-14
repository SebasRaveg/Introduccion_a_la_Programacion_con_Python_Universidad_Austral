print("Hola este es el simulador de dados")
import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
suma =dado1+dado2
print("El valor del primer dado es: ",dado1)
print("El valor del segundo dado es: ",dado2)
print("La suma de los dados es: ",suma)
print()

while(True):
    print("Quieres simular de nuevo los dados?")
    print("si es si apreta el numero 1, si es no apreta el numero 2")
    opcion = input()
    if opcion == '1':
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        suma =dado1+dado2
        print("El primer dado vale: ",dado1)
        print("El segundo dado vale: ",dado2)
        print("La suma de los dados es: ",suma)
        print()
        
    elif opcion =='2':
        print("Que pena, hasta luego")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
print('Muchas gracias por jugar')