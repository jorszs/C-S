import os
import sys
#from cancion import song_Schema
from ...utils import import_cancion
from pymongo import MongoClient

# sys.path.append("../..")
# TO DO: importar funcion para recorrer mi carpeta songs y agregar mis canciones a una base de datos


puerto = 27017

mongoClient = MongoClient("localhost", puerto)

db = mongoClient.napster

collection = db.canciones


# importar cancion
ar_cancion, tamaño = importar_cancion("el desorden.mp3")
# collection.insert_one(cancion(ar_cancion))
