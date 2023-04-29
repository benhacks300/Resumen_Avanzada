import sys
import os
from PyQt5 import QtGui
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(750, 300, 300, 300)
        self.setWindowTitle("Sigue al cuadrado")
        self.setStyleSheet("background-color: gray")
        self.setFixedSize(500, 500)
        # Definimos el Rectángulo QRect
        self.label_cuadrado = QLabel("", self)
        self.x_axys = random.randint(0, 450) # Debemos restar el área del cuadrado para que este no se salga de la ventana
        self.y_axys = random.randint(0, 450) # Debemos restar el área del cuadrado para que este no se salga de la ventana
        self.label_cuadrado.setGeometry(QRect(self.x_axys, self.y_axys, 50, 50))
        ruta_imagen_cuadrado = os.path.join("imgs", "verde.png")
        self.pixmap_verde = QPixmap(ruta_imagen_cuadrado) 
        self.label_cuadrado.setPixmap(self.pixmap_verde)
        self.label_cuadrado.setScaledContents(True)

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if (self.x_axys <= x and x <= self.x_axys + 50) and (self.y_axys <= y and y <= self.y_axys + 50):
            self.x_axys = random.randint(0, 450)
            self.y_axys = random.randint(0, 450)
            self.label_cuadrado.move(self.x_axys, self.y_axys)

if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec())
