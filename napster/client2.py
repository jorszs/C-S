# servidorNapster
# TO DO: buscar canciones en mi carpeta y montarlas en una base de datos(debe contener ip, puerto y cancion)
#       enviar info de las canciones al servidor
#       procesa peticiones para descargar cancion- envia la cancion o la parte correspondiente


import zerorpc
import sys
from pymongo import MongoClient

cancion = []


class napsterServer:
    def download(self, name_song, size_song, parts, x):
        print("size: ", size_song)
        print("\ntipo: ", type(int(size_song)))
        part = int(size_song) / parts
        end = int(part * (x + 1))
        start = int(end - part)

        print("size: "+str(size_song)+"\nstart: " +
              str(start)+"\nend: "+str(end)+"\npart: "+str(part))

        url = "./src/songs/"+name_song+".mp3"
        archivo = open(url, "rb+")
        archivo.seek(start)
        song = archivo.read(end)

        return song

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


s = zerorpc.Server(napsterServer())
s.bind("tcp://*:8011")
s.run()
