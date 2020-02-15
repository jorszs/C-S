import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8001")
#message = socket.recv()

message = socket.recv()
#message = message.decode("utf-8")

print ("recibido: "+message.decode("utf-8"))

'''while True:
    
    message = socket.recv()
    print("Received request: %s" % message)'''