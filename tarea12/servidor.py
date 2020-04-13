import zmq
import threading
import time
import xml.etree.cElementTree as ET
from xml.dom import minidom

'''context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000")  # para las operaciones
sock_c = context.socket(zmq.REP)  # para cliente
sock_c.bind("tcp://*:8020")'''

directorio = {
}


def adicionar(op, ip, port):
    directorio[op] = {"ip": ip, "puerto": port}


def puertoXML(port):
    root = ET.Element("root")

    puerto = ET.SubElement(root, "puerto", name="puerto")
    puerto.text = port  # "Texto de nodo1"

    arbol = ET.ElementTree(root)
    arbol.write("./puerto.xml")

    archivo = minidom.parse("./puerto.xml")
    return archivo


def hilo_op():
    while True:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:8000")  # para las operaciones

        message = socket.recv_pyobj()

        socket.send_string("ok")

        operador = message.getElementsByTagName("operador")[0]
        op = operador.firstChild.data
        equipo = message.getElementsByTagName("equipo")[0]
        ip = equipo.firstChild.data
        puerto = message.getElementsByTagName("puerto")[0]
        port = puerto.firstChild.data

        print(op, ip, port)

        adicionar(op, ip, port)
        print(directorio)


def hilo_c():
    while True:
        try:
            context = zmq.Context()
            sock_c = context.socket(zmq.REP)  # para cliente
            sock_c.bind("tcp://*:8020")
            msm_c = sock_c.recv_pyobj()
            #print("xml: ", msm_c)
            #print("tipo: ", type(msm_c))
            operador = msm_c.getElementsByTagName("operador")[0]
            op = operador.firstChild.data
            #print("operador: ", type(op), op)
            servicio = directorio.get(op)
            if servicio:
                print("\nservicio: ", servicio)
                print("\npuerto: ", servicio["puerto"])
                archivo = puertoXML(servicio["puerto"])
                sock_c.send_pyobj(archivo)
        except KeyboardInterrupt:
            print("interrupcion")
            break
        except Exception as err:
            print("error: ", err)
            time.sleep(2)
            break


hilo_1 = threading.Thread(target=hilo_op)
hilo_1.start()
hilo_2 = threading.Thread(target=hilo_c)
hilo_2.start()
