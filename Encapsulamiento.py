class AlumnoIIC2233():
    def __init__(self, nombre, usuario_github, clave_github):
        self.nombre = nombre
        self.usuario_github = usuario_github
        self.__clave_github = clave_github
        
    def ingresar_a_github(self):
        usuario = input("Ingrese usuario: ")
        clave = input("Ingrese clave: ")
        if clave == self.__clave_github and usuario == self.usuario_github:
            print("Ingresaste correctamente a github!")
        else:
            print("Algún input no es correcto:(")
            
    def __ingresar_canal_secreto(self):
        print("Procastino viendo anime sin que nadie sepa")
    
alumno_1 = AlumnoIIC2233("joaquin", "joca122", "rata123")

#print(f"No debería poder leer que la clave es {alumno_1.__clave_github}") # No puedo verlo
print(f"No debería poder leer que la clave es {alumno_1._AlumnoIIC2233__clave_github}") # Puedo verlo

#alumno_1.__ingresar_canal_secreto() # No puedo verlo
alumno_1._AlumnoIIC2233__ingresar_canal_secreto() # Puedo verlo