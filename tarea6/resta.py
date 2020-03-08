import zmq
import socket
import time
import threading

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
                        #op = l[4]

                        print(directorio)
                        a = directorio.get(l[4])
                        # print(a)
                        socket_respuesta.connect(
                            "tcp://" + a['ip'] + ":" + a['puerto'])
                        socket_respuesta.send_string(respuesta)
                    else:
                        # replica la peticion
                        ruta = {"+": {"id": "localhost", "puerto": "8000"},
                                "/": {"id": "localhost", "puerto": "8000"}}

                        print("kkkkkkk")
                        yo = "-"
                        cliente = l[4]
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
                                socket_replicar.send_string("hola guapo")
                            # if key == yo and key == cliente:
                            #    print("key")
                            '''info = directorio.get(key)
                                context_replicar = zmq.Context()
                                socket_replicar = context_replicar.socket(
                                    zmq.REQ)
                                socket_replicar.connect(
                                    "tcp://" + info['ip'] + ":" + info['puerto'])
                                socket_replicar.send_string(respuesta)'''

                    # buscar el servicio en el directorio propio
                    # sino: enviar la peticion a otros servidores --
                    '''msm_c = l[1]  # operador (+,-,*)
                    a = directorio.get(msm_c)  # puerto del servicio solicitado
                    b = directorio.get(l[4])
                    # mandar al cliente el puerto del servicio
                    if a != None:
                        context_rep = zmq.Context()
                        socket = context_rep.socket(zmq.REQ)
                        socket.connect("tcp://"a["ip"]+":"+a["puerto"])'''

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
