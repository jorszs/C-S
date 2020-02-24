import zmq
import socket
import math

context = zmq.Context()
suma = context.socket(zmq.REQ)
suma.connect("tcp://localhost:8000")



#avisar que el servicio esta activo
nombre_equipo = str(socket.gethostname())
msm = "log"+","+nombre_equipo+","+"8005"
suma.send_string(msm)
acuse = suma.recv_string()
print (acuse)


#contexto para reply
context_rep = zmq.Context()
socket = context_rep.socket(zmq.REP)
socket.bind("tcp://*:8005")
message = socket.recv_string()

print (message)

l = message.split(",")
print (l)

try:
    respuesta = math.log(int(l[1]),int(l[2]))
except:
    respuesta = "los argumentos estan fuera del dominio"
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)
