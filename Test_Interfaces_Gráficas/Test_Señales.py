import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(800, 400, 400, 150)
        self.setWindowTitle("Cuenta Clics")
        self.setStyleSheet("background-color: gray")
        self.setFixedSize(400, 150)
        
        self.contador = 0
        self.label_contador = QLabel(f"{self.contador} Clics", self)
        self.label_contador.setFont(QFont("Arial", 20))
        self.boton = QPushButton("Clic", self)
        self.boton.clicked.connect(self.aumentar_contador)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label_contador)
        hbox.addStretch(8)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.boton)
        self.setLayout(vbox)

    def aumentar_contador(self):
        self.contador += 1
        self.label_contador.setText(f"{self.contador} Clics")

if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec())