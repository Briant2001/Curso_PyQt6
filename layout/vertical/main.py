import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Para eliminar el tamaño mínimo y fijo
        self.setMinimumHeight(200)
        # Para establecer un ancho fijo
        self.setFixedWidth(200)
        # Establecer el título de la ventana
        self.setWindowTitle('Layout Vertical Example')

        self.generar_formulario()
        self.show() 

    def generar_formulario(self):
        boton_uno = QPushButton('Botón 1')
        boton_dos = QPushButton('Botón 2')
        boton_tres = QPushButton('Botón 3')
        bonton_cuatro = QPushButton('Botón 4')
        boton_uno.clicked.connect(self.imprimir_boton_uno)
        boton_dos.clicked.connect(self.imprimir_boton_uno)
        boton_tres.clicked.connect(self.imprimir_boton_uno)     
        bonton_cuatro.clicked.connect(self.imprimir_boton_uno)


        layout = QVBoxLayout()
        layout.addWidget(boton_uno)
        layout.addWidget(boton_dos)
        layout.addWidget(boton_tres)
        layout.addWidget(bonton_cuatro)
        self.setLayout(layout)


    def imprimir_boton_uno(self):
        boton = self.sender()
        QMessageBox.information(
            self,
            "Información",
            f"Has presionado: {boton.text()}",
            QMessageBox.StandardButton.Ok,
        )










if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())