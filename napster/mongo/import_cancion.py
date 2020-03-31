import os
import sys


def importar_cancion(nombre):
    size = os.path.getsize(nombre)
    print(size)

    archivo = open(nombre, "rb+")
    archivo.seek(0)
    cancion = archivo.read()
    tamaño = sys.getsizeof(cancion)
    print(tamaño)
    # print(cancion)

    return cancion, size
