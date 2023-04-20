from windows.MainWindow import MainWindow

import sys
import PyQt5.QtWidgets

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MW = MainWindow()
    MW.show()
    sys.exit(app.exec())
