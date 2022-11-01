# import PyQt5
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AddFormWindow(QWidget):
    signal = pyqtSignal(str)

    def __init__(self, window=None):
        super().__init__()
        self.setWindowTitle("Добавить заказ")
        self.setMainUI()
        self.setGeometry(300, 300, 400, 500)
        self.window = window

    def setMainUI(self):
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)

        full_name = QLineEdit()
        phone_num = QLineEdit()
        things = QLineEdit()
        service = QLineEdit()
        add_b = QPushButton('Добавить заказ')

        Row1 = QLabel("Имя Фамилия")
        Row2 = QLabel("Номер телефона")
        Row3 = QLabel("Вещи")
        Row4 = QLabel("Услуга")

        full_name.setPlaceholderText("Имя Фамилия")
        phone_num.setPlaceholderText("+7(***)-***-**-**")
        things.setPlaceholderText("Футболка, штаны, ...")
        service.setPlaceholderText("Зашить, пришить, приштопать")

        self.layout.addWidget(Row1)
        self.layout.addWidget(full_name)
        self.layout.addWidget(Row2)
        self.layout.addWidget(phone_num)
        self.layout.addWidget(Row3)
        self.layout.addWidget(things)
        self.layout.addWidget(Row4)
        self.layout.addWidget(service)
        self.layout.addWidget(add_b)

        # full_name.released.connect(add)
        # phone_num.released.connect(add)
        # things.released.connect(add)
        # service.released.connect(add)
        add_b.released.connect(self.add)

        self.setLayout(self.layout)

    def add(full_name, phone_num, things, service):
        print(full_name, phone_num, things, service)
