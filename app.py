import sys
from main import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mineral Processing Toolkit")

        self.setFixedSize(QSize(int(1920/1.8), int(1080/1.5)))

        button = QPushButton(str(sphericity(int(4),int(3))))
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
