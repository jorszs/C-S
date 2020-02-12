import zmq

context = zmq.Context()

# socket to talk to server
print ("connecting")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8000")

for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))