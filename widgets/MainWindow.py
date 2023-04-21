from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QAction, QLabel, QFileDialog, QPushButton

from functions import check_text
from constants import *
from widgets.ColoredWidget import ColoredWidget
from widgets.StatisticsWindow import StatisticsWindow


class MainWindow(QMainWindow):
    """main window of the application"""
    def __init__(self):
        """initialization"""
        super().__init__()

        self.flags = {"ready": False, "timer": False}
        self.timer_counter = 0
        self.mistakes_count = 0
        self.pointer = None
        self.current_text_name = None
        self.text = None
        self.text_iterator = None
        self.current_char = None

        self.initUI()

    def initUI(self):
        """PyQt element initialization"""
        self.setWindowTitle("Typing Trainer")
        self.setFixedSize(WIDTH, HEIGHT)

        self.set_widgets()
        self.set_actions()
        self.set_layout()
        self.set_menu()

        self.addAction(self.pauseAction)

    def set_widgets(self):
        """set widgets"""
        font = QFont()
        font.setPointSize(FONT_SIZE)

        # Dynamic string
        self.dynamic_string = QLabel(self)
        self.dynamic_string.setFixedWidth(WIDTH)
        self.dynamic_string.setAlignment(Qt.AlignCenter)

        self.dynamic_string.setFont(font)
        self.dynamic_string.setStyleSheet(f"background-color: {SECOND_BACKGROUND_COLOR}")
        self.dynamic_string.setText("Open your file")

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(100)

        self.stopwatch = QLabel(self)
        self.stopwatch.setFixedWidth(int(WIDTH / 4))
        self.stopwatch.setAlignment(Qt.AlignCenter)

        self.stopwatch.setFont(font)
        self.stopwatch.setStyleSheet(f"background-color: {BACKGROUND_COLOR}")
        self.stopwatch.setText(str(self.timer_counter / 10))

        # Statistic label
        self.statistic = QLabel(self)
        self.statistic.setFixedWidth(int(WIDTH / 3))
        self.statistic.setAlignment(Qt.AlignCenter)

        self.statistic.setFont(font)
        self.statistic.setStyleSheet(f"background-color: {BACKGROUND_COLOR}")
        self.statistic.setText("Statistic:\n")

        # Restart button
        self.restart_button_container = ColoredWidget(BACKGROUND_COLOR)

        self.restart = QPushButton(self.restart_button_container)
        self.restart.setFixedWidth(int(WIDTH / 4))
        self.restart.clicked.connect(self.restart_try)
        self.restart.setFocusPolicy(Qt.NoFocus)

        self.restart.setFont(font)
        self.restart.setStyleSheet(f"background-color: {BUTTONS_COLOR}")
        self.restart.setText("restart")

        # Pause button
        self.pause_button_container = ColoredWidget(BACKGROUND_COLOR)

        self.pause = QPushButton(self.pause_button_container)
        self.pause.setFixedWidth(int(WIDTH / 4))
        self.pause.clicked.connect(self.pause_try)
        self.pause.setFocusPolicy(Qt.NoFocus)

        self.pause.setFont(font)
        self.pause.setStyleSheet(f"background-color: {BUTTONS_COLOR}")
        self.pause.setText("pause")

        # Statistics button
        self.statistics_button_container = ColoredWidget(BACKGROUND_COLOR)

        self.statistics = QPushButton(self.statistics_button_container)
        self.statistics.setFixedWidth(int(WIDTH / 3))
        self.statistics.clicked.connect(self.show_statistics)
        self.statistics.setFocusPolicy(Qt.NoFocus)

        self.statistics.setFont(font)
        self.statistics.setStyleSheet(f"background-color: {BUTTONS_COLOR}")
        self.statistics.setText("watch statistics")

        # Statistics window
        self.SW = StatisticsWindow()

    def set_layout(self):
        """set window layout"""
        main_layout = QVBoxLayout()
        upper_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        lower_layout = QHBoxLayout()

        main_layout.setContentsMargins(0, 0, 0, 0)

        upper_layout.addWidget(self.statistics_button_container)
        upper_layout.addWidget(self.stopwatch)
        upper_layout.addWidget(self.statistic)
        self.statistics_button_container.layout.addWidget(self.statistics, alignment=Qt.AlignCenter)

        middle_layout.addWidget(self.dynamic_string)

        lower_layout.addWidget(self.restart_button_container)
        lower_layout.addWidget(self.pause_button_container)
        self.restart_button_container.layout.addWidget(self.restart, alignment=Qt.AlignCenter)
        self.pause_button_container.layout.addWidget(self.pause, alignment=Qt.AlignCenter)

        main_layout.addLayout(upper_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(lower_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def set_actions(self):
        """set actions"""
        self.openAction = QAction("&Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open_call)

        self.exitAction = QAction("&Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.triggered.connect(self.exit_call)

        self.pauseAction = QAction("&Pause", self)
        self.pauseAction.setShortcut("Escape")
        self.pauseAction.triggered.connect(self.pause_try)

    def set_menu(self):
        """set menu"""
        menu = self.menuBar()

        file = menu.addMenu("&File")
        file.addAction(self.openAction)
        file.addAction(self.exitAction)

    def open_call(self):
        """open lesson"""
        try:
            name = QFileDialog.getOpenFileName(self, 'Open File')[0]
            text = open(name, "r").read()

            if not check_text(text):
                raise Exception("Your text doesn't match")

            self.start_configure(text)
            self.current_text_name = name.split("/")[-1]

        except Exception as exception:
            self.statusBar().showMessage(str(exception))

    def exit_call(self):
        """exit application"""
        exit(0)

    def keyPressEvent(self, event):
        """detect user actions. If lesson started, makes equality check of user input"""
        if not (self.flags["ready"]):
            return

        key = event.text()

        if not key:
            return

        if self.current_char != key:
            if self.pointer != 0:
                self.mistakes_count += 1
            self.statusBar().showMessage(f"Current letter: {self.current_char}")
            return

        if not self.flags["timer"]:
            self.flags["timer"] = True

        try:
            self.pointer += 1

            self.dynamic_string.setText(
                self.text[self.pointer:self.pointer + min(DYNAMIC_STRING_SIZE, len(self.text))]
            )

            self.current_char = next(self.text_iterator)

        except StopIteration:
            self.save_statistic()
            self.show_statistics()
            self.restart_try()

    def start_configure(self, text):
        """start lesson configuration"""
        self.timer_counter = 0
        self.mistakes_count = 0
        self.pointer = 0
        self.text = text
        self.text_iterator = iter(text)
        self.current_char = next(self.text_iterator)
        self.flags["ready"] = True

        self.dynamic_string.setText(
            text[self.pointer:min(DYNAMIC_STRING_SIZE, len(text))]
        )

    def end_configure(self):
        """end lesson configuration"""
        self.text = None
        self.text_iterator = None
        self.current_char = None
        self.flags["ready"] = False
        self.flags["timer"] = False

        self.dynamic_string.setText("Open your file")

    def show_time(self):
        """display lesson length"""
        if self.flags["timer"]:
            self.timer_counter += 1
        self.stopwatch.setText(str(self.timer_counter / 10))
        if self.pointer:
            percentages = int(
                (self.pointer / (self.pointer + self.mistakes_count)) * 100
            )
        else:
            percentages = 100
        self.statistic.setText(f"Statistic:\n{percentages}%")

    def restart_try(self):
        """restart lesson"""
        if not self.text:
            return
        text = self.text
        self.end_configure()
        self.start_configure(text)

    def pause_try(self):
        """pause lesson"""
        self.flags["timer"] = False

    def show_statistics(self):
        """open statistics window"""
        self.pause_try()
        self.SW.show()
    
    def save_statistic(self):
        """save lesson statistic"""
        try:
            file = open("resources/statistics.txt", "a")

            result = self.statistic.text().split("\n")[-1]
            time = self.stopwatch.text()
            speed = int(len(self.text) / (self.timer_counter / 10) * 60)
            print(f"Name: {self.current_text_name}, Result: {result}, Time: {time} seconds, Speed(per minute): {speed}", file=file)

            file.close()
        except Exception:
            self.statusBar().showMessage("unable to save statistic")
