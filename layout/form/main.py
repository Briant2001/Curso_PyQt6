import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,QDateEdit, 
                             QLineEdit, QPushButton,QComboBox, QFormLayout, 
                             QHBoxLayout, QMessageBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QDate,Qt

class MainForm(QWidget):
    def __init__(self):
        super().__init__()

        
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Form Layout Example")
        self.creaer_formulario()
        self.show()

    
    def creaer_formulario(self):
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

        self.setLayout(main_form)


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
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainForm()
    sys.exit(app.exec())























        














        



         





