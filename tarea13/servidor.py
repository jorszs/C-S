import zmq
import threading
import json
import time

'''context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000") #para las operaciones
sock_c = context.socket(zmq.REP)#para cliente
sock_c.bind("tcp://*:8020")'''

directorio = {
}

def adicionar(op, ip, port):
    directorio[op] = {"ip":ip,"puerto":port}

def puertoJSON(port):
    p = {}
    p['puerto'] = port
    with open('p.json', 'w') as file:
        json.dump(p, file)
    return p

def hilo_op():
    while True:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:8000")  # para las operaciones

        message = socket.recv_pyobj()
        print("recibido",str(message))
        socket.send_string("ok")

        with open('datos.json', 'r') as file:
            datas = json.load(file)
        
        op = datas.get("operador")
        print("uno",op)
        ip = datas.get("equipo")
        print("dos", ip)
        port = datas.get("puerto")
        print("tres",port)
        

        print ("segundomsn:" , message)
        adicionar(op, ip, port)
        print ("tercermsn",directorio)

def hilo_c():
    while True:
        try:
            context = zmq.Context()
            sock_c = context.socket(zmq.REP)  # para cliente
            sock_c.bind("tcp://*:8020")
            msm_c = sock_c.recv_pyobj()
            print("json" , msm_c)

            with open('data.json', 'r') as file:
                datas = json.load(file)
            
            op = datas.get("operador")
            print(op)

            servicio = directorio.get(op)

            if servicio:
                    print("\nservicio: ", servicio)
                    print("\npuerto: ", servicio["puerto"])
                    archivo = servicio["puerto"]
                    sock_c.send_pyobj(archivo)
        except KeyboardInterrupt:
            print("interrupcion")
            break
        except Exception as err:
            print("error: ", err)
            time.sleep(2)
            break

        '''puerto = directorio.get(msm_c)
        print("puerto",str(puerto['puerto']))
        sock_c.send_string(str(puerto['puerto']))'''



hilo_1 = threading.Thread(target=hilo_op)
hilo_1.start()
hilo_2 = threading.Thread(target=hilo_c)
hilo_2.start()