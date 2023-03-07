class Gato:

  def __init__(self, nombre):
    self.nombre = nombre

  def __str__(self): # Imprime la localización del objeto en la ram [<__main__.Gato object at 0x000001D132F4E150>]
    return self.nombre

  def __repr__(self): # Imprime la clase y sus atributos [Gato: Colores]
    return f"Gato: {self.nombre}"

lista = list()
gato = Gato("Colores")

lista.append(gato)
print(lista)