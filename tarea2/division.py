import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8004")
#message = socket.recv()

message = socket.recv()
message_str = message.decode('utf-8')
l = message_str.split(",")
#print (type(l))
try:
    respuesta = int(l[1]) / int(l[2])
except ZeroDivisionError:
    respuesta = "no se puede dividir entre cero"
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)