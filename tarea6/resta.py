import zmq
import socket
import time
import threading
import json
import ast
# puerto server: 8002

nombre_equipo = str(socket.gethostname())
# en el directorio se guardaran los servicios activos y donde localizarlos
directorio = {
    "-": {"ip": nombre_equipo, "puerto": "8002"},
    "*": {"ip": nombre_equipo, "puerto": "8000"}
}


def adicionar(l):
    #l = msm.split("_")
    directorio[l[1]] = {"ip": l[2], "puerto": l[3]}

# contexto para reply


def server():
    while True:
        # time.sleep(2)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:8002")
            try:
                message = socket.recv_string()
                # print(message)
                l = message.split("_")

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

                        yo = "-"
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
                    print("estas son las keys: ", keys)
                    if len(keys) == 2:
                        # conectarse directamente
                        aux = ruta_dic.get(l[1])  # "-"
                        host = aux["id"]
                        port = aux["puerto"]
                        ruta_dic.pop(l[1])
                        context_servicio = zmq.Context()
                        socket = context_servicio.socket(zmq.REQ)
                        socket.connect("tcp://"+host+":"+port)
                        socket.send_string(message)
                    # el servidor recibe conexion directa de
                    elif len(keys) == 1:
                        print("entro correctamente felicitaciones !!!")
                        respuesta = int(l[2]) - int(l[3])
                        print(respuesta)
                        respuesta = "e"+"_" + \
                            l[1]+"_"+l[2]+"_"+l[3]+"_" + \
                            str(respuesta)  # "resultado_-_2_3_1"
                        print(respuesta)
                        aux = ruta_dic.get(l[4])  # "+"
                        host = aux.get("ip")
                        port = aux.get("puerto")
                        print("aux", aux)
                        print("host", host)
                        print("puerto", port)
                        context_servicio = zmq.Context()
                        socket_res = context_servicio.socket(zmq.REQ)
                        # socket_res.connect("tcp://"+host+":"+port)
                        socket_res.connect("tcp://"+host+":"+port)
                        socket_res.send_string(respuesta)
                    else:
                        aux = ruta_dic.get(keys[-2])  # [+,-,/]
                        host = aux["id"]
                        port = aux["puerto"]
                        ruta_dic.pop(keys[-2])  # [+,/]
                        context_servicio = zmq.Context()
                        socket = context_servicio.socket(zmq.REQ)
                        socket.connect("tcp://"+host+":"+port)
                        socket.send_string(mensaje)
                elif l[0] == "resultado":
                    # "resultado_-_2_3_1"
                    print(l[2]+l[1]+l[3]+": "+l[4])
            except:
                pass
        except:
            pass  # print("ffffff")


hilo1 = threading.Thread(target=server)
hilo1.start()
'''
l = message.split("_")
print (l)

respuesta = int(l[1]) - int(l[2])
print (respuesta)
respuesta = str(respuesta)
socket.send_string(respuesta)'''
