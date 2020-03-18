import zerorpc


class funciones_rpc:
    def op(self, p):
        print("division")
        l = p.split(",")
        try:
            respuesta = int(l[1]) / int(l[2])
        except ZeroDivisionError:
            respuesta = "no se puede dividir entre cero"

        print(respuesta)
        respuesta = str(respuesta)
        return respuesta


s = zerorpc.Server(funciones_rpc())
s.bind("tcp://*:8004")
s.run()
