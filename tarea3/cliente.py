import zmq
context = zmq.Context()
# socket to talk to server
print ("connecting")
cliente = context.socket(zmq.REQ)
cliente.connect("tcp://localhost:8000")


while True:

    o = raw_input('Operador: ')
    cliente.send_string(o)

    respuesta = cliente.recv()
    message_str = respuesta.decode('utf-8')

    print 'Puerto: ', respuesta

    a = raw_input('Ingrese el primero numero: ')
    b = raw_input('Ingrese el segundo numero: ')

    p = o + "," + a + "," + b

    print ('concatenacion', p)

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:"+ respuesta)
    socket.send_string(p)

    res = socket.recv_string()

    print res

    #message_str = .decode('utf-8')
