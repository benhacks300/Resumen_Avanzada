import threading
import time

def saludar():
    
    for i in range(10):
        nombre_thread = threading.current_thread().name
        print(f"Hola, mi nombre es {nombre_thread} :p")


hilo_1 = threading.Thread(name="Juanito", target=saludar)
hilo_1.start()
hilo_1.join()

print("Fin del programa")