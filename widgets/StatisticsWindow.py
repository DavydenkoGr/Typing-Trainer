from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit

from constants import STATISTICS_WIDTH, STATISTICS_HEIGHT, FONT_SIZE, BACKGROUND_COLOR, BUTTONS_COLOR


class StatisticsWindow(QWidget):
    """window displays statistics"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.initUI()

    def initUI(self):
        """PyQt element initialization"""
        self.setWindowTitle("Lessons Statistics")
        self.setFixedSize(STATISTICS_WIDTH, STATISTICS_HEIGHT)
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}")

        self.set_widgets()
        self.set_layout()

    def set_widgets(self):
        """set widgets"""
        font = QFont()
        font.setPointSize(FONT_SIZE)

        # Lessons statistics list
        self.statistics = QPlainTextEdit(self)
        self.statistics.setFixedSize(int(STATISTICS_WIDTH * 0.8), int(STATISTICS_HEIGHT * 0.6))

        self.statistics.setStyleSheet("background-color: white")

        # Clear button
        self.clear = QPushButton(self)
        self.clear.setFixedWidth(int(STATISTICS_WIDTH * 0.8))
        self.clear.clicked.connect(self.clear_all)
        self.clear.setFocusPolicy(Qt.NoFocus)

        self.clear.setFont(font)
        self.clear.setStyleSheet(f"background-color: {BUTTONS_COLOR}")
        self.clear.setText("clear all")
    
    def set_layout(self):
        """set window layout"""
        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.statistics, alignment=Qt.AlignCenter)
        layout.addWidget(self.clear, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def show(self):
        """show window"""
        super().show()
        self.show_statistics()

    def show_statistics(self):
        """display statistics to QPlainTextEdit"""
        self.statistics.clear()

        try:
            file = open("resources/statistics.txt", "r")
            for line in file.readlines():
                self.statistics.insertPlainText(line)
        except Exception:
            self.statistics.clear()
            self.statistics.insertPlainText("unable to open file statistics.txt")

    def clear_all(self):
        """clear all lessons statistics"""
        try:
            file = open("resources/statistics.txt", "w")
            file.close()

            self.statistics.clear()
            self.statistics.insertPlainText("Success!")
        except Exception:
            self.statistics.clear()
            self.statistics.insertPlainText("unable to clear file statistics.txt")
