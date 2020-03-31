import zerorpc
import sys
cancion = []


class dir_rpc:
    def pet(self, p):
        # print(p)
        print(sys.getsizeof(p))
        cancion.append(p)
        archivo = open("cancion.mp3", "wb")
        archivo.write(p)
        archivo.close()
        print("recibido")


s = zerorpc.Server(dir_rpc())
s.bind("tcp://*:8000")
s.run()
