import os
import sys

import hashlib

# recibe el archivo despues de abrirlo con read para lectura del archivo "a = archivo.read()"


def get_hash_song(song):
    hashmd5 = hashlib.md5()
    hashmd5.update(song)
    return hashmd5.hexdigest()


def importar_cancion(nombre):
    size = os.path.getsize(nombre)

    archivo = open(nombre, "rb+")
    archivo.seek(0)
    cancion = archivo.read()

    id_song = get_hash_song(cancion)
    #tamaño = sys.getsizeof(cancion)

    return cancion, size, id_song
