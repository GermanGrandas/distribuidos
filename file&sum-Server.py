from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

"""def	suma_remota(a,b):
	return a+b


def x(a,b):
	result = suma_remota(a,b)
	with open("test.txt", "wb") as handle:
		handle.write(result.to_bytes(2, byteorder='big'))

	with open("test.txt", "rb") as handle:
		return xmlrpc.client.Binary(handle.read())"""

def suma(lista):
	result = 0
	for x in lista:
		result+=x
	return result

def test_remoto(x):
	data =[int(y) for y in x.data.decode().split(',')]
	print(data)
	with open("test.txt", "wb") as handle:
		handle.write(str(suma(data)).encode())
	with open("test.txt", "rb") as handle:
		return xmlrpc.client.Binary(handle.read())



server = SimpleXMLRPCServer(("localhost", 8001))
#server.register_function(suma_remota, "suma")
server.register_function(test_remoto, "test")
print ("soy el servidor y estoy corriendo por el pueto 8001")
server.serve_forever()
