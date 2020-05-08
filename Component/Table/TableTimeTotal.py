from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Connector.ConnMain import ConnMain
from Component.Method.method import valueTransferBoxToWhole
from Component.Method.method import todayReturnBoxToStr
from Design import Style


class TableTimeTotal(QTableWidget):
    def __init__(self, userName, year, widget=None):
        QTableWidget.__init__(self)
        self.userName = userName
        self.year = year
        self.widget = widget
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connMain = ConnMain()

    def __variables__(self):
        todayColumn = todayReturnBoxToStr()
        self.columnWhole, _ = self.connMain.ColumnAndDfTimeWhole(self.year, self.userName)
        self.listTotal = self.connMain.ReturnTotalDays(self.year, self.userName, self.columnWhole)
        self.todayColumn = self.columnWhole.index(todayColumn)

    def __component__(self):
        self.__tblTime__()

    def __tblTime__(self):
        self.setStyleSheet(Style.Table_TimeTotal)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnWhole))
        self.setHorizontalHeaderLabels(self.columnWhole)
        self.insertRow(0)
        self.setRowHeight(0, 50)
        for col, data in enumerate(self.listTotal):
            value = valueTransferBoxToWhole(str(data))
            item = QTableWidgetItem(str(value))
            item.setFlags(Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignCenter)
            self.setItem(0, col, item)
        self.resizeColumnsToContents()
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        for col in range(0, 5):
            self.hideColumn(col)
        height = self.rowHeight(0)
        self.setFixedHeight(height)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
