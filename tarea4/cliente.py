import zmq
'''context = zmq.Context()
# socket to talk to server
print ("connecting")
cliente = context.socket(zmq.REQ)
cliente.connect("tcp://localhost:8020")
'''


def Cliente():

    while True:
        context = zmq.Context()
        suma = context.socket(zmq.REQ)
        suma.connect("tcp://localhost:8020")
        o = input('Operador: ')
        # cliente.send_string(o)

        #respuesta = cliente.recv()
        #message_str = respuesta.decode('utf-8')

        #print ('Puerto: ', message_str)
        #print (type(respuesta))

        a = input('Ingrese el primero numero: ')
        b = input('Ingrese el segundo numero: ')

        p = o + "," + a + "," + b

        return (p)
        #print ('concatenacion', p)
        # print(respuesta)

        #socket = context.socket(zmq.REQ)
        #socket.connect("tcp://127.0.0.1:"+ message_str)
        # socket.send_string(p)

        #res = socket.recv_string()

        #print (res)

        # message_str = .decode('utf-8')
