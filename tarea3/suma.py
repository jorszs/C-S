import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8001")


message = socket.recv_string()
#message_str = message.decode('utf-8')

print message

l = message.split(",")
print (l)

respuesta = int(l[1]) + int(l[2])
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)
