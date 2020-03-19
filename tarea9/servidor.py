import zerorpc
import threading

directorio = {
}


def adicionar(l):
    info = directorio.get(l[0])
    if info == None:
        directorio[l[0]] = {"ip": l[1], "puerto": l[2]}
    else:
        pass


class dir_rpc:
    def pet(self, p):
        l = p.split(",")
        print(p)
        operador = l[0]

        puerto = directorio.get(operador)
        print(puerto)
        if puerto == None:
            # el servicio no esta registrado
            print("el operador no se relaciona a alguna operacion guardada")
        else:
            # retornar el puerto del servicio encontrado
            print("estableciendo conexion")
            return (puerto)

    def report(self, p):
        print(type(p))
        adicionar(p)
        print(directorio)


s = zerorpc.Server(dir_rpc())
s.bind("tcp://*:8000")
s.run()
'''server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(dir_rpc())
print("soy un servidor implementado con clases")
server.serve_forever()'''


'''while True:
    def suma(p):
        print p
        l = p.split(",")
        operador = lista[0]
        puerto = directorio.get(operador)
        if puerto == None:
            print ("el operador no se relaciona a alguna operacion guardada")
        else:
            print ("estableciendo conexion")

server = SimpleXMLRPCServer(("localhost", 8000))
class funciones_rpc:
    def suma(self, p):
        print p
        l = p.split(",")
        respuesta = int(l[0]) + int(l[1])
        print respuesta
        respuesta = str(respuesta)

        #print (type(l))
        #respuesta = int(l[0]) + int(l[1])

        return respuesta
    def resta(self, p):
        print p
        l = p.split(",")
        respuesta = int(l[0]) - int(l[1])
        print respuesta
        respuesta = str(respuesta)
        return respuesta

    def multiplicacion(self, p):
        print p
        l = p.split(",")
        respuesta = int(l[0]) * int(l[1])
        print respuesta
        respuesta = str(respuesta)
        return respuesta

    def division(self, p):
        print p
        l = p.split(",")
        respuesta = int(l[0]) / int(l[1])
        print respuesta
        respuesta = str(respuesta)
        return respuesta

    def potencia(self, p):
        print p
        l = p.split(",")
        respuesta = int(l[0]) ** int(l[1])
        print respuesta
        respuesta = str(respuesta)
        return respuesta

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(funciones_rpc())
print("soy un servidor implementado con clases")
server.serve_forever()'''
