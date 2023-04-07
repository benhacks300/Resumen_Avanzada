from abc import ABC, abstractclassmethod
from secrets import choice

class Personaje(ABC): # Ésta es la plantilla por la cual nuestras próximas clases deberán basarse
    def __init__(self, nombre, color, tareas):
        self.color = color 
        self.tareas = tareas
        self.nombre = nombre
    
    # Método que deberá si o si tener las clases hijas (Subclases)
    @abstractclassmethod 
    def hacer_tareas(self):
        pass
    
    @abstractclassmethod
    def habilidad_especial(self):
        print(f"{self.nombre} utiliza su habilidad especial")

    # Métodos que son generales para las otras clases, éstos estarán igualmente de disponibles para las clases hijas
    def presionar_boton(self): 
        print(f"¡¡{self.nombre} llamo a una reunión urgente")

    def revisar_camaras(self):
        print(f"{self.nombre} revisa las cámaras")

    def revisar_registros(self):
        print(f"{self.nombre} revisa el registro de ingresos")

class Impostor(Personaje):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # "Importamos", los atributos provenientes de la clase padre (Personaje)
        self.sabotajes = "" # Añadimos los atributos propios de la clase hija

        # SIEMPRE DEBEMOS IMPLEMENTAR LAS ABSTRACTCLASSMETHOD HECHAS DE LA CLASE PADRE, sino la clase hija no puede funcionar :c
        def hacer_tareas(self): 
            super().hacer_tareas

        def habilidad_especial(self, destino):
            super().habilidad_especial
            print(f"{self.nombre} ingresa en las alcantarilas y se dirije a {destino}")
        