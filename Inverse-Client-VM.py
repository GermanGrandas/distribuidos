import xmlrpc.client
import random


s = xmlrpc.client.ServerProxy('http://23.96.112.79:8001')
#lista = [1,2,3,4]
def generateList(n):
    l = []
    for i in range(n):
        l.append(random.randint(0,1000))
    return l
n = int(input('Ingrese el tamaño de la lista: '))
lista = generateList(n)

def test(l):
    with open("test2.txt", "wb") as handle:
        for x in range(0,len(l)):
            if x < len(l)-1:
                string = str(l[x])+','
            else:
                string = str(l[x])
            handle.write(string.encode())
        handle.close()

    with open("test2.txt", "rb") as handle:
        d = s.test(xmlrpc.client.Binary(handle.read()))
        data =[int(y) for y in d.data.decode().split(',')]
        handle.close()
        return data


nuevaLista = test(lista)
print('Original: {} ---> Nueva: {}'.format(lista,nuevaLista))
