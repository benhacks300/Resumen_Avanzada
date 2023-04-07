import threading 
import time

# Haremos que nuestro thread "padre", se presente con su nombre, este es quién siempre ejecuta nuestro script
print(f"Holaa, soy el thread padre con nombre {threading.current_thread().name} y seré yo quien ejecute tu script :3\n")

# Esta será la función creada que se ejecutará en nuestro thread desde el atributo "target"
def contador_independiente(valor: int):
    nombre_thread = threading.current_thread().name # Con esta función podemos obtener el nombre con el cual nuestro thread ha sido creado 
    print(f"Me presento, soy el thread {nombre_thread} y voy a contar hasta {valor}")
    for i in range(1, valor + 1):
        print(f"{nombre_thread}: {i}...\n")
        time.sleep(1) # La función sleep nos permite realizar una simulación del tiempo te trabajo del thread
    print("He terminado de contar :3\n")

# Para crear un thread, este se debe instanciar como una clase común y corriente
mi_hilo = threading.Thread(target=contador_independiente, kwargs={"valor": 10}, name="Benjamin")
mi_hilo.start()
mi_hilo.join()

tiempo = 5
hilo_con_tiempo_de_espera = threading.Timer(tiempo, contador_independiente, args=(10,)) # Este hilo comienza su ejecución luego de 5 segundos
hilo_con_tiempo_de_espera.start() 
for i in range(1, tiempo+1):
    print(f"Contando... {i}")
    time.sleep(1)
print()
hilo_con_tiempo_de_espera.join()

print("MainThread ha terminado su pega")
