import zmq
import threading

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

def hilo_op():
    while True:
        message = socket.recv_string()
        print("recibido",str(message))
        socket.send_string("ok")
        print (message)
        adicionar(message)
        print (directorio)

def hilo_c():
    while True:
        msm_c = sock_c.recv_string()
        print(msm_c)
        puerto = directorio.get(msm_c)
        #print("puerto",str(puerto['puerto']))
        sock_c.send_string(str(puerto['puerto']))



hilo_1 = threading.Thread(target=hilo_op)
hilo_1.start()
hilo_2 = threading.Thread(target=hilo_c)
hilo_2.start()