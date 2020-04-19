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

    def searchSong(self, req, parametro):
        print("buscando cancion")
        # TO DO: buscar en la base de datos
        #        devolver lista de usuarios que tienen la cancion
        # parametro puede ser titulo,artista,album
        puerto = 27017
        mongoClient = MongoClient("localhost", puerto)
        db = mongoClient.napster

        collection = db.canciones
        cursor = collection.find({parametro: req})

        list_songs_found = []
        for x in cursor:
            if(x["servidores"]):
                # print(x["servidores"])
                list_songs_found.append({
                    "titulo": x["titulo"],
                    "artista": x["artista"],
                    "album": x["album"],
                    "tamaño": x["tamaño"],
                    "servidores": x["servidores"]
                })
                # return x["servidores"], x["tamaño"], x["titulo"]
        return list_songs_found

    def reportSongs(self, client_songs):
        print("2-guardando cancion")
        onServers = False
        servidores = None
        puerto = 27017
        mongoClient = MongoClient("localhost", puerto)
        db = mongoClient.napster
        collection_canciones = db.canciones
        print("3-coleccion importada")
        # por cada cancion del cliente buscar si la cancion ya esta en la base de datos
        # con ese cliente, si no esta entonces agregarla
        songs = client_songs["songs"]
        for i in songs:
            titulo = i["titulo"]
            print("4-", titulo, type(titulo))
            song = None
            song = db.canciones.find({"titulo": titulo})
            song_found = [song]
            for x in song:
                print("cancion: ", x)
                song_found.append(x)
                servidores = x["servidores"]
            if(len(song_found) == 2):
                print("5-cancion encontrada ", song)

                if servidores:
                    for i in servidores:
                        print("6-buscando servidores",)
                        if (i["ip"] == client_songs["ip"] and i["port"] == client_songs["port"]):
                            print("match con servidor")
                            onServers = True

                if onServers == False:
                    # el usuario no esta en la lista de servidores entonces lo agrego a la lista servidores en la cancion encontrada en la bd
                    print("7-actualizando", song)
                    if(len(song_found) == 2):
                        cancion = song_found[1]
                        print("7.5-cancion", cancion)
                        print("7.6-titulo", cancion["titulo"])
                        song_title = cancion["titulo"]
                        result = db.canciones.update_one({"titulo": song_title}, {
                            '$push': {"servidores": {"ip": client_songs["ip"], "port": client_songs["port"]}}})
                        result.matched_count
                    else:
                        pass
            else:
                # agregar nueva cancion
                print("agregando nueva cancion")
                new_song = {
                    "titulo": i["titulo"],
                    "artista": i["artista"],
                    "album": i["album"],
                    "tamaño": i["tamaño"],
                    "servidores": [{"ip": client_songs["ip"], "port":client_songs["port"]}]
                }

                new_s = db.canciones.insert_one(new_song)


s = zerorpc.Server(dir_rpc())
s.bind("tcp://*:8001")
s.run()
