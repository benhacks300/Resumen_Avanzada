import threading
import time

# La clase que queremos que sea un thread debe heredar de Thread proveniente de threading
class ContadorDeOvejas(threading.Thread):
    def __init__(self, nombre, cantidad_de_ovejas):
        super().__init__(name=nombre) # SIEMPRE DEBEMOS LLAMAR AL SUPER DE LA CLASE PADRE (Thread), es aquí donde debemos armar el thread con sus carácteristicas
        self.cantidad_ovejas = cantidad_de_ovejas

    # Este será nuestro start() de nuestro thread pero como estámos trabajando con OOP, se sobreescribe como run()
    def run(self):                                                                                 
        print(f"Me presento, soy el thread {self.name} y contaré la cantidad de {self.cantidad_ovejas} oveja{'s' if self.cantidad_ovejas > 1 else ''}")# Forma para editar un string dependiendo de su cantidad :p
        for oveja in range(1, self.cantidad_ovejas + 1):
            print(f"{self.name}: {oveja} oveja{'s' if oveja > 1 else ''}")
            time.sleep(1)
        print()
        print(f"Yo, {self.name}, terminé de contar las ovejas :3")
        print("**se duerme**\n")

# Creamos los threads
hilo_1 = ContadorDeOvejas("Ignacio", 20)
hilo_2 = ContadorDeOvejas("Simono", 10)
hilo_1.start() # Iniciamos el proceso con start, pero luego se sobreescribe por run()
hilo_1.join() # Con el método join(), estámos haciendo que nuestro hilo Ignacio ejecute sus acciones primero dentro del MainThread

hilo_2.start()
hilo_2.join() # Esperamos a que Ignacio termine para que Simono comience a contar

# Una vez sus hijos hayan terminado de contar, ahora es el padre que dirá hola
print("Soy el MainThread diciendo hola luego de esperar a mis hijos :3")