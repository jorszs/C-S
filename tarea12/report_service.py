import xml.etree.cElementTree as ET
from xml.dom import minidom
import socket


def reportService(operacion, ip, port):
    puerto = '8001'
    equipo = str(socket.gethostname())
    print(equipo)

    root = ET.Element("root")
    #servicio = ET.SubElement(root, "servicio")

    operador = ET.SubElement(root, "operador", name="operador")
    operador.text = operacion  # "Texto de nodo1"

    equipo = ET.SubElement(root, "equipo", name="equipo")
    equipo.text = ip

    puerto = ET.SubElement(root, "puerto", name="puerto")
    puerto.text = port

    # ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"
    arbol = ET.ElementTree(root)
    arbol.write("./reportService.xml")

    archivo = minidom.parse("./reportService.xml")
    return archivo
