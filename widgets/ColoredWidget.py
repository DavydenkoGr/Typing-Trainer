from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class ColoredWidget(QWidget):
    """additional widget, use it to set background color to widget"""
    def __init__(self, color):
        """initialization of container for widgets"""
        super(ColoredWidget, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
