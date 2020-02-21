import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000") #para las operaciones
sock_c = context.socket(zmq.REP)#para cliente
sock_c.bind("tcp://*:8020")

directorio = {
}

def adicionar(msm):
    l = msm.split(",")
    directorio[l[0]] = {"ip":l[1],"puerto":l[2]}





while True:

    message = socket.recv_string()
    print("recibido",str(message))
    socket.send_string("ok")
    print (message)
    adicionar(message)
    print (directorio)

    msm_c = sock_c.recv_string()
    print(msm_c)
    puerto = directorio.get(msm_c)
    #print("puerto",str(puerto['puerto']))
    sock_c.send_string(str(puerto['puerto']))
    #sock_c.send_string("hola")
    #message_str = msm_c.decode('utf-8')
    #message = socket.recv()
    #message_str = message.decode('utf-8')
    #print (message)
    #adicionar(message)
    #puerto = directorio.get(message)
    #socket.send(puerto)
    #message_str = message.decode('utf-8')
