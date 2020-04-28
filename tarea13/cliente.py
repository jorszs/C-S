import zmq
import json

context = zmq.Context()
# socket to talk to server
print ("connecting")
cliente = context.socket(zmq.REQ)
cliente.connect("tcp://localhost:8020")





while True:
    context = zmq.Context()
    suma = context.socket(zmq.REQ)
    suma.connect("tcp://localhost:8020")
    data = {}
    o = input('Operador: ')
    data['operador'] = o


    with open('data.json', 'w') as file:
        json.dump(data, file)

    with open('data.json', 'r') as file:
        operadores = json.load(file)

    cliente.send_pyobj(operadores)
    print("operador.json: ", operadores)

    #-----------------------------
    respuesta = cliente.recv_pyobj()
    print("objeto puerto recibido: ", respuesta)
    
    with open('datos.json', 'r') as file:
         datas = json.load(file)
            
    respuesta = datas.get("puerto")
    print(respuesta)
    #cliente.send_string(operador)

    #respuesta = cliente.recv()
    #message_str = respuesta.decode('utf-8')

    #print ('Puerto: ', message_str)
    #print (type(respuesta))

    a = input('Ingrese el primero numero: ')

    data['operandouno'] = a


    with open('data.json', 'w') as file:
        json.dump(data, file)

    b = input('Ingrese el segundo numero: ')

    data['operandodos'] = b


    with open('data.json', 'w') as file:
        json.dump(data, file)

    
    with open('datos.json', 'r') as file:
         datas = json.load(file)

    #p = o + "," + a + "," + b
    
   
    #print ('concatenacion', p)
    #print(respuesta)

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:"+ respuesta)
    socket.send_pyobj(respuesta)

    res = socket.recv_pyobj()

    with open('result.json', 'r') as file:
        dates = json.load(file)

    archivo = dates.get("respuesta")
    print(archivo)


    #message_str = .decode('utf-8')