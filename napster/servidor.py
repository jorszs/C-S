# server
# recibe peticiones de clientes buscando una cancion
# parametros de busqueda (artista, cancion, album)
# recibe informacion de cada cliente y que canciones tiene
# las guarda en una base de datos


import zerorpc
import sys
from pymongo import MongoClient

cancion = []


class dir_rpc:
    def pet(self, p):
        # print(p)
        print(sys.getsizeof(p))
        cancion.append(p)
        archivo = open("cancion.mp3", "wb")
        archivo.write(p)
        archivo.close()
        print("recibido")

    def searchSong(self, req):
        print("buscando cancion")
        # TO DO: buscar en la base de datos
        #        devolver lista de usuarios que tienen la cancion
        puerto = 27017
        mongoClient = MongoClient("localhost", puerto)
        db = mongoClient.napster

        collection = db.canciones
        cursor = collection.find({"titulo": req})

        for x in cursor:
            if(x["servidores"]):
                # print(x["servidores"])
                return x["servidores"], x["tamaño"]
            # return x["servidores"]
        #clients = db.getCollection('canciones').find({})


s = zerorpc.Server(dir_rpc())
s.bind("tcp://*:8000")
s.run()
