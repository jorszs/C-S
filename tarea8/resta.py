import zerorpc


class funciones_rpc:
    def op(self, p):
        print("resta")
        l = p.split(",")
        respuesta = int(l[1]) - int(l[2])
        print(respuesta)
        respuesta = str(respuesta)
        return respuesta


s = zerorpc.Server(funciones_rpc())
s.bind("tcp://*:8002")
s.run()
