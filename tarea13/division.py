import zmq
import socket
import report_service
import json

context = zmq.Context()
suma = context.socket(zmq.REQ)
suma.connect("tcp://localhost:8000")

result = {
}


# constantes
op = "/"
port = "8004"

# avisar que el servicio esta activo
nombre_equipo = str(socket.gethostname())
print(nombre_equipo, type(nombre_equipo))
reportJSON = report_service.reportService(op, nombre_equipo, port)
print(reportJSON, type(reportJSON))
#msm = "+"+","+nombre_equipo+","+"8001"
suma.send_pyobj(reportJSON)
acuse = suma.recv_string()
print(acuse)


# contexto para reply
context_rep = zmq.Context()
socket = context_rep.socket(zmq.REP)
socket.bind("tcp://*:"+port)
message = socket.recv_pyobj()



with open('data.json', 'r') as file:
    datas = json.load(file)
            
operando1 = datas.get("operandouno")
print(operando1)


with open('data.json', 'r') as file:
    datas = json.load(file)
            
operando2 = datas.get("operandodos")
print(operando2)


print("operandos: ", operando1, " ", operando2)

# --------------------operacion----------------------
try:
    resultado = str(int(operando1) / int(operando2))
except ZeroDivisionError:
    resultado = "no se puede hacer la operacion"


print("resultado: ", resultado)
result['respuesta'] = resultado

with open('result.json', 'w') as file:
        json.dump(result, file)

with open('result.json', 'r') as file:
    dat = json.load(file)

archivo = dat.get("respuesta")
print(archivo)

socket.send_pyobj(archivo)





