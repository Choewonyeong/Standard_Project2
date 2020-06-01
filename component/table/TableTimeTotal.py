from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connDB import connDB
from material import LdtTableTotal


class TableTimeTotal(QTableWidget):
    def __init__(self, account, year, columns):
        QTableWidget.__init__(self)
        self.account = account
        self.year = year
        self.columns = columns
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__setData__()

    def __connector__(self):
        self.connDB = connDB(self.year)

    def __variables__(self):
        self.lst = self.connDB.listTotal(self.columns, self.account)

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.lst))
        self.setHorizontalHeaderLabels(self.lst)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def __setData__(self):
        self.insertRow(0)
        for col, data in enumerate(self.lst):
            item = QTableWidgetItem(str(data))
            item.setFlags(Qt.ItemIsEditable)
            self.setItem(0, col, item)
            LdtTableTotal(0, col, str(data), self)
        self.resizeColumnsToContents()
