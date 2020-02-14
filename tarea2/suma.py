import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:8001")
#message = socket.recv()


while True:
    message = socket.recv()
    print("Received request: %s" % message)