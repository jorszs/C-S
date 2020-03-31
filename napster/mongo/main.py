from pymongo import MongoClient
from cancion import cancion

import sys
import os
from import_cancion import importar_cancion

puerto = 27017

mongoClient = MongoClient("localhost", puerto)

db = mongoClient.napster

collection = db.canciones


# importar cancion
ar_cancion, tamaño = importar_cancion("el desorden.mp3")
collection.insert_one(cancion(ar_cancion))
