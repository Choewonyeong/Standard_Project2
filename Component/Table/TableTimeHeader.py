from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Design import Style


class TableTimeHeader(QTableWidget):
    def __init__(self, userName, year, width, height, widget=None):
        QTableWidget.__init__(self)
        self.userName = userName
        self.year = year
        self.width = width
        self.height = height
        self.widget = widget
        self.__component__()

    def __component__(self):
        self.__tblHeader__()

    def __tblHeader__(self):
        self.setStyleSheet(Style.Table_Header)
        self.setRowCount(0)
        self.setColumnCount(1)
        self.insertRow(0)
        self.setRowHeight(0, 50)
        self.setColumnWidth(0, self.width)
        item = QTableWidgetItem('일간 합계')
        item.setFlags(Qt.ItemIsEditable)
        item.setTextAlignment(Qt.AlignCenter)
        self.setItem(0, 0, item)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
