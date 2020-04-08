import threading
import time
import asyncio
import datetime


def f1():
    time.sleep(2)
    print("hola")
    # print(string)


def f2():
    time.sleep(2)
    print("mundo")


def crearHilos():
    lista = []
    inicio = datetime.datetime.now()
    for i in range(10):
        def funcion():
            lista.append(i)

        a = threading.Thread(target=funcion)
        a.start()
        a.join()
    fin = datetime.datetime.now()
    print(lista)
    print("tiempo: "+str(fin.second - inicio.second))


a = threading.Thread(name="h_1", target=f1)
b = threading.Thread(name="h_2", target=f2)

'''a.start()
b.start()

a.join()
b.join()
'''
crearHilos()


'''lista = [{"ip": 2}, {"ip": 1}, {"ip": 3}]
lista.sort(key=lambda dict: dict["ip"])
print(lista)'''

# *************************
'''req = "cancion"
res = {
    "id": i,
    "song":"ndjf55f8fhdnf55df56"
}

#cliente
lista.append(res)
lista.order([id])

for i in lista():
    archivo.write(i[song])
'''


# **************************

# crearHilos()
