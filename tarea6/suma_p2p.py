import zmq
import threading
import socket
import cliente
import time
import json

# puerto server: 8000

# contexto
#context = zmq.Context()

# avisar que el servicio esta activo
# i = informar que el servicio esta activo
# p = peticion de alguna operacion
# s = servicio encontrado (empieza a devolverse en la ruta, avisando que el servicio se encontro)


# ---------------------------

nombre_equipo = str(socket.gethostname())
# config

directorio = {
    "+": {"ip": nombre_equipo, "puerto": "8000"}
}


def adicionar(msm):
    l = msm.split("_")
    directorio[l[0]] = {"ip": l[1], "puerto": l[2]}


# recibe
# informe de servicio activo
# peticion de operacion


def report_service():
    while True:

        try:
            context = zmq.Context()
            r_service = context.socket(zmq.REQ)
            r_service.connect("tcp://localhost:8002")
            try:
                nombre_equipo = str(socket.gethostname())
                # r para avisar que vamos a reportar servicio
                msm = "r" + "_" + "+" + "_" + nombre_equipo + "_" + "8000"
                r_service.send_string(msm)
                acuse = suma.recv_string()
                print(acuse)
            except:
                pass
        except:
            pass
        time.sleep(10)


def server():
    while True:
        time.sleep(6)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:8000")
            try:
                message = socket.recv_string()
                print(message)
                l = message.split("_")
                # print(type(l[0]))
                #print("cualquier cosa")

                if l[0] == "p":
                    print("otra cosa")
                    respuesta = int(l[2]) + int(l[3])
                    print(respuesta)
                    respuesta = str(respuesta)
                    socket.send_string(respuesta)
                else:

                    msm_c = l[1]  # operador
                    a = directorio.get(msm_c)
                    if a == None:
                        adicionar(l)
                        print(directorio)
                    else:
                        pass
                # recibir mensaje de confirmacion (servicio encontrado)
            except:
                pass
        except:
            pass  # print("ffffff")


def client():
    while True:
        time.sleep(3)
        o = input('Operador: ')
        a = input('Ingrese el primero numero: ')
        b = input('Ingrese el segundo numero: ')

        # generamos el diccionario ruta
        info = directorio.get("+")
        ruta = {"+": info}
        ruta_str = json.dumps(ruta)
        # p porque vamos a hacer una peticion de operacion
        p = "p" + "_" + o + "_" + a + "_" + b + "_" + "+" + "_" + ruta_str

        if o == "+":
            resultado = int(a) + int(b)
            print(resultado)
        else:
            try:
                print("******")
                context = zmq.Context()
                suma = context.socket(zmq.REQ)
                suma.connect("tcp://localhost:8002")
                time.sleep(3)
                try:
                    suma.send_string(p)
                    #resultado = suma.recv_string()
                    # print(resultado)
                    # print("conectando...")
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
hilo_servicio = threading.Thread(target=report_service)
hilo_servicio.start()
hilo_server = threading.Thread(target=server)
hilo_server.start()
#hilo_s = threading.Thread(target=server)
# hilo_s.start()
