import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8002")


message = socket.recv_string()
#message_str = message.decode('utf-8')
l = message.split(",")
#print (type(l))
respuesta = int(l[1]) - int(l[2])
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)
