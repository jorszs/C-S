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
