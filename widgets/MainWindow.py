
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QAction, QLabel, QFileDialog

from constants import *
from widgets.Color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Typing Trainer")
        self.setFixedSize(WIDTH, HEIGHT)

        self.set_widgets()
        self.set_layout()
        self.set_actions()
        self.set_menu()

    def set_widgets(self):
        self.dynamic_string = QLabel(self)
        self.dynamic_string.setFixedWidth(WIDTH)
        self.dynamic_string.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(36)

        self.dynamic_string.setFont(font)
        self.dynamic_string.setStyleSheet(f"background-color: {SECOND_BACKGROUND_COLOR}")
        self.dynamic_string.setText("Open your file")

    def set_layout(self):
        main_layout = QVBoxLayout()
        upper_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        lower_layout = QHBoxLayout()

        main_layout.setContentsMargins(0, 0, 0, 0)

        upper_layout.addWidget(Color(BACKGROUND_COLOR))
        upper_layout.addWidget(Color(BACKGROUND_COLOR))
        upper_layout.addWidget(Color(BACKGROUND_COLOR))

        middle_layout.addWidget(self.dynamic_string)

        lower_layout.addWidget(Color(BACKGROUND_COLOR))
        lower_layout.addWidget(Color(BACKGROUND_COLOR))

        main_layout.addLayout(upper_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(lower_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def set_actions(self):
        self.openAction = QAction("&Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open_call)

        self.exitAction = QAction("&Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(self.exit_call)

    def set_menu(self):
        menu = self.menuBar()

        file = menu.addMenu("&File")
        file.addAction(self.openAction)
        file.addAction(self.exitAction)

    def open_call(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')

    def exit_call(self):
        exit(0)

    def keyPressEvent(self, event):
        key = event.key()

        if 65 < key < 90:
            print(chr(key))
