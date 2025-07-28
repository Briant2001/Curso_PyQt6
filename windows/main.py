import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStatusBar)
from PyQt6.QtGui import QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setStyleSheet("QStatusBar { background-color: lightgray; }")
        self.statusBar.showMessage("Ocurrió un error en la comunicacion", 5000)  # Mensaje por 5 segundos
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Main Window with Status Bar')
        self.generate_window()
        self.show()

    def generate_window(self):
        self.create_action()
        self.crete_menu()

    def create_action(self):
        self.open_action = QAction('Abrir', self)
        self.open_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_action.setStatusTip('Abrir un archivo')
        self.open_action.triggered.connect(self.open)

        #Guardar
        self.save_action = QAction('Guardar', self)
        self.save_action.setShortcut(QKeySequence("Ctrl+S"))
        self.save_action.setStatusTip('Guardar un archivo')
        self.save_action.triggered.connect(self.save)

        # eXPORTAR
        self.export_action = QAction('Exportar', self)
        self.export_action.setShortcut(QKeySequence("Ctrl+E"))
        self.export_action.setStatusTip('Exportar un archivo')
        self.export_action.triggered.connect(self.export)

        #Deshacer
        self.undo_action = QAction('Deshacer', self)
        self.undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_action.setStatusTip('Deshacer la última acción')
        self.undo_action.triggered.connect(self.undo)

        #Rehacer
        self.redo_action = QAction('Rehacer', self)
        self.redo_action.setShortcut(QKeySequence("Ctrl+Y"))
        self.redo_action.setStatusTip('Rehacer la última acción')
        self.redo_action.triggered.connect(self.redo)

    def crete_menu(self):
        menu_archivo = self.menuBar().addMenu('Archivo')
        menu_archivo.addAction(self.open_action)
        menu_archivo.addAction(self.save_action)
        menu_archivo.addAction(self.export_action)

        menu_archivo = self.menuBar().addMenu('Editar')
        menu_archivo.addAction(self.undo_action)
        menu_archivo.addAction(self.redo_action)

    def open(self):
        print("Abrir archivo")
    def save(self):
        print("Guardar archivo")
    def export(self):
        print("Exportar archivo")
    def undo(self):
        print("Deshacer última acción")
    def redo(self):
        print("Rehacer última acción")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())

        