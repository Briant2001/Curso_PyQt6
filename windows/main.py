import sys
from PyQt6.QtWidgets import (QApplication,QWidget, QMainWindow, QStatusBar, QFileDialog,
                             QVBoxLayout,QTextEdit,QFontDialog,QColorDialog,QToolBar)
from PyQt6.QtGui import QAction, QKeySequence, QTextCharFormat, QPixmap
from PyQt6.QtCore import QStandardPaths

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.s("QStatusBar { background-color: lightgray; }")
        self.statusBar.showMessage("Ocurrió un error en la comunicacion", 5000)  # Mensaje por 5 segundos
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Main Window with Status Bar')
        self.generate_window()
        self.show()

    def generate_window(self):
        self.crete_content()
        self.create_action()
        self.crete_menu()
        self.create_toolbar()


    def create_toolbar(self):
        self.toolbar = QToolBar("Barra de herramientas")
        self.addToolBar(self.toolbar)


    def crete_content(self):
        layout = QVBoxLayout()
        self.editor = QTextEdit()
        layout.addWidget(self.editor)
        layout.setContentsMargins(30,30,30,30)  

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def crete_menu(self):
        menu_archivo = self.menuBar().addMenu('Archivo')
        menu_archivo.addAction(self.open_action)
        menu_archivo.addAction(self.save_action)
        menu_archivo.addAction(self.export_action)

        menu_archivo = self.menuBar().addMenu('Editar')
        menu_archivo.addAction(self.font_action)
        menu_archivo.addAction(self.undo_action)
        menu_archivo.addAction(self.redo_action)
        menu_archivo.addAction(self.color_action)

        menu_ver  = self.menuBar().addMenu("Ver")
        submenu_personal = menu_ver.addMenu("Personalización")
        submenu_personal.addAction(self.view_open_action)
        submenu_personal.addAction(self.view_save_action)
        submenu_personal.addAction(self.view_export_action)

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

        # Exportar
        self.export_action = QAction('Exportar', self)
        self.export_action.setShortcut(QKeySequence("Ctrl+E"))
        self.export_action.setStatusTip('Exportar un archivo')
        self.export_action.triggered.connect(self.export)

        #font_action
        self.font_action = QAction('Fuente', self)
        self.font_action.setShortcut(QKeySequence("Ctrl+F"))
        self.font_action.setStatusTip('Cambio de fuente')
        self.font_action.triggered.connect(self.set_font)

        #color_action
        self.color_action = QAction('Color ', self)
        self.color_action.setShortcut(QKeySequence("Ctrl+K"))
        self.color_action.setStatusTip('Cambio de color')
        self.color_action.triggered.connect(self.set_color)

        #Deshacer
        self.undo_action = QAction('Deshacer', self)
        self.undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        self.undo_action.setStatusTip('Deshacer la última acción')
        self.undo_action.triggered.connect(self.editor.undo)

        #Rehacer
        self.redo_action = QAction('Rehacer', self)
        self.redo_action.setShortcut(QKeySequence("Ctrl+Y"))
        self.redo_action.setStatusTip('Rehacer la última acción')
        self.redo_action.triggered.connect(self.editor.redo)


        #Ver/Ocultar barra de herramientas
        self.view_open_action = QAction('Abrir', self,checkable=True)
        self.view_open_action.setStatusTip('Agregar boton en la barra de tareas para abrir archivo')
        self.view_open_action.triggered.connect(self.view_open)

        #Guardar
        self.view_save_action = QAction('Guardar', self,checkable=True)
        self.view_save_action.setStatusTip('Agregar boton en la barra de tareas para abrir archivo')
        self.view_save_action.triggered.connect(self.view_save)

        # Exportar
        self.view_export_action = QAction('Exportar', self,checkable=True)
        self.view_export_action.setStatusTip('Agregar boton en la barra de tareas para abrir archivo')
        self.view_export_action.triggered.connect(self.view_export)

    def open(self):
        print("Abrir archivo")
        options = (QFileDialog.Option.DontUseNativeDialog)
        initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation
        )
        file_type = "Text Files(*.txt);;Images(*.png);;All Files(*)"
        self.file, _ = QFileDialog(self,"Abrir archivo",initial_dir, file_type, options=options).getOpenFileName()

        #Mostrar texto
        with open(self.file,"r") as f:
            self.editor.setText(f.read())

    def save(self):
        options = (QFileDialog.Option.DontUseNativeDialog)
        initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation
        )
        file_name, _ = QFileDialog.getSaveFileName(self,"Guardar archivo",initial_dir,"Archivo de texto (*.txt);; HTML (*.html);; ")

        if file_name.endswith(".txt"):
            text = self.editor.toPlainText()
            with open(file_name,"w") as f:
                f.write(text)
        elif file_name.endswith(".html"):
            text = self.editor.toHtml()
            with open(file_name,"w") as f:
                f.write(text)

    def export(self):
         initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.DocumentsLocation
        )
         screen = QApplication.primaryScreen()
         pixmap = screen.grabWindow(self.editor.winId())
         
         file_name, _ = QFileDialog.getSaveFileName(self,"Guardar archivo",initial_dir,"Imagen (*.png);; Imagen (*.jpg);; ")

         if file_name:
             pixmap.save(file_name)


    def view_open(self):
        if self.view_open_action.isChecked():
            self.toolbar.addAction(self.open_action)
        else:
            self.toolbar.removeAction(self.open_action)

    def view_save(self):
        if self.view_save_action.isChecked():
            self.toolbar.addAction(self.save_action)
        else:
            self.toolbar.removeAction(self.save_action)

    def view_export(self):
        if self.view_export_action.isChecked():
            self.toolbar.addAction(self.export_action)
        else:
            self.toolbar.removeAction(self.export_action)

    def set_font(self):
        selecte_text_cursosr = self.editor.textCursor()

        font, ok = QFontDialog.getFont(
            self.editor.currentFont(), self
        )

        if ok: 
            if selecte_text_cursosr.hasSelection():
                format = self.editor.currentCharFormat()
                format.setFont(font)
                selecte_text_cursosr.mergeCharFormat(format)
            else :
                self.editor.setCurrentFont(font)

    def set_color(self):
        selected_text_cursor = self.editor.textCursor()
        color = QColorDialog.getColor(self.editor.textColor(), self)

        if color.isValid():
            if selected_text_cursor.hasSelection():
                format = QTextCharFormat()
                format.setForeground(color)
                selected_text_cursor.mergeCharFormat(format)
            else:
                self.editor.setTextColor(color)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())

        