import zmq
import threading
import socket
import cliente
import time
import json

# puerto server: 8003
yo = "*"
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
    "+": {"ip": nombre_equipo, "puerto": "8003"}
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
                msm = "r" + "_" + "+" + "_" + nombre_equipo + "_" + "8003"
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
        # time.sleep(2)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:8000")
            try:
                message = socket.recv_string()
                print(message)
                l = message.split("_")
                # print(l)
                # print(type(l[0]))
                #print("cualquier cosa")

                if l[0] == "p":
                    if l[1] == "-":
                        # aqui se devuelve enviando el puerto del sevicio hasta llegar a cliente

                        print(l)

                        ruta = l[5]  # se extrae el diccionario_string ruta
                        # se convierte a diccionario
                        ruta_dic = json.loads(ruta)
                        # agrego mi servicio/nodo a la ruta
                        ruta_dic["-"] = {"id": nombre_equipo, "puerto": "8002"}
                        keys = []  # se guardaran las keys del diccionario ruta
                        # se extraen todas las keys (para saber cuantos nodos hay en la ruta)
                        for key in ruta_dic:
                            keys.append(key)
                        # se agrega el dato ruta actualizado a la lista
                        #l[5] = json.dumps(ruta_dic)
                        print("llaves de ruta: ", keys)

                        # si estamos ubicados en el ultimo nodo mas cercano al cliente cambiamos el token que esta al inicio del mensaje
                        # lo sabemos si en ruta solo quedan dos nodos: el cliente y el que tiene el servicio

                        context_respuesta = zmq.Context()
                        socket_respuesta = context_respuesta.socket(zmq.REQ)

                        print(directorio)
                        # traer la seccion de ruta para analizar cual fue el ultimo nodo agregado
                        # enviar el puerto y el host al ultimo nodo
                        # eliminar el ultimo nodo de la ruta
                        #a = directorio.get(l[4])

                        a = ruta_dic.get(keys[-2])
                        # eliminar penultimo nodo de ruta (el ultimo contiene la direccion del servicio buscado)
                        if len(keys) > 2:
                            ruta_dic.pop(keys[-2])

                        l[5] = json.dumps(ruta_dic)
                        l[0] = "s"
                        nuevo_msm = '_'.join(l)
                        print("nuevo mensaje:", nuevo_msm)
                        socket_respuesta.connect(
                            "tcp://" + a['ip'] + ":" + a['puerto'])
                        socket_respuesta.send_string(nuevo_msm)
                    else:


                        cliente = l[4]
                        ruta_str = l[5]  # string de ruta

                        ruta_dic = json.loads(ruta_str)  # diccionario de ruta
                        print(ruta_dic)

                        ruta_dic["-"] = {"ip": nombre_equipo, "puerto": "8002"}
                        ruta_str = json.dumps(ruta_dic)
                        l[5] = ruta_str

                        nuevo_msm = '_'.join(l)

                        for key in directorio:
                            if key != yo or key != cliente:
                                print("yolo")
                                info = directorio.get(key)
                                print(info)
                                context_replicar = zmq.Context()
                                socket_replicar = context_replicar.socket(
                                    zmq.REQ)
                                socket_replicar.connect(
                                    "tcp://" + info['ip'] + ":" + info['puerto'])
                                socket_replicar.send_string(nuevo_msm)
                elif l[0] == "r":

                    msm_c = l[1]  # operador
                    a = directorio.get(msm_c)
                    if a == None:
                        adicionar(l)
                        print(directorio)
                    else:
                        pass
                # recibir mensaje de confirmacion (servicio encontrado)
                elif l[0] == "s":

                    # si queda un solo elemento en ruta: conectar directamente
                    # sino seguir pasando el mensaje al penultimo nodo de ruta
                    ruta_str = l[5]
                    ruta_dic = json.loads(ruta_str)
                    keys = []
                    for key in ruta_dic:
                        keys.append(key)

                    if len(keys) == 2:

                        # conectarse directamente
                        aux = ruta_dic.get(l[1])  # "-"
                        #print("entro correctamente felicitaciones !!!", aux)
                        host = aux["id"]
                        port = aux["puerto"]
                        ruta_dic.pop(l[1])
                        #print("ruta: ", ruta_dic)
                        l[5] = json.dumps(ruta_dic)
                        nuevo_msm = '_'.join(l)

                        #print("este es el nuevo mensaje: ", nuevo_msm)
                        context_servicio = zmq.Context()
                        socket = context_servicio.socket(zmq.REQ)
                        socket.connect("tcp://"+host+":"+port)
                        socket.send_string(nuevo_msm)
                    # el servidor recibe conexion directa de
                    elif len(keys) == 1:
                        respuesta = int(l[2]) + int(l[3])
                        respuesta = "resultado"+"_" + \
                            l[1]+"_"+l[2]+"_"+l[3]+"_" + \
                            respuesta  # "resultado_-_2_3_1"
                        aux = ruta_dic.get(l[4])  # "+"
                        host = aux["id"]
                        port = aux["puerto"]
                        context_servicio = zmq.Context()
                        socket = context_servicio.socket(zmq.REQ)
                        socket.connect("tcp://"+host+":"+port)
                        socket.send_string(mensaje)
                    else:
                        aux = ruta_dic.get(keys[-2])  # [+,-,/]
                        host = aux["id"]
                        port = aux["puerto"]
                        ruta_dic.pop(keys[-2])  # [+,/]
                        context_servicio = zmq.Context()
                        socket = context_servicio.socket(zmq.REQ)
                        socket.connect("tcp://"+host+":"+port)
                        socket.send_string(mensaje)
                elif l[0] == "e":
                    print("entro a resultado")
                    # "resultado_-_2_3_1"
                    print(l)
                    print(str(l[2])+str(l[1])+str(l[3])+": "+str(l[4]))
                elif l[0] == "resultado":
                    # "resultado_-_2_3_1"
                    print(l[2]+l[1]+l[3]+": "+l[4])
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
                # time.sleep(3)
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




hilo_c = threading.Thread(target=client)
hilo_c.start()
hilo_servicio = threading.Thread(target=report_service)
hilo_servicio.start()
hilo_server = threading.Thread(target=server)
hilo_server.start()
