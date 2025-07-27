from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QAction # Necesario para acciones de menú
import sys

class MainWindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación con QMainWindow")
        self.setGeometry(100, 100, 600, 400)

        # --- Área Central (donde va el contenido principal) ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(QLabel("Contenido principal de la aplicación."))
        layout.addWidget(QPushButton("Un botón en el área central"))

        # --- Barra de Menú ---
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Archivo")

        # Acciones de menú
        exit_action = QAction("Salir", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close) # Conecta a la función de cerrar la ventana
        file_menu.addAction(exit_action)

        about_action = QAction("Acerca de...", self)
        about_action.triggered.connect(self.show_about_dialog)
        menu_bar.addMenu("Ayuda").addAction(about_action)

        # --- Barra de Herramientas ---
        toolbar = self.addToolBar("Herramientas")
        toolbar.addAction(exit_action) # Puedes reutilizar acciones

        # --- Barra de Estado ---
        self.statusBar().showMessage("Listo para operar.")


    def show_about_dialog(self):
        QMessageBox.information(self, "Acerca de", "Esta es una aplicación de ejemplo con QMainWindow.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    sys.exit(app.exec())