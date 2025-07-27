from PyQt6.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QHBoxLayout,QMessageBox)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle('Layout Horizontal Example')

        self.generar_form()
        self.show()

    def generar_form(self):
        correo_label = QLabel('Correo:')
        self.correo_input = QLineEdit()
        self.correo_input.setPlaceholderText('Ingrese su correo electrónico')
        enviar_button = QPushButton('Enviar')
        enviar_button.clicked.connect(self.enviar_correo)

        layout = QHBoxLayout()
        layout.addWidget(correo_label)
        layout.addWidget(self.correo_input)
        layout.addWidget(enviar_button)
    
        self.setLayout(layout)

    def enviar_correo(self):
        QMessageBox.information(
            self,
            "Información",
            f"Correo enviado correctamente! {self.correo_input.text()}",
            QMessageBox.StandardButton.Ok,
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
