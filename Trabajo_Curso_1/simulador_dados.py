import random

seguir = ""
print("SIMULADOR DE DADOS")
print()
input("Para continuar presiona INTRO --> ")
print()

while seguir == "":

    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    suma = dado1+dado2

    print("El primer dado vale --> ", dado1) 
    print("El segundo dado vale --> ", dado2)
    print("La suma de los dados es --> ", suma)

    print()
    print("Quieres volver a jugar?")
    seguir = input("Presione INTRO para seguir jugando / Presione otra TECLA e INTRO para no jugar mas ")
    print()

print("Has salido.")
