#!/usr/bin/env python3

import socket

mi_socket = socket.socket()
mi_socket.connect( ('localhost', 8000) )

#print ("ingrese operacion")
#operacion = input()

mensaje = "Hola desde el cliente"
#mi_socket.send(mensaje.encode('utf-8')) #el mensaje se envia en bytes, es necesario codificarlo primero
respuesta = mi_socket.recv(1024)
respuesta = respuesta.decode('utf-8')
print (respuesta)
print ("ingrese operacion")
operacion = input()
mi_socket.send(operacion.encode('utf-8'))
#print (type(respuesta))
mi_socket.close()