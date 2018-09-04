import xmlrpc.client

a =int(input('Ingrese el primer numero: '))
b=int(input('Ingrese el segundo numero: '))

s = xmlrpc.client.ServerProxy('http://localhost:8001')
#print("la suma es: " + str(s.suma(a,b)))


#
#print(int.from_bytes(s.test(a,b).data, 'big'))

def test(a,b):
    with open("test2.txt", "wb") as handle:
        l = str(a)+','+str(b)
        w = l.encode()
        handle.write(w)

    with open("test2.txt", "rb") as handle:
        r = s.test(xmlrpc.client.Binary(handle.read()))
        print(r.data.decode())

test(a,b)