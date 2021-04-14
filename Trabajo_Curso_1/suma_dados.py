import random

def suma_dados():
    preguntar = input('¿Desea tirar los dados? (s/n): ')
    while preguntar!= 's' and preguntar!= 'n':
        preguntar = input('Por favor, teclee "s" o "n": ')

    dado = [1, 2, 3, 4, 5, 6]
    while preguntar == 's':
        num1 = random.choice(dado)
        num2 = random.choice(dado)
        print('El primer número es: ' + str(num1))
        print('El segundo número es: ' + str(num2))
        print('La suma es: ' + str(num1 + num2))
        preguntar = input('¿Desea tirar los dados de nuevo? (s/n): ')
        while preguntar!= 's' and preguntar!= 'n':
            preguntar = input('Por favor, teclee "s" o "n": ')