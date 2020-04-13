import zmq
import socket
import report_service
import xml.etree.cElementTree as ET
from xml.dom import minidom

context = zmq.Context()
suma = context.socket(zmq.REQ)
suma.connect("tcp://localhost:8000")

# constantes
op = "+"
port = "8001"

# avisar que el servicio esta activo
nombre_equipo = str(socket.gethostname())
print(nombre_equipo, type(nombre_equipo))
reportXML = report_service.reportService(op, nombre_equipo, port)
print(reportXML, type(reportXML))
#msm = "+"+","+nombre_equipo+","+"8001"
suma.send_pyobj(reportXML)
acuse = suma.recv_string()
print(acuse)


# contexto para reply
context_rep = zmq.Context()
socket = context_rep.socket(zmq.REP)
socket.bind("tcp://*:"+port)
message = socket.recv_pyobj()

# print(message)
op_element = message.getElementsByTagName("operador")[0]
op = op_element.firstChild.data

operando1_element = message.getElementsByTagName("elemento1")[0]
operando1 = operando1_element.firstChild.data

operando2_element = message.getElementsByTagName("elemento2")[0]
operando2 = operando2_element.firstChild.data

#print("operandos: ", operando1, " ", operando2)

# --------------------operacion----------------------
resultado = int(operando1) + int(operando2)

#print("resultado: ", resultado)

root = ET.Element("root")
respuesta = ET.SubElement(root, "respuesta", name="operador")
respuesta.text = str(resultado)

arbol = ET.ElementTree(root)
arbol.write("./result.xml")

archivo = minidom.parse("./result.xml")

socket.send_pyobj(archivo)
