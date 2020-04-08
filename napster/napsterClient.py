# napster cliente: tendra definido las funciones de cliente y de servidor
# cada componente es cliente y servidor a la vez
# cliente puede solicitar informacion al servidor sobre canciones (ya sea el titulo, artista o album)
# el servidor analiza dentro de su base de datos quien o quienes tienen la cancion
# el servidor debe devolver la ip y el puerto del cliente que posee el archivo
# el cliente debe conectarse directamente con los poseedores de la cancion
# estos los devuelven en partes iguales segun el # de clientes que tienen la cancion


import os
import sys
import zerorpc
import threading
import eyed3
from src.utils.import_cancion import importar_cancion

path = "./src/songs"
ip = "localhost"
port = "8013"

servers = [{"ip": "localhost", "port": "8000"}]
# clienteNapster
# TO DO: hacer peticiones(cancion,artista,album)
#       recibir ip y puerto
#       conectarse y recibir con un ciclo las partes de las canciones


def ClientNapster():
    reportSongsToServer()
    name_song = menu()
    if name_song:
        servers, size_song = reqSong(name_song)
        print("servidores: ", servers)
        print("tamaño: ", size_song)
        # TO DO: conectarse a todos los servidores que tienen la cancion
        song_files_list = conectToServersThreads(name_song, servers, size_song)
        song_files_list.sort(key=lambda dict: dict["id"])
        if(song_files_list):
            print("yeeeahh")
            # TO DO: guardar el archivo en mi directorio /src/songs
            archivo = open("./src/songs/cancion1.mp3", "wb")
            archivo.seek(0)

            for i in song_files_list:
                archivo.write(i["song"])
    else:
        pass


# buscar y enviar reporte de canciones al servidor principal
def reportSongsToServer():
    list_of_songs = seek_songs_of_folder(path)
    client_songs = {
        "ip": ip,
        "port": port,
        "songs": list_of_songs
    }

    cliente = zerorpc.Client()
    cliente.connect("tcp://"+servers[0]["ip"]+":"+servers[0]["port"])
    cliente.reportSongs(client_songs)


def seek_songs_of_folder(path):
    lista_canciones = []
    for root,  dirs, files in os.walk(path):
        for file in files:
            try:
                if file.find(".mp3") < 0:
                    continue
                path = os.path.abspath(os.path.join(root, file))

                size = os.path.getsize(path)

                t = eyed3.load(path)
                song_metadatos = {"titulo": t.tag.title,
                                  "artista": t.tag.artist,
                                  "album": t.tag.album,
                                  "tamaño": size}
                lista_canciones.append(song_metadatos)
                #print(t.tag.title, t.tag.artist)
                # TO DO: construir un esquema song: {titulo,artista, album,}
                #       guardar las canciones en una lista
                # {yo:{ip:"",
                #   port:""}
                #   canciones: [{title:"",album:"",artista:""},{title:"",album:"",artista:""}]
                #
                # }
            except Exception as e:
                print(e)
                continue
    # print(lista_canciones)
    return lista_canciones


def menu():
    op = input("1. buscar cancion \n")

    if (op == "1"):
        print("buscar por: \n")
        print("1. titulo \n")
        print("2. album \n")
        print("3. artista \n")
        filter = input("Digite la opcion de busqueda: ")
        if(filter == "1"):
            song = input("\ncual es el nombre de la cancion: ")
            return song
        elif (filter == "2"):
            album = input("\ncual es el album de la cancion: ")
            return album
        elif (filter == "3"):
            artista = input("\ncual es el album de la cancion: ")
            return artista

# descargar cancion de clientes secuencialmente


def conectToServers(name_song, list_servers, size_song):
    # pedir cancion al servidor
    x = 0
    list_of_parts = []
    parts = len(list_servers)
    #part = size_song / parts

    for i in list_servers:
        url = "tcp://"+i["ip"]+":"+i["port"]
        print("url: ", url)
        context = zerorpc.Client()
        context.connect(url)
        song_part = context.download(name_song, size_song, parts, x)
        list_of_parts.append(song_part)
        x = x+1

    return list_of_parts


def conectToServersThreads(name_song, list_servers, size_song):
    # pedir cancion al servidor
    x = 0
    list_of_parts = []
    hilos = []
    parts = len(list_servers)
    #part = size_song / parts

    def song(i, x):
        print("ejecutando: "+str(x))
        url = "tcp://"+i["ip"]+":"+i["port"]
        print("url: ", url)
        context = zerorpc.Client()
        context.connect(url)

        song_part = context.download(name_song, size_song, parts, x)
        list_of_parts.append({"id": x, "song": song_part})

    for i in list_servers:
        hilos.append(threading.Thread(target=song, args=(i, x)))
        x = x+1

    for i in hilos:
        i.start()

    for i in hilos:
        i.join()

    print("lista: ", len(list_of_parts))
    return list_of_parts


def reqSong(cancion):
    c = zerorpc.Client()
    c.connect("tcp://localhost:8000")
    return c.searchSong(cancion)


# ejecutar el cliente y el servidor en dos hilos diferentes
def executeClienteAndServer():
    client = threading.Thread(target=ClientNapster)
    client.start()


executeClienteAndServer()
# enviar_cancion(cancion, tamaño)
