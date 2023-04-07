class Humano:
    
    def __init__(self, nombre, edad, peso): 
        self.nombre = nombre                                    
        self.edad = edad
        self.peso = peso
        self.vivo = True

    def ir_al_baño(self):
        self.peso -= 2
        print(f"{self.nombre} hizo del 2 y ahora pesa {self.peso} kg")

    def cumpleaños(self):
        self.edad += 1
        print(f"Es el cumpleaños de {self.nombre} y cumple {self.edad} años")

class Estudiante(Humano):
    def __init__(self, nombre, edad, peso, nota, generacion):
        super().__init__(nombre, edad, peso) # Le aclaramos que los atributos entregados son correspondientes a la clase Humano
        self.nota = nota
        self.generacion = generacion

    def agregar_decima_a_nota(self, decimas):
        self.nota += decimas / 10
        print(f"Nota queda en {self.nota}") 

estudiante_1  = Estudiante("Pepe", 23, 80, 5.5, 2020)
estudiante_1.ir_al_baño()
estudiante_1.cumpleaños()
estudiante_1.agregar_decima_a_nota(5)