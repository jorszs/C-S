import zmq
import socket
import time
import threading
'''context = zmq.Context()
suma = context.socket(zmq.REQ)
suma.connect("tcp://localhost:8020")'''


# avisar que el servicio esta activo
'''nombre_equipo = str(socket.gethostname())
msm = "-"+","+nombre_equipo+","+"8002"
suma.send_string(msm)
acuse = suma.recv_string()
print (acuse)'''


# en el directorio se guardaran los servicios activos y donde localizarlos
directorio = {
}


def adicionar(msm):
    l = msm.split(",")
    directorio[l[0]] = {"ip": l[1], "puerto": l[2]}

# contexto para reply


def server():
    while True:
        time.sleep(3)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:8002")
            try:
                message = socket.recv_string()
                print(message)
                l = message.split(",")
                print(l)
                if l[0] == "p":
                    respuesta = int(l[2]) - int(l[3])
                    print(respuesta)
                    respuesta = str(respuesta)
                    socket.send_string(respuesta)

                elif l[0] == "r":
                    pass
            except:
                pass
        except:
            pass  # print("ffffff")


hilo1 = threading.Thread(target=server)
hilo1.start()
'''
l = message.split(",")
print (l)

respuesta = int(l[1]) - int(l[2])
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)'''
