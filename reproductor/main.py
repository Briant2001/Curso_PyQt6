import sys
from PyQt6.QtWidgets import (QApplication,QMainWindow,QLabel, QPushButton
                             ,QDockWidget,QStatusBar,QTabWidget,QWidget
                             ,QHBoxLayout,QVBoxLayout,QListWidget)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)



    def iniUI(self):
        self.setWindowTitle("Reproductor de musica")
        self.setGeometry(100,100,600,500)
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

    # def generate_productor_tab(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

