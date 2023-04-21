from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit

from constants import STATISTICS_WIDTH, STATISTICS_HEIGHT


class StatisticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lessons Statistic")
        self.setFixedSize(STATISTICS_WIDTH, STATISTICS_HEIGHT)

        self.set_widgets()
        self.set_layout()

        self.addAction(self.pauseAction)

    def set_widgets(self):
        # Lessons statistics list
        self.statistics = QPlainTextEdit(self)

        # Clear button
        self.clear = QPushButton(self)
    
    def set_layout(self):
        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.statistics)
        layout.addWidget(self.clear)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def clear(self):
        pass
