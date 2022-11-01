import PyQt5
# from PyQt5 import *
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class OrdersList(QWidget):

    signal = pyqtSignal(str)

    def __init__(self, window=None):
        super().__init__()
        self.setWindowTitle("Список заказов")
        self.setMainUI()
        self.setGeometry(300, 300, 400, 500)
        self.window = window

    def setMainUI(self):
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)

        self.table = QTableWidget()
        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        # storage = Storage() # TODO: конект к запросу.
        # st_def_val = StorageDefVal()
        thead = ["ID", "Услуга", "Вещи", "Заказчик", "Статус"]
        col_num = 0
        for val in thead:
            self.table.setItem(0, col_num, QTableWidgetItem(str(val)))
            col_num += 1

        self.setLayout(self.layout)
