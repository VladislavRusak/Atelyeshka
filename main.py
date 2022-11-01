import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from window import *

from db.service import service


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(400, 500)
    widget.show()

    sys.exit(app.exec())
