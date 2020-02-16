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

    message = []
    message = socket.recv()
    message_str = message.decode('utf-8')

    operador = message[0]
    puerto = directorio.get(operador)

    socket.send(puerto)
