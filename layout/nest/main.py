import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QWidget, QPushButton,QLabel,QLineEdit, QHBoxLayout)

# Layout anidado con QVBoxLayout y QHBoxLayout
# Este ejemplo muestra cómo crear un formulario simple con campos de entrada y un botón de envío.
# El formulario está organizado en un diseño vertical que contiene varios diseños horizontales para agrupar los campos de entrada.
# El uso de QVBoxLayout y QHBoxLayout permite una disposición clara y ordenada de los elementos en la interfaz gráfica. 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Layout nested example')
        self.generar_form()
        self.show()

    def generar_form(self):
        mensaje_principal = QLabel('Porfavor ingrese sus datos: ')
        nombre_label = QLabel('Nombre:')
        nombre_label.setFixedWidth(60)
        self.nombre_input = QLineEdit()
        apellido_label = QLabel('Apellido:')
        apellido_label.setFixedWidth(60)
        self.apellido_input = QLineEdit()
        edad_label = QLabel('Edad:')
        edad_label.setFixedWidth(60)
        self.edad_input = QLineEdit()
        correo_label = QLabel('Correo:')
        correo_label.setFixedWidth(60)
        self.correo_input = QLineEdit()
        direccion_label = QLabel('Dirección:')
        direccion_label.setFixedWidth(60)
        self.direccion_input = QLineEdit()
        telefono_label = QLabel('Teléfono:')
        telefono_label.setFixedWidth(60)
        self.telefono_input = QLineEdit()
        enviar_button = QPushButton('Enviar')

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(mensaje_principal)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()

        horizontal_layout1.addWidget(nombre_label)
        horizontal_layout1.addWidget(self.nombre_input)
        horizontal_layout1.addWidget(correo_label)
        horizontal_layout1.addWidget(self.correo_input)

        horizontal_layout2.addWidget(apellido_label)
        horizontal_layout2.addWidget(self.apellido_input)
        horizontal_layout2.addWidget(direccion_label)
        horizontal_layout2.addWidget(self.direccion_input)

        horizontal_layout3.addWidget(edad_label)
        horizontal_layout3.addWidget(self.edad_input)
        horizontal_layout3.addWidget(telefono_label)
        horizontal_layout3.addWidget(self.telefono_input)

        vertical_layout.addLayout(horizontal_layout1)
        vertical_layout.addLayout(horizontal_layout2)
        vertical_layout.addLayout(horizontal_layout3)
        vertical_layout.addWidget(enviar_button)

        self.setLayout(vertical_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())

















