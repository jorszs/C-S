import zmq
import socket
context = zmq.Context()
suma = context.socket(zmq.REQ)
suma.connect("tcp://localhost:8000")


#avisar que el servicio esta activo
nombre_equipo = str(socket.gethostname())
msm = "+"+","+nombre_equipo+","+"8001"
suma.send_string(msm)
acuse = suma.recv_string()
print (acuse)


#message = suma.recv_string()
#message_str = message.decode('utf-8')

#print (message)

#l = message.split(",")
#print (l)

#respuesta = int(l[1]) + int(l[2])
#print (respuesta)
#respuesta = str(respuesta)
#suma.send_string(respuesta)
