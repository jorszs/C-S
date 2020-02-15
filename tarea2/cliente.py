import zmq

context = zmq.Context()

# socket to talk to server
print ("connecting")
cliente = context.socket(zmq.REQ)
cliente.connect("tcp://localhost:8000")

while True:

    o = input('Operador: ')
    a = input('Ingrese el primero numero: ')
    b = input('Ingrese el segundo numero: ')

    '''cliente.send(o)
    cliente.send(a)
    cliente.send(b)'''

    p = o + "," + a + "," + b
    print ('concatenacion', p)

    cliente.send_string(p)

    print ('Resultado:',cliente.recv(1024))

    if 'exit' == input('Type "exit" to exit, no input to continue '):
        cliente.send(b"exit")
        cliente.close()
        exit()

'''for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))'''