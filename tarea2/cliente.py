import zmq

context = zmq.Context()

# socket to talk to server
print ("connecting")
cliente = context.socket(zmq.REQ)
cliente.connect("tcp://localhost:8000")

while True:

    o = raw_input('Operador: ')
    a = raw_input('Ingrese el primero numero: ')
    b = raw_input('Ingrese el segundo numero: ')

    '''cliente.send(o)
    cliente.send(a)
    cliente.send(b)'''

    p = o + "," + a + "," + b
    print ('concatenacion', p)

    cliente.send_string(p)
    
    resultado = (cliente.recv(1024).decode('utf-8'))
    print ('Resultado:',resultado)

    if 'exit' == input('Type "exit" to exit, no input to continue '):
        cliente.send(b"exit")
        cliente.close()
        exit()
