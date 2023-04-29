import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs): # Añadimos los attributos de QWidget
        super().__init__(*args, **kwargs) # Añadimos los attributos de QWidget
        
        self.init_gui() # Función exclusiva para meter dentro las configuraciones de las ventanas


    def init_gui(self):
        # Configuramos Ventana con su geometría y nombre:
                      #Ubi_X Ubi_y Tam_x Tam_y
        self.setGeometry(700, 200, 500, 800)
        self.setWindowTitle('Inicio sesión MyToTo')
        self.setStyleSheet("background-color: grey") # Cambiamos de color el fondo de la ventana
        
        # Configuramos Labels de usuario:
        self.label_usuario = QLabel("Usuario:", self) # Un Label permite mostrar cosas (texto, imágenes)
        self.usuario = QLineEdit("", self) # QLineEdit genera sectores para poder introducir texto
        self.usuario.setStyleSheet("background-color: white")

        # Configuramos Labels de correo:
        self.label_correo = QLabel("Correo:", self)
        self.correo = QLineEdit("", self)
        self.correo.setStyleSheet("background-color: white") # Los labels y los LineEdit pueden cambiar su color de fondo

        # Configuramos Labels de contraseña:
        self.label_contrasena = QLabel("Contraseña:", self)
        self.contrasena = QLineEdit("", self)
        self.contrasena.setStyleSheet("background-color: white")

        # Configuramos botón:
        self.boton_ingresar = QPushButton("Ingresar", self) # Genera botones apretables >:3
        self.boton_ingresar.setStyleSheet("background-color: skyblue")
        
        # Configuramos imágen:
        self.imagen = QLabel(self) # Creamos un Label donde añadir luego la imágen que queremos mostrar
        self.imagen.setGeometry(25, 25, 100, 100)

        ruta_imagen = os.path.join("imgs", "Twitter_logo_blue.png") # Ruta de la imágen
        pixeles = QPixmap(ruta_imagen) # Instanciamos la imágen que obtuvimos con el path
        self.imagen.setPixmap(pixeles)
        self.imagen.setScaledContents(True) # Hacemos que la resolución de la imágen se adapte a nuestras dimensiones

        #hbox_0 = QHBoxLayout()
        #hbox_0.addWidget(self.imagen)
        #hbox_0.addStretch(10)

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.label_usuario)
        hbox_1.addWidget(self.usuario)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(self.label_correo)
        hbox_2.addWidget(self.correo)

        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.label_contrasena)
        hbox_3.addWidget(self.contrasena)
        
        vbox = QVBoxLayout()
        #vbox.addLayout(hbox_0)
        vbox.addLayout(hbox_1) # Con la función Layout podemos añadir contenedores dentro de contenedores
        vbox.addLayout(hbox_2) # Con la función Layout podemos añadir contenedores dentro de contenedores
        vbox.addLayout(hbox_3) # Con la función Layout podemos añadir contenedores dentro de contenedores
        vbox.addWidget(self.boton_ingresar) # Con la función Widget podemos añadir elementos creados 
        self.setLayout(vbox) # Instancia los contenedores 

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())