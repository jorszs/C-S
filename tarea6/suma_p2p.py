import zmq
import threading
import socket
import cliente
import time

# conexion a resta
# CLIENT
# socket cliente (suma)


# server
# socket server (operacion)

'''context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://*:8000") #para las operaciones'''


# avisar que el servicio esta activo
# i = informar que el servicio esta activo
# p = peticion de alguna operacion


# ---------------------------


# config

directorio = {
}


def adicionar(msm):
    l = msm.split(",")
    directorio[l[0]] = {"ip": l[1], "puerto": l[2]}


# recibe
# informe de servicio activo
# peticion de operacion

# condicional if (mensaje[0] == o)
'''

def hilo_op():
    while True:
        message = server.recv_string() #peticion de resta
        print (type(message))
        if informe:
            
            print("recibido",str(message))
            socket.send_string("ok")
            print (message)
            adicionar(message)
            print (directorio)

        elif operacion:
            a + b'''


def report_service():
    while True:
        time.sleep(10)
        try:
            context = zmq.Context()
            r_service = context.socket(zmq.REQ)
            r_service.connect("tcp://localhost:8002")
            try:
                nombre_equipo = str(socket.gethostname())
                # r para avisar que vamos a reportar servicio
                msm = "r" + "," + "+" + "," + "nombre_equipo" + "," + "8002"
                r_service.send_string(msm)
                acuse = suma.recv_string()
                print(acuse)
            except:
                pass
        except:
            pass


def server():
    while True:
        time.sleep(3)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:8002")
            while True:
                message = socket.recv_string()
                print(message)
        except:
            pass


def client():
    while True:
        time.sleep(3)
        o = input('Operador: ')
        a = input('Ingrese el primero numero: ')
        b = input('Ingrese el segundo numero: ')

        # p porque vamos a hacer una peticion de operacion
        p = "p" + "," + o + "," + a + "," + b
        try:

            context = zmq.Context()
            suma = context.socket(zmq.REQ)
            suma.connect("tcp://localhost:8002")
            time.sleep(3)
            try:
                suma.send_string(p)
                resultado = suma.recv_string()
                print(resultado)
                print("conectando...")
            except KeyboardInterrupt:
                pass
            except:
                pass

        except KeyboardInterrupt:
            print("no se pudo conectar...")
        except:
            #print("no se pudo conectar")
            pass


        # peticion
        # cliente.Cliente
'''        print ("hilo cliente (suma) ejecutandose")
        o = input('Operador: ')
        msm_c = suma.recv_string()
        print(msm_c)
        puerto = directorio.get(msm_c)
        #print("puerto",str(puerto['puerto']))
        suma.send_string(str(puerto['puerto']))'''


#hilo_1 = threading.Thread(target=hilo_op)
# hilo_1.start()
hilo_c = threading.Thread(target=client)
hilo_c.start()
hilo_serv = threading.Thread(target=report_service)
hilo_serv.start()
#hilo_s = threading.Thread(target=server)
# hilo_s.start()
