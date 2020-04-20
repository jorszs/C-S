import napsterServer
import napsterClient
import threading
import socket


port = "8011"
path = "./src/songs/"
# server

napsterServer.path = path


def executeServer():
    s = napsterServer.zerorpc.Server(napsterServer.napsterServer())
    s.bind("tcp://*:"+port)
    s.run()


# client

ip = socket.gethostbyname(socket.gethostname())  # ip = "localhost"


servers = [{"ip": "localhost", "port": "8001"},
           {"ip": "localhost", "port": "8000"}]
# ejecutar el cliente y el servidor en dos hilos diferentes

# ejecutar cliente y servidor


def execute():
    client = threading.Thread(
        target=napsterClient.ClientNapster, args=(path, ip, port, servers))
    client.start()
    server = threading.Thread(target=executeServer)
    server.start()


execute()
