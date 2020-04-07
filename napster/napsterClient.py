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
from src.utils.import_cancion import importar_cancion


# clienteNapster
# TO DO: hacer peticiones(cancion,artista,album)
#       recibir ip y puerto
#       conectarse y recibir con un ciclo las partes de las canciones

def ClientNapster():
    name_song = menu()
    if name_song:
        servers, size_song = reqSong(name_song)
        print("servidores: ", servers)
        print("tamaño: ", size_song)
        # TO DO: conectarse a todos los servidores que tienen la cancion
        song_files_list = conect_to_servers(name_song, servers, size_song)
        if(song_files_list):
            print("yeeeahh")
            # TO DO: guardar el archivo en mi directorio /src/songs
            archivo = open("./src/songs/cancion1.mp3", "wb")
            archivo.seek(0)

            for i in song_files_list:
                archivo.write(i)
    else:
        pass


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


def conect_to_servers(name_song, list_servers, size_song):
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
