import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000") # el "*" conecta con el localhost

while True:
    #wait for next request from client
    message = socket.recv()
    print ("receive request %s" % message)

    #do something

    #send reply for client
    socket.send(b"hi from servidor")

