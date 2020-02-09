#!/usr/bin/env python3

import socket

#print (socket)
mi_socket = socket.socket() #establecer la configuracion inicial con valores predeterminados
mi_socket.bind( ('localhost',8000) )#establecer la conexion
mi_socket.listen(5)#cantidad de peticiones que puede manejas en cola

while True:
    conexion, addr = mi_socket.accept()
    print ("nueva conexion establecida")
    #print (addr)
    mensaje = "saludo desde el servidor"
    conexion.send(mensaje.encode('utf-8'))
    peticion = conexion.recv(1024)
    peticion = peticion.decode('utf-8')
    peticion = int(peticion)
    print (peticion)
    print (type(peticion))
    conexion.close()
    