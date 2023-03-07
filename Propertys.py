class AlumnoIIC2233():
    def __init__(self, nombre, puntaje, usuario_github, clave_github):
        self.nombre = nombre
        self.max_pte = 100
        self.min_pte = 0
        self.__puntaje = puntaje
        self.usuario_github = usuario_github
        self.__clave_github = clave_github
    
    @property  #Getter (Para obtener el atributo)
    def puntaje(self): 
        return self.__puntaje
    
    @puntaje.setter     #Setter (Para establecer el valor del atributo) 
    # TODO SE RIGE DESDE EL NOMBRE QUE SE DEFINE LA PROPERTY INICIAL (GETTER)
    def puntaje(self, valor):
        if valor < 0:
            self.__puntaje = 0
        elif valor > 100:
            self.__puntaje = 100
        else:
            self.__puntaje = valor
    
    @puntaje.deleter    #Deleter (Para eliminar un atributo)
    def puntaje(self):
        print("Borrando puntaje...")
        del self.__puntaje
    
    def sube_meme(self):
        self.puntaje += 20
    
    def hace_tarea_dia_anterior(self):
        self.puntaje -= 10

    def ingresar_a_github(self):
        usuario = input("ingrese usuario: ")
        clave = input("ingrese clave: ")
        if clave == self._clave_github and usuario == self.usuario_github:
            print("Ingresaste correctamente a github!")
        else:
            print("Algún input no es correcto:(")
            
    def __ingresar_canal_secreto(self):
        print("veo anime sin que me digan que soy una rata")

alumno_1 = AlumnoIIC2233("joaquin", 20, "joca122", "rata123")

#Accedemos al puntaje (Getter)
print(alumno_1.puntaje)

#Probamos que el puntaje no baje de 0 (Setter)
for _ in range(10):
    alumno_1.hace_tarea_dia_anterior()
print(alumno_1.puntaje)

#Probamos que el puntaje no suba de 100 (Setter)
for _ in range(10):
    alumno_1.sube_meme()
print(alumno_1.puntaje)

#Eliminamos el puntaje (Deleter)
del alumno_1.puntaje
print(alumno_1.puntaje)
