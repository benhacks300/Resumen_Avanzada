import sys
import os
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QRadioButton, QSpinBox, QCheckBox)

from PyQt5.QtGui import QFont

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_gui()

    def init_gui(self):
        self.setGeometry(750, 150, 500, 600)
        self.setWindowTitle("Registro a MyToTo")
        self.setStyleSheet("background-color: gray")
        self.setFixedSize(500, 600)

        self.label_usuario = QLabel("Usuario:", self)
        self.usuario = QLineEdit("", self)
        self.usuario.setStyleSheet("background-color: white")

        self.label_genero = QLabel("Género:", self)
        self.label_genero.setFont(QFont("Sanserif", 10))
        self.genero_1 = QRadioButton("Femenino")
        self.genero_2 = QRadioButton("Masculino")
        self.genero_3 = QRadioButton("No binario")
        self.genero_4 = QRadioButton("No mencionar")

        self.label_edad = QLabel("Edad:", self)
        self.edad = QSpinBox()
        self.edad.setMinimum(18)
        self.edad.setStyleSheet("background-color: white")

        self.label_configuracion = QLabel("Configuración:", self)
        self.configuracion_1 = QCheckBox("Cuenta Privada")
        self.configuracion_2 = QCheckBox("Recibir Noticias")
        self.configuracion_3 = QCheckBox("Acepto Términos y condiciones")

        self.boton = QPushButton("Continuar", self)
        self.boton.setStyleSheet("background-color: white")

        hbox_usuario = QHBoxLayout()
        hbox_usuario.addStretch(1)
        hbox_usuario.addWidget(self.label_usuario)
        hbox_usuario.addWidget(self.usuario)
        hbox_usuario.addStretch(1)
        
        hbox_genero = QHBoxLayout()
        hbox_genero.addStretch(6)
        hbox_genero.addWidget(self.label_genero)
        hbox_genero.addStretch(1)
        vbox_genero = QVBoxLayout()
        vbox_genero.addWidget(self.genero_1)
        vbox_genero.addWidget(self.genero_2)
        vbox_genero.addWidget(self.genero_3)
        vbox_genero.addWidget(self.genero_4)
        hbox_genero.addLayout(vbox_genero)
        hbox_genero.addStretch(6)

        hbox_edad = QHBoxLayout()
        hbox_edad.addStretch(1)
        hbox_edad.addWidget(self.label_edad)
        hbox_edad.addWidget(self.edad)
        hbox_edad.addStretch(1)

        hbox_configuracion = QHBoxLayout()
        hbox_configuracion.addStretch(6)
        hbox_configuracion.addWidget(self.label_configuracion)
        hbox_configuracion.addStretch(1)
        vbox_configuracion = QVBoxLayout()
        vbox_configuracion.addWidget(self.configuracion_1)
        vbox_configuracion.addWidget(self.configuracion_2)
        vbox_configuracion.addWidget(self.configuracion_3)
        hbox_configuracion.addLayout(vbox_configuracion)
        hbox_configuracion.addStretch(6)

        hbox_boton = QHBoxLayout()
        hbox_boton.addWidget(self.boton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_usuario)
        vbox.addLayout(hbox_genero)
        vbox.addLayout(hbox_edad)
        vbox.addLayout(hbox_configuracion)
        vbox.addLayout(hbox_boton)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
