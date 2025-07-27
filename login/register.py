from PyQt6.QtWidgets import (QDialog,QLabel,QPushButton,
                             QLineEdit,QMessageBox)
from PyQt6.QtGui import QFont,QFontDatabase

import os

class RegistrarUsuario(QDialog) :
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()
        

    def generar_formulario(self):
        # print(QFontDatabase.families())
        self.setWindowTitle("Registrar Usuario")
        self.setGeometry(150, 130, 300, 200)

        self.user_label = QLabel("Nombre de Usuario:", self)
        self.user_label.setFont(QFont("Candara", 10))
        self.user_label.setStyleSheet("color:#1E90FF")
        self.user_label.move(20, 54)

        self.user_input = QLineEdit(self)
        self.user_input.setFont(QFont("Candara", 10))
        self.user_input.resize(120, 20)
        self.user_input.move(150, 50)

        self.pass_label = QLabel("Contraseña:", self)
        self.pass_label.setFont(QFont("Candara", 10))
        self.pass_label.setStyleSheet("color:#1E90FF")
        self.pass_label.move(20, 86)

        self.pass_input = QLineEdit(self)
        self.pass_input.setFont(QFont("Candara", 10))
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_input.resize(120, 20)
        self.pass_input.move(150, 84)

        self.pass_label_confirm = QLabel("Confirmar Contraseña:", self)
        self.pass_label_confirm.setFont(QFont("Candara", 10))
        self.pass_label_confirm.setStyleSheet("color:#1E90FF")
        self.pass_label_confirm.move(20, 118)

        self.pass_input_confirm = QLineEdit(self)
        self.pass_input_confirm.setFont(QFont("Candara", 10))
        self.pass_input_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_input_confirm.resize(120, 20)
        self.pass_input_confirm.move(150, 114)

        self.register_button = QPushButton("Registrar", self)
        self.register_button.setFont(QFont("Candara", 10))
        self.register_button.resize(100, 30)
        self.register_button.move(50, 150)
        self.register_button.clicked.connect(self.register)
        # self.show()

        self.cancel_button = QPushButton("Cancelar", self)
        self.cancel_button.setFont(QFont("Candara", 10))
        self.cancel_button.resize(100, 30)
        self.cancel_button.move(150, 150)
        self.cancel_button.clicked.connect(self.closer)


    def register(self):
        usuer_path = os.path.join(os.path.dirname(__file__), "usuarios.txt")

        usuario  = self.user_input.text()
        password = self.pass_input.text()
        password_confirm = self.pass_input_confirm.text()
        
        if not usuario or not password or not password_confirm:
            QMessageBox.warning(self, 
                                "Error", 
                                "Todos los campos son obligatorios.",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif password != password_confirm:
            QMessageBox.warning(self, 
                                "Error", 
                                "Las contraseñas no coinciden.",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(usuer_path,"a+") as file:
                    file.write(f"{usuario},{password}\n")
                    print(f"Usuario {usuario} registrado correctamente.")
                QMessageBox.information(self, 
                                      "Registro Exitoso", 
                                      "Usuario registrado correctamente.",
                                      QMessageBox.StandardButton.Ok,
                                      QMessageBox.StandardButton.Ok)
                self.close()  # Cierra el diálogo después de registrar
            except FileNotFoundError as e:
                QMessageBox.critical(self, 
                                     "Error", 
                                     f"No se pudo registrar el usuario: {e}",
                                     QMessageBox.StandardButton.Close,
                                     QMessageBox.StandardButton.Close)


    def closer(self):
        self.close()  # Close the dialog without any action
        