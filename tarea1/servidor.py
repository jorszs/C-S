#!/usr/bin/env python3

import socket
import math

#print (socket)
servidor = socket.socket() #establecer la configuracion inicial con valores predeterminados
servidor.bind( ('localhost',8000) )#establecer la conexion
servidor.listen(5)#cantidad de peticiones que puede manejas en cola
cliente, addr = servidor.accept()

while True:
    peticion = cliente.recv(1024)
    print peticion
    l = peticion.split(",")
    print l
    #print peticion

    if l[0] == '+':
        print 'Suma'
        resultado = str(int(l[1]) + int(l[2]))
    elif l[0] == '-':
        print 'Resta'
        resultado = str(int(l[1]) - int(l[2]))
    elif l[0] == '*':
        print 'Multiplicacion'
        resultado = str(int(l[1]) *int(l[2]))
    elif l[0] == '/':
        try:
            print 'Division'
            resultado = str(int(l[1]) / int(l[2]))
        except ZeroDivisionError:
            resultado = "no se puede dividir entre cero"
    elif l[0] == '^':
        print 'Potencia'
        resultado = str(int(l[1]) ** int(l[2]))
    elif l[0] == 'log':
        try:
            print 'logaritmo'
            resultado = str(math.log(int(l[1]),int(l[2])))
        except ValueError:
            resultado= "los argumentos estan fuera del dominio"
            
    elif l[0] == 'exit':
        print 'Exiting'
        servidor.close()
        cliente.close()
        break

    print l[1],l[0],l[2], '=', resultado
    cliente.send(str(resultado))
