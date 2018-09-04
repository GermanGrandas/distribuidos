from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


def invertir(l):
	nl = []
	for x in range(len(l)-1,-1,-1):
		nl.append(l[x])
	return nl


def test_remoto(x):
	data =[int(y) for y in x.data.decode().split(',')]
	l = invertir(data)
	with open("test.txt", "wb") as handle:
		for x in range(0,len(l)):
			if x < len(l)-1:
				string = str(l[x])+','
			else:
				string = str(l[x])
			handle.write(string.encode())
		handle.close()
	with open("test.txt", "rb") as handle:
		return xmlrpc.client.Binary(handle.read())
		handle.close()



server = SimpleXMLRPCServer(("localhost", 8001))
server.register_function(test_remoto, "test")
print ("soy el servidor y estoy corriendo por el puerto 8001")
server.serve_forever()
