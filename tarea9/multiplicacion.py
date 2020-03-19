import zerorpc
import platform
import time
import threading
# constantes
yo = "*"
hostname = platform.uname()[1]
puerto = "8003"
server = "8000"


class funciones_rpc:
    def op(self, p):
        print("suma")
        l = p.split(",")
        respuesta = int(l[1]) * int(l[2])
        print(respuesta)
        respuesta = str(respuesta)
        return respuesta


# reportar servicio
def reportar():
    while True:
        c = zerorpc.Client()
        c.connect("tcp://localhost:"+server)
        mensaje = [yo, hostname, puerto]
        c.report(mensaje)
        time.sleep(5)


hilo_1 = threading.Thread(target=reportar)
hilo_1.start()

s = zerorpc.Server(funciones_rpc())
s.bind("tcp://*:"+puerto)
s.run()
