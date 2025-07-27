from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

class SimpleWidgetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con QWidget")
        self.setGeometry(200, 200, 300, 150) # x, y, ancho, alto

        layout = QVBoxLayout()
        layout.addWidget(QLabel("¡Soy una ventana básica con QWidget!"))
        layout.addWidget(QPushButton("Haz clic"))
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWidgetWindow()
    window.show()
    sys.exit(app.exec())