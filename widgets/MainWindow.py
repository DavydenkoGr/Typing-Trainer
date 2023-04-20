from constants import *
from widgets.Color import Color

from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Typing Trainer")
        self.setFixedSize(WIDTH, HEIGHT)

        self.set_layout()

        pass

    def set_layout(self):
        main_layout = QVBoxLayout()
        upper_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        lower_layout = QHBoxLayout()

        main_layout.setContentsMargins(0, 0, 0, 0)

        upper_layout.addWidget(Color(BACKGROUND_COLOR))
        upper_layout.addWidget(Color(BACKGROUND_COLOR))
        upper_layout.addWidget(Color(BACKGROUND_COLOR))

        middle_layout.addWidget(Color(BACKGROUND_COLOR))

        lower_layout.addWidget(Color(BACKGROUND_COLOR))
        lower_layout.addWidget(Color(BACKGROUND_COLOR))

        main_layout.addLayout(upper_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(lower_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
