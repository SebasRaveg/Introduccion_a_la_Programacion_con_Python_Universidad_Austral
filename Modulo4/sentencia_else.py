
def buscar_numero_en(numero, lista):
    """
       Buscar el numero @numero en la lista @lista.
       Si lo encuentra devuelve la posicion en la que
       se encontro su primera aparicion.
       Si no lo encuentra devuelve -1.
    """
    indice = -1

    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    else:
        indice = 1
    return indice
buscar_numero_en(1, [2, 3, 1, 4, 5])
buscar_numero_en(1, [2, 6, 3, 4, 5])