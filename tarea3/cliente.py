import zmq

context = zmq.Context()

# socket to talk to server
print ("connecting")
cliente = context.socket(zmq.REQ)
cliente.connect("tcp://localhost:8000")


while True:

    o = raw_input('Operador: ')

    cliente.send_string(o)

    message = cliente.recv()
    message_str = message.decode('utf-8')

    print 'Puerto:', message

    '''a = raw_input('Ingrese el primero numero: ')
    b = raw_input('Ingrese el segundo numero: ')

    p = o + "," + a + "," + b

    print ('concatenacion', p)

    print ("estableciendo conexion")
    context_red = zmq.Context()
    socket = context_red.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:"+message)

    cliente.send_string(p)'''
