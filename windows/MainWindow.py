from PyQt5.QtWidgets import QWidget
from constants import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Typing Trainer")
        self.setFixedSize(WIDTH, HEIGHT)
