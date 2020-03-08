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
    #l = msm.split(",")
    directorio[l[1]] = {"ip": l[2], "puerto": l[3]}

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

                if l[0] == "p":
                    if l[1] == "-":
                        # aqui se devuelve enviando el puerto del sevicio hasta llegar a cliente

                        print("otra cosa")
                        print(l)
                        respuesta = int(l[2]) - int(l[3])
                        print(respuesta)
                        respuesta = str(respuesta)
                        context_respuesta = zmq.Context()
                        socket_respuesta = context_respuesta.socket(zmq.REQ)
                        print("------------")

                        print(directorio)
                        # traer la seccion de ruta para analizar cual fue el ultimo nodo agregado
                        # enviar el puerto y el host al ultimo nodo
                        # eliminar el ultimo nodo de la ruta
                        a = directorio.get(l[4])
                        # print(a)
                        socket_respuesta.connect(
                            "tcp://" + a['ip'] + ":" + a['puerto'])
                        socket_respuesta.send_string(respuesta)
                    else:

                        yo = "-"
                        cliente = l[4]
                        ruta_str = l[5] + "," + l[6]  # string de ruta

                        ruta_dic = json.loads(ruta_str)  # diccionario de ruta
                        print(ruta_dic)

                        ruta_dic["-"] = {"ip": nombre_equipo, "puerto": "8002"}
                        ruta_str = json.dumps(ruta_dic)
                        l[5] = ruta_str
                        l.pop(6)
                        nuevo_msm = ','.join(l)

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

                else:

                    msm_c = l[1]  # operador
                    a = directorio.get(msm_c)
                    if a == None:
                        adicionar(l)
                        # print(directorio)
                    else:
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
