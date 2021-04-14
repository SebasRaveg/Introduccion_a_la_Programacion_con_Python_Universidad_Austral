
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
    return indice
buscar_numero_en(1, [2, 3, 1, 4, 5])
buscar_numero_en(1, [2, 6, 3, 4, 5])

# MODULOS

# import sentencia_break
# sentencia_break.buscar_numero_en(1,[1,2,3])
# from sentencia_break import buscar_numero_en
# buscar_numero_en(1,[1,2,3])

# PAQUETES

# import Modulo4
# from Modulo4 import sentencia_break
# from Modulo4.sentencia_break import buscar_numero_en