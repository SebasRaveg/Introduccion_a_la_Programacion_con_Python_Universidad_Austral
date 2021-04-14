def a_function(a_number):
    """
      La funcion recibe un numero a_number y hace:
      Si el numero es par:
          Si es multiplo de 10:
             Devolver el resultado de dividir el numero por 2
          Si es multiplo de 8
             Devolver el resultado de dividir el numero por 4
         Sino restarle 1 
      Si el numero es impar:
          Si es multiplo de 3:
             Devolver el resultado de multiplicar el numero por 11
          Si es multiplo de 2:
             Devolver el resultado de multiplicar el numero por 23
          Sino sumarle 1
    """
 

    result = None
    if a_number % 2 == 0:
        if a_number % 10 == 0:
            result = a_number / 2
        elif a_number % 8 == 0:
            result = a_number / 4
        else:
            result = a_number - 1
    else:
        if a_number % 3 == 0:
            result = a_number * 11
        elif a_number % 7 == 0:
            result = a_number * 23
        else:
            result = a_number + 1
    return result

result_1 = a_function(20)
print(result_1)