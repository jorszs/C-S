import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000") 

directorio = {
    '+':'8001',
    '-':'8002',
    '*':'8003',
    '/':'8004',
    '^':'8005',
    'log':'8006'
}

def redireccionar(lista,message):
    operador = lista[0]
    puerto = directorio.get(operador)
    if puerto == None:
        print ("el operador no se relaciona a alguna operacion guardada")
    else:
        print ("estableciendo conexion")
        context_red = zmq.Context()
        socket = context_red.socket(zmq.REQ)
        socket.connect("tcp://127.0.0.1:"+puerto)
        socket.send(message)
        respuesta = socket.recv()
        print ("la respuesta es: "+ respuesta.decode('utf-8'))
        return respuesta


while True:
    #wait for next request from client
    #redireccionar('+')
    #puerto = directorio.get('p')
    #if puerto == None:
    #    print ("nada")
    message = socket.recv()
    message_str = message.decode('utf-8')
    l = message_str.split(",")
    print (l)
    #llamada a funcion redireccionar para conectarse con el servidor que tenga la operacion
    respuesta = redireccionar(l,message)
    print ("receive request %s" % message)
    print (respuesta,type(respuesta))
    
    #enviar respuesta a cliente
    socket.send(respuesta)
    #do something

    #send reply for client
    #socket.send(b"hi from servidor")

