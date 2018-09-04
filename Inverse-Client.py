import xmlrpc.client


s = xmlrpc.client.ServerProxy('http://localhost:8001')
lista = [1,2,3,4]

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