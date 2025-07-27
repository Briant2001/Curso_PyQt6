import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit,QTextEdit,QPushButton,
                             QStackedLayout,QFormLayout,QVBoxLayout, 
                             QHBoxLayout,
                             QComboBox,QDateEdit,QMessageBox)

from PyQt6.QtCore import Qt,QDate
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()


    def initUI(self):
        self.setWindowTitle("QStaked Layout Example")
        self.setGeometry(100, 100, 800, 600)
        self.generar_window()

    def generar_window(self):
        boton_1 = QPushButton("Ventana 1")
        boton_1.clicked.connect(self.change_window)
        boton_2 = QPushButton("Ventana 2")
        boton_2.clicked.connect(self.change_window)
        boton_3 = QPushButton("Ventana 3")
        boton_3.clicked.connect(self.change_window)

        button_group = QHBoxLayout()
        button_group.addWidget(boton_1)
        button_group.addWidget(boton_2)
        button_group.addWidget(boton_3)

        #Pagina 1
        tittle_label = QLabel("Mapa")
        tittle_label.setFont(QFont("Arial", 18,))
        tittle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Establecer el alto y ancho del label
        tittle_label.setMinimumHeight(20)


        image_label = QLabel()
        pixmap = QPixmap("C:\\Users\\bmaldona\Cursos\\python\\pyqt6\\layout\\QStakedLayout\\images\\images.png")
        pixmap = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setPixmap(pixmap)
        #Obtener el tamaño de la ventana
        window_size = self.size()
        #Ajustar la imagen al tamaño de la ventana
        image_label.setMaximumSize(window_size)
        # image_label.setScaledContents(True)
        # Ajustar el alto y ancho del label

        page1_layout = QVBoxLayout()
        page1_layout.addWidget(tittle_label)
        page1_layout.addWidget(image_label)
        page1_layout.addStretch(2)  # Espacio abajo

        contenedor_1 = QWidget()
        contenedor_1.setLayout(page1_layout)

        #Pagina 2
        titulo = QLabel("Formulario de Registro")
        titulo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Ingrese su nombre")

        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Ingrese su apellido")

        self.genero_combo = QComboBox()
        self.genero_combo.addItems(["Masculino", "Femenino", "Otro"])

        self.fecha_nac_edit = QDateEdit()
        self.fecha_nac_edit.setDisplayFormat("dd/MM/yyyy")
        self.fecha_nac_edit.setMaximumDate(QDate.currentDate())
        self.fecha_nac_edit.setCalendarPopup(True)
        self.fecha_nac_edit.setDate(QDate.currentDate())

        self.telefono_edit= QLineEdit()
        self.telefono_edit.setPlaceholderText("Ingrese su teléfono")
        self.telefono_edit.setInputMask("9999-9999")

        submit_button = QPushButton("Enviar")
        submit_button.clicked.connect(self.enviar_formulario)

        layout_h_box = QHBoxLayout()
        layout_h_box.addWidget(self.nombre_edit)
        layout_h_box.addWidget(self.apellido_edit)


        main_form = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Nombre: ",layout_h_box)
        main_form.addRow("Genero: ",self.genero_combo)
        main_form.addRow("Fecha: ",self.fecha_nac_edit)
        main_form.addRow("Telefono: ",self.telefono_edit)
        main_form.addRow(submit_button)

        contenedor_2 = QWidget()
        contenedor_2.setLayout(main_form)


        #Pagina 3
        titulo_texto = QLabel("Ventana de Texto")
        titulo_texto.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        titulo_texto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.observations_edit = QTextEdit()
        self.observations_edit.setPlaceholderText("Ingrese sus observaciones aquí...")

        form_3 = QFormLayout()
        form_3.addRow(titulo_texto)
        form_3.addRow("Observaciones",self.observations_edit)

        contenedor_3 = QWidget()
        contenedor_3.setLayout(form_3)

        #Stacked Layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(contenedor_1)
        self.stacked_layout.addWidget(contenedor_2) 
        self.stacked_layout.addWidget(contenedor_3)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_group)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)

    def enviar_formulario(self):
        QMessageBox.information(
            self,
            "Información del sistema",
            f"Nombre: {self.nombre_edit.text()}\n"
            f"Genero: {self.genero_combo.currentText()}\n"
            f"Fecha:  {self.fecha_nac_edit.text()}\n"
            f"Telefono: {self.telefono_edit.text()}",
            QMessageBox.StandardButton.Ok
        )
        

    def change_window(self):
        sender = self.sender()
        if sender.text() == "Ventana 1":
            self.stacked_layout.setCurrentIndex(0)
        elif sender.text() == "Ventana 2":
            self.stacked_layout.setCurrentIndex(1)
        elif sender.text() == "Ventana 3":
            self.stacked_layout.setCurrentIndex(2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())