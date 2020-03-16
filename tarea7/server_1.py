import zmq
import socket
import time
import threading
import json
import ast
# puerto server: 8003
yo = "s1"
mi_port = "8050"

nombre_equipo = str(socket.gethostname())
# en el directorio se guardaran los servicios activos y donde localizarlos
directorio = {
    "^": {"ip": nombre_equipo, "puerto": "8003"},
}

# se guardan los servicios registrados
registrados = {
    "-": {"ip": nombre_equipo, "puerto": "8002"},
    "/": {"ip": nombre_equipo, "puerto": "8004"},
    "log": {"ip": nombre_equipo, "puerto": "8005"}


    # "^": {"ip": nombre_equipo, "puerto": "8003"},
}

# diccionario de servidores
servers = {
    "s2": {"ip": nombre_equipo, "puerto": "8051"},
    # "s3": {"ip": nombre_equipo, "puerto": "8052"}
}

# diccionario de servicios
servicios = {
}


def adicionar(l):
    #print("agregando servicio")
    servicios[l[1]] = {"ip": l[2], "puerto": l[3]}
    print(servicios)


def adicionar_serv(l):
    print("agregando servidor")
    servers[l[1]] = {"ip": l[2], "puerto": l[3]}
    print(servers)


def report_service():
    while True:
        print("report ejecutando...")
        try:
            # recorrer el directorio y reportar servicios
            for key in servers:
                try:
                    a = servers.get(key)
                    puerto = a["puerto"]
                    print("r ", puerto)
                    context = zmq.Context()
                    r_service = context.socket(zmq.REQ)
                    r_service.connect("tcp://localhost:" + puerto)
                    nombre_equipo = str(socket.gethostname())
                    # r para avisar que vamos a reportar servicio
                    # yo + "_" + nombre_equipo + "_" + mi_port
                    msm = "rs" + "_" + yo + "_" + nombre_equipo + "_" + mi_port
                    try:
                        r_service.send_string(msm)
                        print("report enviado", msm)
                    except KeyboardInterrupt:
                        pass
                    except:
                        pass
                except KeyboardInterrupt:
                    pass
                except:
                    pass
            # acuse = suma.recv_string()
            # print(acuse)
        except KeyboardInterrupt:
            pass
        except:
            pass
        time.sleep(10)

# contexto para reply


def server():
    while True:
        # time.sleep(2)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:"+mi_port)
            try:
                message = socket.recv_string()
                print("mensaje recibido", message)
                l = message.split("_")

                if l[0] == "p":
                    # la peticion esta en mi lista de servicios ?
                    svc = servicios.get(l[1])
                    if svc != None:
                        print("entraaaaaaa")
                        # aqui se devuelve enviando el puerto del sevicio hasta llegar a cliente
                        ip_servicio = svc["ip"]
                        puerto_servicio = svc["puerto"]
                        print(l)

                        ruta = l[5]  # se extrae el diccionario_string ruta
                        # se convierte a diccionario
                        ruta_dic = json.loads(ruta)
                        # agrego servicio encontrado en mi diccionario servicios a la ruta
                        ruta_dic[l[1]] = {
                            "ip": ip_servicio, "puerto": puerto_servicio}
                        keys = []  # se guardaran las keys del diccionario ruta
                        # se extraen todas las keys (para saber cuantos nodos hay en la ruta)
                        for key in ruta_dic:
                            keys.append(key)
                        # se agrega el dato ruta actualizado a la lista
                        # l[5] = json.dumps(ruta_dic)
                        print("llaves de ruta: ", keys)

                        # si estamos ubicados en el ultimo nodo mas cercano al cliente cambiamos el token que esta al inicio del mensaje
                        # lo sabemos si en ruta solo quedan dos nodos: el cliente y el que tiene el servicio

                        context_respuesta = zmq.Context()
                        socket_respuesta = context_respuesta.socket(zmq.REQ)

                        # print(directorio)
                        # traer la seccion de ruta para analizar cual fue el ultimo nodo agregado
                        # enviar el puerto y el host al ultimo nodo
                        # eliminar el ultimo nodo de la ruta
                        # a = directorio.get(l[4])

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

                        cliente = l[4]  # operacion del cliente
                        ruta_str = l[5]  # string de ruta

                        ruta_dic = json.loads(ruta_str)  # diccionario de ruta
                        print("replicando peticion. ruta: ", ruta_dic)

                        ruta_dic[yo] = {"ip": nombre_equipo, "puerto": mi_port}
                        ruta_str = json.dumps(ruta_dic)
                        l[5] = ruta_str

                        nuevo_msm = '_'.join(l)

                        keys = []  # se guardaran las keys del diccionario ruta
                        # se extraen todas las keys (para saber cuantos nodos hay en la ruta)
                        for key in ruta_dic:
                            keys.append(key)

                        # tenemos que verificar no replicar el mensaje a los nodos que ya estan dentro de ruta
                        for key in servers:
                            if key != yo and key != cliente and key not in keys:
                                info = servers.get(key)
                                print("replicando a nodo:", info)
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
                        # print(directorio)
                    else:
                        pass
                elif l[0] == "rs":

                    msm_c = l[1]  # operador
                    a = servers.get(msm_c)
                    if a == None:
                        adicionar_serv(l)
                        # print(directorio)
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
                        host = aux["ip"]
                        port = aux["puerto"]

                        ruta_dic.pop(l[1])
                        l[5] = json.dumps(ruta_dic)
                        nuevo_msm = '_'.join(l)

                        context_servicio = zmq.Context()
                        socket = context_servicio.socket(zmq.REQ)
                        socket.connect("tcp://"+host+":"+port)

                        socket.send_string(nuevo_msm)

                    # el servidor recibe conexion directa de
                    elif len(keys) == 1:
                        print("entro correctamente felicitaciones !!!")
                        respuesta = int(l[2]) ** int(l[3])
                        print(respuesta)
                        respuesta = "e"+"_" + \
                            l[1]+"_"+l[2]+"_"+l[3]+"_" + \
                            str(respuesta)  # "resultado_-_2_3_1"
                        print(respuesta)
                        aux = ruta_dic.get(l[4])  # "-"
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
                    elif len(keys) > 2:
                        aux = ruta_dic.get(keys[-2])  # [+,-,/]
                        print("nodo intermedio *******************************", aux)
                        host = aux["ip"]
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
            except KeyboardInterrupt:
                pass
            except:
                pass
        except KeyboardInterrupt:
            pass
        except:
            pass


hilo_servicio = threading.Thread(target=report_service)
hilo_servicio.start()
hilo1 = threading.Thread(target=server)
hilo1.start()
