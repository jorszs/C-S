import xml.etree.cElementTree as ET
from xml.dom import minidom
import zmq
context = zmq.Context()
# socket to talk to server
print("connecting")
cliente = context.socket(zmq.REQ)
try:
    cliente.connect("tcp://localhost:8020")
except:
    pass


def requestXML(o, a, b):
    root = ET.Element("root")
    #doc = ET.SubElement(root, "doc")

    operador = ET.SubElement(root, "operador", name="operador")
    operador.text = o  # "Texto de nodo1"

    elemento1 = ET.SubElement(root, "elemento1", name="elemento1")
    elemento1.text = a

    elemento2 = ET.SubElement(root, "elemento2", name="elemento2")
    elemento2.text = b

    # ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"
    arbol = ET.ElementTree(root)
    arbol.write("./request.xml")

    archivo = minidom.parse("./request.xml")
    return archivo


def crearXMLoperador(o):
    root = ET.Element("root")
    #doc = ET.SubElement(root, "doc")

    operador = ET.SubElement(root, "operador", name="operador")
    operador.text = o

    arbol2 = ET.ElementTree(root)
    arbol2.write("./operador.xml")

    # archivo = open("./operador.xml", "r")
    # return archivo


while True:

    o = input('Operador: ')
    crearXMLoperador(o)
    doc = minidom.parse("./operador.xml")
    #doc2 = open("./operador.xml")
    print("tipo: ", type(doc))
    cliente.send_pyobj(doc)
    print("operador.xml: ", doc)
    #op = doc.getElementsByTagName("operador")[0]
    #print("operador: ", op.firstChild.data)

    # for i in op:
    #   print("op: ", i.getAttribute("operador")[0])

    # cliente.send_string(o)

    respuesta = cliente.recv_pyobj()
    print("objeto puerto recibido: ", respuesta)
    puertoxml = respuesta.getElementsByTagName("puerto")[0]
    Puerto = puertoxml.firstChild.data
    print('Puerto: ', Puerto)
    # print (type(respuesta))

    a = input('Ingrese el primero numero: ')
    b = input('Ingrese el segundo numero: ')

    #p = o + "," + a + "," + b

    req = requestXML(o, a, b)

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:" + Puerto)
    socket.send_pyobj(req)

    res = socket.recv_pyobj()
    result_element = res.getElementsByTagName("respuesta")[0]
    result = result_element.firstChild.data
    print(result)

    # message_str = .decode('utf-8')
