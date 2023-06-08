"""
The main part of the messenger that needs to be executed.
"""
import sys
from PySide6 import QtWidgets
from messenger import Welcome

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Welcome('http://127.0.0.1:5000')
    window.show()
    app.exec()