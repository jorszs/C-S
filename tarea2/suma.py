import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8001")
#message = socket.recv()

message = socket.recv()
message_str = message.decode('utf-8')
l = message_str.split(",")
#print (type(l))
respuesta = int(l[1]) + int(l[2])
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)
#message = message.decode("utf-8")
#print (respuesta)
#print ("recibido: "+message.decode("utf-8"))

'''while True:
    
    message = socket.recv()
    print("Received request: %s" % message)'''