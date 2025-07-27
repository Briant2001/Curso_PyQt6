from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap
import os
from PyQt6.QtCore import Qt  # Agrega esta línea

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Ventana Principal")

        self.generar_contenido()

    def generar_contenido(self):
        image_path= os.path.join(os.path.dirname(__file__), "python.png")

        try:
            with open(image_path):
                image_label = QLabel(self)
                # image_label.setPixmap(QPixmap(image_path))
                pixmap = QPixmap(image_path).scaled(
                    200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
                )
                image_label.setPixmap(pixmap)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", 
                                 "Imagen no encontrada: " + image_path,
                                 QMessageBox.StandardButton.Close,
                                 QMessageBox.StandardButton.Close)
