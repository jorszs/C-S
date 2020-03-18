import zerorpc
import math


class funciones_rpc:
    def op(self, p):
        print("logaritmo")
        l = p.split(",")
        try:
            respuesta = math.log(int(l[1]),int(l[2]))
        except:
            respuesta = "los argumentos estan fuera del dominio"
        print(respuesta)
        respuesta = str(respuesta)
        return respuesta


s = zerorpc.Server(funciones_rpc())
s.bind("tcp://*:8006")
s.run()
