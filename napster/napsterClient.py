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

'''path = "./src/songs"
ip = "localhost"
port = "8011"

servers = [{"ip": "localhost", "port": "8000"}]'''
# clienteNapster
# TO DO: hacer peticiones(cancion,artista,album)
#       recibir ip y puerto
#       conectarse y recibir con un ciclo las partes de las canciones


def ClientNapster(path, ip, port, servers):
    while True:
        reportSongsToServer(path, ip, port, servers)
        opcion, parametro_de_busqueda = menu()
        print("opcion: ", opcion)
        if opcion == "1":
            if parametro_de_busqueda:
                param = "titulo"
                print("buscando por titulo.")
                # server_list almacena los clientes que tienen la cancion
                seekAndDowloand(param, parametro_de_busqueda, servers, path)
        elif opcion == "2":
            if parametro_de_busqueda:
                print("busqueda por album")
                param = "album"
                # busqueda y descarga
                seekAndDowloand(param, parametro_de_busqueda, servers, path)
        elif opcion == "3":
            if parametro_de_busqueda:
                print("busqueda por artista")


def seekAndDowloand(param, parametro_de_busqueda, servers, path):
    # server_list almacena los clientes que tienen la cancion
    # servers_list, size_song, name_song = reqParam(  # reqSong()
    list_songs_found = reqParam(
        parametro_de_busqueda, servers, param)

    # para cada cancion en la lista de canciones encontradas
    # encontrar y descargar
    print("canciones encontradas: ", len(list_songs_found))
    for song in list_songs_found:
        name_song = song["titulo"]
        size_song = song["tamaño"]
        servers_list = song["servidores"]
        print("servidores: ", servers_list)
        print("tamaño: ", size_song)
        # TO DO: conectarse a todos los servidores que tienen la cancion
        song_files_list = conectToServersThreads(
            name_song, servers_list, size_song)
        song_files_list.sort(key=lambda dict: dict["id"])
        if(song_files_list):
            print("yeeeahh")
            # TO DO: guardar el archivo en mi directorio /src/songs
            archivo = open(path + name_song + ".mp3", "wb")
            archivo.seek(0)

            for i in song_files_list:
                archivo.write(i["song"])

            # reproducir cancion
            url = path + name_song + ".mp3"
            url_song = os.path.abspath(url)
            os.startfile(url_song)
        else:
            print("no se descargo la cancion")
            pass

# buscar y enviar reporte de canciones al servidor principal


def reportSongsToServer(path, ip, port, servers):
    list_of_songs = seek_songs_of_folder(path)
    client_songs = {
        "ip": ip,
        "port": port,
        "songs": list_of_songs
    }

    # TO DO: hacer un try conectandose a los servidores hasta que se haga conexion con alguno
    for server in servers:
        try:
            print("report song. servidor: ", server)
            ip = server["ip"]
            port = server["port"]
            #print("ip", type(server["ip"]))
            #print("port", type(server["port"]))
            cliente = zerorpc.Client()

            url = "tcp://"+ip+":"+port
            #print("url: ", url)
            cliente.connect(url)
            cliente.reportSongs(client_songs)
        except:
            print("error al conectar con servidor al reportar canciones")
            pass


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
            return filter, song
        elif (filter == "2"):
            album = input("\ncual es el album de la cancion: ")
            return filter, album
        elif (filter == "3"):
            artista = input("\ncual es el artista de la cancion: ")
            return filter, artista

# descargar cancion de clientes secuencialmente


def conectToServers(parametro_de_busqueda, list_servers, size_song):
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
        song_part = context.download(
            parametro_de_busqueda, size_song, parts, x)
        list_of_parts.append(song_part)
        x = x+1
    print("devolviendo parte de la cancion")
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

        song_part = context.download(
            name_song, size_song, parts, x)
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


def reqSong(cancion, servers):
    for server in servers:
        try:
            c = zerorpc.Client()
            c.connect("tcp://localhost:"+server["port"])
            servs, tamaño, name_song = c.searchSong(cancion)
            if servs:
                return servs, tamaño
        except:
            pass

# busqueda generica para buscar por titulo, artista y album


def reqParam(parametro_de_busqueda, servers, param):
    for server in servers:
        try:
            c = zerorpc.Client()
            c.connect("tcp://localhost:"+server["port"])
            # servs, tamaño, name_song = c.searchSong(
            list_songs_found = c.searchSong(
                parametro_de_busqueda, param)
            if list_songs_found:
                # return servs, tamaño, name_song
                return list_songs_found
        except:
            print("no se pudo hacer la busqueda en este servidor")
            pass

# ejecutar el cliente y el servidor en dos hilos diferentes
# def executeClientAndServer():
###    client = threading.Thread(target=ClientNapster)
# client.start()


# executeClientAndServer()
# enviar_cancion(cancion, tamaño)
