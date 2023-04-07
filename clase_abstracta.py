from abc import ABC, abstractclassmethod
from secrets import choice

class Personaje(ABC):
    def __init__(self, nombre, color, tareas):
        self.color = color 
        self.tareas = tareas
        self.nombre = nombre
    
    @abstractclassmethod
    def hacer_tareas(self):
        pass
    
    @abstractclassmethod
    def habilidad_especial(self):
        print(f"{self.nombre} utiliza su habilidad especial")

    def presionar_boton(self):
        print(f"¡¡{self.nombre} llamo a una reunión urgente")

    def revisar_camaras(self):
        print(f"{self.nombre} revisa las cámaras")

    def revisar_registros(self):
        print(f"{self.nombre} revisa el registro de ingresos")

class Impostor(Personaje):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sabotajes = ""

        def hacer_tareas(self):
            super().hacer_tareas

        def habilidad_especial(self, destino):
            super().habilidad_especial
            print(f"{self.nombre} ingresa en las alcantarilas y se dirije a {destino}")