import os
import sys
import zerorpc
from mongo.import_cancion import importar_cancion
# print(cancion)


cancion, tamaño = importar_cancion("el desorden.mp3")


#proxy = xmlrpclib.ServerProxy("http://localhost:8000")


def enviar_cancion(cancion, tamaño):
    c = zerorpc.Client()
    c.connect("tcp://localhost:8000")
    c.pet(cancion)


def enviar_cancion_partes(cancion, tamaño):
    c = zerorpc.Client()
    c.connect("tcp://localhost:8000")
    info = c.pet(cancion)

    for i in range(5):
        info = c.pet(cancion)


enviar_cancion(cancion, tamaño)
