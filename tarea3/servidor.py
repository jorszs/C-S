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

while True:

    message = socket.recv_string()
    #message_str = message.decode('utf-8')
    print message
    puerto = directorio.get(message)
    socket.send(puerto)
    message_str = message.decode('utf-8')
