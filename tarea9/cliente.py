import zerorpc
#a =input('Ingrese el primer numero: ')
#b =input('Ingrese el segundo numero: ')
# l=[1,2,3,4,5,6,7]

#proxy = xmlrpclib.ServerProxy("http://localhost:8000")


while True:

    o = input('Ingrese el operando: ')
    c = zerorpc.Client()
    c.connect("tcp://localhost:8000")
    puerto = c.pet(o)
    print(type(puerto))
    a = input('Ingrese el primer numero: ')
    b = input('Ingrese el segundo numero: ')
    p = o + ',' + a + ',' + b

    c_o = zerorpc.Client()
    c_o.connect("tcp://localhost:"+puerto)
    print(c_o.op(p))
