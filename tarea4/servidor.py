import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000")


directorio = {
}

def adicionar(msm):
    l = msm.split(",")
    directorio[l[0]] = {"ip":l[1],"puerto":l[2]}


message = socket.recv_string()
socket.send_string("ok")
print (message)
adicionar(message)
print (directorio)


while True:

    message = socket.recv()
    #message_str = message.decode('utf-8')
    print (message)
    #adicionar(message)
    #puerto = directorio.get(message)
    #socket.send(puerto)
    #message_str = message.decode('utf-8')
