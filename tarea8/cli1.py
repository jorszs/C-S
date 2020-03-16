import zerorpc
#a =input('Ingrese el primer numero: ')
#b =input('Ingrese el segundo numero: ')
#l=[1,2,3,4,5,6,7]

#proxy = xmlrpclib.ServerProxy("http://localhost:8000")


while True:

    o = input('Ingrese el operando: ')
    a = input('Ingrese el primer numero: ')
    b = input('Ingrese el segundo numero: ')
    p =  o + ',' + a + ',' + b
    c = zerorpc.Client()
    c.connect("http://localhost:8000")
    #print (c.hol(p))
