import sys
import random 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon
import os


RootFolder = os.path.dirname(os.path.abspath(__file__))

class MainWin(QMainWindow):
    def __init__(self, *args):
        super(MainWin, self).__init__(*args)
        self.setWindowTitle("Here: {}".format(RootFolder))
        self.setWindowIcon(QIcon("gui/Eulitha_icon.ico"))
        self.setFixedWidth(500)
        self.button = QPushButton("Press Me!")
        self.button.setToolTip("This is a <b>QPushButton</b> widget")
        self.button.setStyleSheet("background-color: red")
        self.button.clicked.connect(self.on_click)
        self.setCentralWidget(self.button)

    def on_click(self):
        r,g,b = random.randbytes(3)
        color_style = "background-color: rgb({}, {}, {});".format(r,g,b)
        self.button.setStyleSheet(color_style)


def main():
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())