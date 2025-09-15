import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QLabel, QPushButton
                             ,QDockWidget,QStatusBar,QTabWidget,QWidget
                             ,QHBoxLayout,QVBoxLayout,QListWidget,QFileDialog,QListWidgetItem)
from PyQt6.QtGui import QPixmap, QAction, QKeySequence
from PyQt6.QtCore import Qt,QStandardPaths
import os

class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.iniUI()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def iniUI(self):
        self.setWindowTitle("Reproductor de musica")
        self.setGeometry(100,100,400,500)
        self.generate_main_window()
        self.create_dock()
        self.create_actions()
        self.create_menu()
        self.show()

    def generate_main_window(self):
        tab_bar = QTabWidget(self)
        self.reproductor_container = QWidget()
        self.settings_container = QWidget()

        tab_bar.addTab(self.reproductor_container,"Reproductor")
        tab_bar.addTab(self.settings_container,"Configuración")

        self.generate_productor_tab()
        # self.generate_settings_tab()

        tab_h_box = QHBoxLayout()
        tab_h_box.addWidget(tab_bar)

        main_container = QWidget()
        main_container.setLayout(tab_h_box)
        self.setCentralWidget(main_container)

    def generate_productor_tab(self):
        main_v_box = QVBoxLayout()
        buttons_h_box = QHBoxLayout()

        mage_path= os.path.join(os.path.dirname(__file__), "images/images.png")

        song_image = QLabel()
        pixmap = QPixmap(mage_path)
        song_image.setPixmap(pixmap)
        song_image.setScaledContents(True)

        button_repeat = QPushButton("Reapetir")
        button_before = QPushButton("Regresar")
        button_play = QPushButton("Iniciar")
        button_next = QPushButton("Siguiente")
        button_random = QPushButton("Aleatorio")


        buttons_h_box.addWidget(button_repeat)
        buttons_h_box.addWidget(button_before)
        buttons_h_box.addWidget(button_play)
        buttons_h_box.addWidget(button_next)
        buttons_h_box.addWidget(button_random)
        button_container = QWidget()
        button_container.setLayout(buttons_h_box)

        main_v_box.addWidget(song_image)
        main_v_box.addWidget(button_container)

        self.reproductor_container.setLayout(main_v_box)


    def create_actions(self):
        self.listar_musica_action = QAction("&Listar Musica",self,checkable=True)
        self.listar_musica_action.setShortcut(QKeySequence("Ctrl+L"))
        self.listar_musica_action.setStatusTip("Listar musica para reproducir")
        self.listar_musica_action.triggered.connect(self.list_musica)
        self.listar_musica_action.setChecked(True)

        self.open_folder_action = QAction("Abrir Carpeta ",self) 
        self.open_folder_action.setShortcut(QKeySequence("Ctrl+O"))
        self.open_folder_action.setStatusTip("Abre tu carpeta de musica")
        self.open_folder_action.triggered.connect(self.open_folder_musica)
        self.open_folder_action.setChecked(True)
       
    def create_menu(self): 
        self.menuBar()
        menu_open = self.menuBar().addMenu("File")
        menu_open.addAction(self.open_folder_action)

        menu_view = self.menuBar().addMenu("Ver")
        menu_view.addAction(self.listar_musica_action)
   
    def list_musica(self):
        if self.listar_musica_action.isChecked():
            self.dock.show()
        else:
            self.dock.hide()


    def open_folder_musica(self):
        initial_dir = QStandardPaths.writableLocation(
            QStandardPaths.StandardLocation.MusicLocation)
        selected_folder = QFileDialog.getExistingDirectory(None,"Selecciona una carptea",initial_dir)
        for archivo in os.listdir(selected_folder):
            ruta_archivo = os.path.join(selected_folder,archivo)
            if ruta_archivo.endswith(".mp3"):
                self.songs_list.addItem(archivo)

    def create_dock(self):
        self.songs_list = QListWidget()
        self.dock = QDockWidget("Lista de canciones",self)
        self.dock.setWindowTitle("Lista de canciones")
        self.dock.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea |  Qt.DockWidgetArea.BottomDockWidgetArea
        )
        self.dock.setWidget(self.songs_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea,self.dock)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
















