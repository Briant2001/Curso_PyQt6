import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton,QMessageBox, QCheckBox
from PyQt6.QtGui import QFont,QPixmap
from register import RegistrarUsuario   
import os
from main import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        ##Define the UI elements
        self.initUI()


    def initUI(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Mi login")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_logged_in = False

        # Creamos el label del usuario
        self.user_label = QLabel("Usuario:", self)
        self.user_label.setFont(QFont("Arial", 12))
        self.user_label.move(20, 54)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(110,50)

        self.pass_label = QLabel("Contraseña:", self)
        self.pass_label.setFont(QFont("Arial", 12))
        self.pass_label.move(20, 86)
        
        self.pass_input = QLineEdit(self)
        self.pass_input.resize(250,24)
        self.pass_input.move(110,84)
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.check_view_password = QCheckBox("Ver contraseña", self)
        self.check_view_password.move(110, 120)
        self.check_view_password.toggled.connect(self.toggle_password_visibility)

        loggin_button = QPushButton("Iniciar sesión", self)
        loggin_button.resize(100, 30)
        loggin_button.move(110, 150) 
        loggin_button.clicked.connect(self.login)

        register_button = QPushButton("Registrar", self)
        register_button.resize(100, 30)
        register_button.move(220, 150) 
        register_button.clicked.connect(self.register)


    def toggle_password_visibility(self, state):
        if state:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

    def login(self):
        user = []
        usuer_path = os.path.join(os.path.dirname(__file__), "usuarios.txt")
        try:
            with open(usuer_path, "r") as file:
                for line in file:
                    #strinp para quitar espacios y saltos de línea
                    user.append(line.strip("\n"))
            
            login_information = f"{self.user_input.text()},{self.pass_input.text()}"

            if login_information in user:
                QMessageBox.information(self, "Login", 
                                        "Inicio de sesión exitoso.",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.is_logged_in = True
                self.close()
                self.open_home()
            else:
                QMessageBox.warning(self, "Login", 
                                    "Usuario o contraseña incorrectos.",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.critical(self, f"Error", "Archivo de usuarios no encontrado: {e}")
        except Exception as e:
            QMessageBox.critical(self, f"Error", "Error en el inicio de sesión:s " + str(e))
            QApplication.quit()  # O sys.exit(1)
        # finally:
        #     self.close()

    def register(self):
        self.new_usert_form = RegistrarUsuario()
        self.new_usert_form.show()

    def open_home(self):
        self.home_window = MainWindow()
        self.home_window.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())    
        
