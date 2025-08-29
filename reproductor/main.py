import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QLabel, QPushButton
                             ,QDockWidget,QStatusBar,QTabWidget,QWidget
                             ,QHBoxLayout,QVBoxLayout,QListWidget)
from PyQt6.QtGui import QPixmap

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

