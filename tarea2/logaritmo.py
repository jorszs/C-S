import zmq
import math
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8006")
#message = socket.recv()

message = socket.recv()
message_str = message.decode('utf-8')
l = message_str.split(",")
print (l)
try:
    respuesta = math.log(int(l[1]),int(l[2]))
except:
    respuesta = "los argumentos estan fuera del dominio"
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)