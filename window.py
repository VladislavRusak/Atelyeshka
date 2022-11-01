# import datetime
# import os
# import sqlite3
# import sys

import PyQt5
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from queries import addOrder

from windows.addOrder import *
from windows.orderList import *


class MainWindow(QWidget):
    mainWinSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Ателье Лариса")
        self.setMainUI()
        self.setGeometry(300, 300, 400, 500)
        self.parent = parent

    def setMainUI(self):
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.layout)

        butt1 = QPushButton('Добавить заказ')  # TODO: добавить названия
        butt2 = QPushButton('Список заказанных работ')
        butt3 = QPushButton('В работе')
        butt4 = QPushButton('Законченые заказы')
        butt5 = QPushButton('Клиенты')

        self.layout.addWidget(butt1)
        self.layout.addWidget(butt2)
        self.layout.addWidget(butt3)
        self.layout.addWidget(butt4)
        self.layout.addWidget(butt5)

        # TODO: приконектить к ф-циям адресации
        butt1.released.connect((self.openAddForm))
        butt2.released.connect((self.openOrdersList))
        # butt3.released.connect((self.openProcessedOrders))
        # butt4.released.connect((self.openFinishedOrders))
        # butt5.released.connect((self.openCustomers))

    def resizeEvent(self, event):
        QWidget.resizeEvent(self, event)

    def openAddForm(self):
        self.form = AddFormWindow()
        self.form.show()

    def openOrdersList(self):
        self.form = OrdersList()
        self.form.show()

    # def openProcessedOrders(self):
    #     self.form = ProcessedOrders()
    #     self.form.show()

    # def openFinishedOrders(self):
    #     self.form = FinishedOrders()
    #     self.form.show()

    # def openCustomers(self):
    #     self.form = Customers()
    #     self.form.show()


# class AddFormWindow(QWidget):
#     signal = pyqtSignal(str)

#     def __init__(self, window=None):
#         super().__init__()
#         self.setWindowTitle("Добавить заказ")
#         self.setMainUI()
#         self.setGeometry(300, 300, 400, 500)
#         self.window = window

#     def setMainUI(self):
#         self.layout = QBoxLayout(QBoxLayout.TopToBottom)

#         FullName = QLineEdit()
#         PhoneNum = QLineEdit()
#         DressList = QLineEdit()
#         Service = QLineEdit()
#         add_b = QPushButton('Добавить работу')

#         Row1 = QLabel("Имя Фамилия")
#         Row2 = QLabel("Номер телефона")
#         Row3 = QLabel("Вещи")
#         Row4 = QLabel("Услуга")

#         FullName.setPlaceholderText("Имя Фамилия")
#         PhoneNum.setPlaceholderText("+7(***)-***-**-**")
#         DressList.setPlaceholderText("Футболка, штаны, ...")
#         Service.setPlaceholderText("Зашить, пришить, приштопать")

#         self.layout.addWidget(Row1)
#         self.layout.addWidget(FullName)
#         self.layout.addWidget(Row2)
#         self.layout.addWidget(PhoneNum)
#         self.layout.addWidget(Row3)
#         self.layout.addWidget(DressList)
#         self.layout.addWidget(Row4)
#         self.layout.addWidget(Service)
#         self.layout.addWidget(add_b)

#         self.setLayout(self.layout)


# class OrdersList(QWidget):

#     signal = pyqtSignal(str)

#     def __init__(self, window=None):
#         super().__init__()
#         self.setWindowTitle("Добавить заказ")
#         self.setMainUI()
#         self.setGeometry(300, 300, 400, 500)
#         self.window = window

#     def setMainUI(self):
#         self.layout = QBoxLayout(QBoxLayout.TopToBottom)
#         self.setLayout(self.layout)
#         self.table = QTableWidget()
#         self.table.setRowCount(1)
#         self.table.setColumnCount(4)
#         # storage = Storage() # TODO: конект к запросу.
#         # st_def_val = StorageDefVal()
#         thead = ["ID", "Услуга", "Вещи", "Заказчик", "Статус"]
#         col_num = 0
#         for val in thead:
#             self.table.setItem(0, col_num, QTableWidgetItem(str(val)))
#             col_num += 1


# class ProcessedOrders(QWidget):

#     signal = pyqtSignal(str)

#     def __init__(self, window=None):
#         super().__init__()
#         self.setWindowTitle("Добавить заказ")
#         self.setMainUI()
#         self.setGeometry(300, 300, 800, 600)
#         self.window = window

#     def setMainUI(self):
#         self.layout = QBoxLayout(QBoxLayout.TopToBottom)
#         self.setLayout(self.layout)
#         self.table = QTableWidget()
#         self.table.setRowCount(1)
#         self.table.setColumnCount(4)
#         # storage = Storage() # TODO: конект к запросу.
#         # st_def_val = StorageDefVal()
#         thead = ["ID", "Услуга", "Вещи", "Заказчик", "Статус"]
#         col_num = 0
#         for val in thead:
#             self.table.setItem(0, col_num, QTableWidgetItem(str(val)))
#             col_num += 1


# class FinishedOrders(QWidget):

#     signal = pyqtSignal(str)

#     def __init__(self, window=None):
#         super().__init__()
#         self.setWindowTitle("Добавить заказ")
#         self.setMainUI()
#         self.setGeometry(300, 300, 800, 600)
#         self.window = window

#     def setMainUI(self):
#         self.layout = QBoxLayout(QBoxLayout.TopToBottom)
#         self.setLayout(self.layout)
#         self.table = QTableWidget()
#         self.table.setRowCount(1)
#         self.table.setColumnCount(4)
#         # storage = Storage() # TODO: конект к запросу.
#         # st_def_val = StorageDefVal()
#         thead = ["ID", "Услуга", "Вещи", "Заказчик", "Статус"]
#         col_num = 0
#         for val in thead:
#             self.table.setItem(0, col_num, QTableWidgetItem(str(val)))
#             col_num += 1


# class Customers(QWidget):

#     signal = pyqtSignal(str)

#     def __init__(self, window=None):
#         super().__init__()
#         self.setWindowTitle("Добавить заказ")
#         self.setMainUI()
#         self.setGeometry(300, 300, 800, 600)
#         self.window = window

#     def setMainUI(self):
#         self.layout = QBoxLayout(QBoxLayout.TopToBottom)
#         self.setLayout(self.layout)
#         self.table = QTableWidget()
#         self.table.setRowCount(1)
#         self.table.setColumnCount(3)
#         # storage = Storage() # TODO: конект к запросу.
#         # st_def_val = StorageDefVal()
#         # TODO: можно добавить колонку активыне заказы(true, false)
#         thead = ["ID", "ФИО", "Номер телефона"]
#         col_num = 0
#         for val in thead:
#             self.table.setItem(0, col_num, QTableWidgetItem(str(val)))
#             col_num += 1
