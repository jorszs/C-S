import zmq
import socket
import time
import threading
import json
import ast
# puerto server: 8004
yo = "/"
mi_port = "8004"


nombre_equipo = str(socket.gethostname())
# en el directorio se guardaran los servicios activos y donde localizarlos
# se guardan los servicios activos
directorio = {
    "/": {"ip": nombre_equipo, "puerto": "8004"}
}

# se guardan los servicios registrados
registrados = {
    "^": {"ip": nombre_equipo, "puerto": "8003"}
}


def adicionar(l):
    #l = msm.split("_")
    directorio[l[1]] = {"ip": l[2], "puerto": l[3]}


def report_service():
    while True:
        print("report ejecutando...")
        try:
            # recorrer el directorio y reportar el servicio

            for key in registrados:

                a = registrados.get(key)

                puerto = a["puerto"]
                print(puerto)

                try:
                    context = zmq.Context()
                    r_service = context.socket(zmq.REQ)
                    r_service.connect("tcp://localhost:" + puerto)
                    nombre_equipo = str(socket.gethostname())
                    # r para avisar que vamos a reportar servicio
                    msm = "r" + "_" + yo + "_" + nombre_equipo + "_" + mi_port
                    r_service.send_string(msm)
                    #acuse = suma.recv_string()
                    # print(acuse)
                except:
                    pass
        except:
            pass
        time.sleep(10)


# contexto para reply
def client():
    while True:
        time.sleep(3)
        o = input('Operador: ')
        a = input('Ingrese el primero numero: ')
        b = input('Ingrese el segundo numero: ')

        # generamos el diccionario ruta
        info = directorio.get(yo)
        ruta = {yo: info}
        ruta_str = json.dumps(ruta)
        # p porque vamos a hacer una peticion de operacion
        p = "p" + "_" + o + "_" + a + "_" + b + "_" + yo + "_" + ruta_str

        if o == yo:
            try:
                resultado = int(a) / int(b)
            except ZeroDivisionError:
                resultado = "no se pudo dividir por cero"
        else:
            try:
                print("******")
                print(directorio)

                for key in directorio:
                    if key != yo:
                        a = directorio.get(key)
                        host = a["ip"]
                        puerto = a["puerto"]
                        context = zmq.Context()
                        resta = context.socket(zmq.REQ)
                        resta.connect("tcp://"+host+":" + puerto)
                # time.sleep(3)
                        try:
                            print("enviando peticion")
                            resta.send_string(p)
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


def server():
    while True:
        print("corriendo servidor...")
        # time.sleep(2)
        try:
            context_rep = zmq.Context()
            socket = context_rep.socket(zmq.REP)
            socket.bind("tcp://*:8004")
            try:
                message = socket.recv_string()
                print("mensaje recibido", message)
                l = message.split("_")

                if l[0] == "p":
                    if l[1] == yo:
                        # aqui se devuelve enviando el puerto del sevicio hasta llegar a cliente

                        print(l)

                        ruta = l[5]  # se extrae el diccionario_string ruta
                        # se convierte a diccionario
                        ruta_dic = json.loads(ruta)
                        # agrego mi servicio/nodo a la ruta
                        ruta_dic[yo] = {"ip": nombre_equipo, "puerto": mi_port}
                        keys = []  # se guardaran las keys del diccionario ruta
                        # se extraen todas las keys (para saber cuantos nodos hay en la ruta)
                        for key in ruta_dic:
                            keys.append(key)
                        # se agrega el dato ruta actualizado a la lista
                        #l[5] = json.dumps(ruta_dic)
                        print("llaves de ruta: ", keys)

                        # si estamos ubicados en el ultimo nodo mas cercano al cliente cambiamos el token que esta al inicio del mensaje
                        # lo sabemos si en ruta solo quedan dos nodos: el cliente y el que tiene el servicio

                        # print(directorio)
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
                        host = a["ip"]
                        puerto = a["puerto"]
                        print("host y puerto", host, puerto)

                        context_respuesta = zmq.Context()
                        socket_respuesta = context_respuesta.socket(zmq.REQ)
                        socket_respuesta.connect(
                            "tcp://" + host + ":" + puerto)
                        socket_respuesta.send_string(nuevo_msm)
                    else:

                        cliente = l[4]
                        ruta_str = l[5]  # string de ruta

                        ruta_dic = json.loads(ruta_str)  # diccionario de ruta
                        print(ruta_dic)

                        ruta_dic[yo] = {"ip": nombre_equipo, "puerto": mi_port}
                        ruta_str = json.dumps(ruta_dic)
                        l[5] = ruta_str

                        nuevo_msm = '_'.join(l)

                        keys = []  # se guardaran las keys del diccionario ruta
                        # se extraen todas las keys (para saber cuantos nodos hay en la ruta)
                        for key in ruta_dic:
                            keys.append(key)

                        # tenemos que verificar no replicar el mensaje a los nodos que ya estan dentro de ruta
                        for key in directorio:
                            if key != yo and key != cliente and key not in keys:
                                info = directorio.get(key)
                                print(info)
                                context_replicar = zmq.Context()
                                socket_replicar = context_replicar.socket(
                                    zmq.REQ)
                                socket_replicar.connect(
                                    "tcp://" + info['ip'] + ":" + info['puerto'])
                                socket_replicar.send_string(nuevo_msm)
                elif l[0] == "r":
                    print("entro_r")
                    msm_c = l[1]  # operador
                    a = directorio.get(msm_c)
                    if a == None:
                        adicionar(l)
                        print("directorio_r", directorio)
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
                        aux = ruta_dic.get(l[1])  # "+"
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
                        try:
                            respuesta = int(l[2]) / int(l[3])
                        except ZeroDivisionError:
                            respuesta = "no se puede dividir entre cero"
                            print(respuesta)
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
            except:
                pass
        except:
            pass


hilo_c = threading.Thread(target=client)
hilo_c.start()
hilo_servicio = threading.Thread(target=report_service)
hilo_servicio.start()
hilo1 = threading.Thread(target=server)
hilo1.start()
