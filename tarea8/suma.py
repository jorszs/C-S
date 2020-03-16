import zerorpc

class funciones_rpc:
    def suma(self, p):
        l = p.split(",")
        respuesta = int(l[1]) + int(l[2])
        print (respuesta)
        respuesta = str(respuesta)
        return respuesta

s = zerorpc.Server(funciones_rpc())
s.bind("http://localhost:8000")
s.run()
