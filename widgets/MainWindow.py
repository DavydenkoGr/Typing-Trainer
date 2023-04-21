from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QAction, QLabel, QFileDialog

from functions import check_text
from constants import *
from widgets.Color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.flags = {"ready": False, "timer": False}
        self.pointer = None
        self.text = None
        self.text_iterator = None
        self.current_char = None

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
        try:
            name = QFileDialog.getOpenFileName(self, 'Open File')[0]
            text = open(name, "r").read()

            if not check_text(text):
                raise Exception("Your text doesn't match")

            self.start_configure(text)

        except Exception as exception:
            self.statusBar().showMessage(str(exception))

    def exit_call(self):
        exit(0)

    def keyPressEvent(self, event):
        if not (self.flags["ready"]):
            return

        key = event.text()

        if not key:
            return

        if self.current_char != key:
            self.statusBar().showMessage(f"Current letter: {self.current_char}")
            return

        # Все проверки пройдены успешно, запускаем таймер, если не запущен
        if not self.flags["timer"]:
            self.flags["timer"] = True

        try:
            self.pointer += 1

            self.dynamic_string.setText(
                self.text[self.pointer:min(DYNAMIC_STRING_SIZE, len(self.text))]
            )

            self.current_char = next(self.text_iterator)

        except StopIteration:
            self.end_configure()

    def start_configure(self, text):
        self.pointer = 0
        self.text = text
        self.text_iterator = iter(text)
        self.current_char = next(self.text_iterator)
        self.flags["ready"] = True

        self.dynamic_string.setText(
            text[self.pointer:min(DYNAMIC_STRING_SIZE, len(text))]
        )

    def end_configure(self):
        self.pointer = None
        self.text = None
        self.text_iterator = None
        self.current_char = None
        self.flags["ready"] = False
        self.flags["timer"] = False

        self.dynamic_string.setText("Open your file")
