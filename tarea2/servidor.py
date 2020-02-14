import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000") # el "*" conecta con el localhost

directorio = {
    '+':'8001',
    '-':'8002',
    '*':'8003',
    '/':'8004',
    '^':'8005',
    'log':'8006'
}

def redireccionar(lista):
    operador = lista[0]
    puerto = directorio.get(operador)
    if puerto == None:
        print ("el operador no se relaciona a alguna operacion guardada")
    else:
        print ("estableciendo conexion")
        context_red = zmq.Context()
        socket = context_red.socket(zmq.REQ)
        socket.bind("tcp://*:"+puerto)
        socket.send(b"hola")


while True:
    #wait for next request from client
    redireccionar('+')
    #puerto = directorio.get('p')
    #if puerto == None:
    #    print ("nada")
    message = socket.recv()
    print ("receive request %s" % message)

    #do something

    #send reply for client
    socket.send(b"hi from servidor")

