#!/usr/bin/env python3

import socket

cliente = socket.socket()
cliente.connect( ('localhost', 8000) )
mensaje = "Hola desde el cliente"
#mi_socket.send(mensaje.encode('utf-8')) #el mensaje se envia en bytes, es necesario codificarlo primero

while True:

    o = raw_input('Operador: ')
    a = raw_input('Ingrese el primero numero: ')
    b = raw_input('Ingrese el segundo numero: ')

    '''cliente.send(o)
    cliente.send(a)
    cliente.send(b)'''

    p = o + "," + a + "," + b
    print 'concatenacion', p

    cliente.send(p)

    print 'Resultado:',cliente.recv(1024)

    if 'exit' == raw_input('Type "exit" to exit, no input to continue '):
		cliente.send('exit')
		cliente.close()
		exit()

'''respuesta = mi_socket.recv(1024)
respuesta = respuesta.decode('utf-8')
print (respuesta)
print ("ingrese operacion")
operacion = input()
mi_socket.send(operacion.encode('utf-8'))
#print (type(respuesta))
mi_socket.close()'''
