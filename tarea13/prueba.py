import json

data = {}

o = input('Ingrese el operador: ')
data['operador'] = o
a = input('Ingrese el primer numero: ')
data['operando1'] = a
b = input('Ingrese el segundo numero: ')
data['operando2'] = b

'''p = o + ',' + a + ',' + b  

print(p)

l = p.split(",")'''


#data = data.split(",")


with open('data.json', 'w') as file:
    json.dump(data, file)

with open('data.json', 'r') as file:
    datos = json.load(file)



print(len(data))







if data['operador'] == '+':
    print('Suma')
    resultado = int(data['operando1']) + int(data['operando2'])
    print(resultado)
elif data['operador'] == '-':
    print('Resta')
    resultado = int(data['operando1']) - int(data['operando2'])
    print(resultado)
elif data['operador'] == '*':
    print('Multiplicacion')
    resultado = int(data['operando1']) * int(data['operando2'])
    print(resultado)
elif data['operador'] == '/':
    print('Division')
    resultado = int(data['operando1']) / int(data['operando2'])
    print(resultado)
elif data['operador'] == '**':
    print('Potencia')
    resultado = int(data['operando1']) ** int(data['operando2']) 
    print(resultado)


'''operador = {}
o = input('Operador: ')
operador['operador'] = o
print(operador)'''