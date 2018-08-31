from xmlrpc.server import SimpleXMLRPCServer

def	suma_remota(a,b):
	return a+b
	
server = SimpleXMLRPCServer(("40.74.231.113", 8001))
server.register_function(suma_remota, "suma")
print ("soy el servidor y estoy corriendo por el pueto 8001")
server.serve_forever()
