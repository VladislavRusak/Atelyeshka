import sys
import os
import sqlite3

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from window import *


try:
    sqlite_connection = sqlite3.connect('db/Alelye.sqlite3')
    cursor = sqlite_connection.cursor()
    print("База данных успешно подключена")

    cursor.execute("select sqlite_version();")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к SQLite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто.")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(400, 500)
    widget.show()

    sys.exit(app.exec())
