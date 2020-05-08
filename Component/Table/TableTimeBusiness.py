from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Connector.ConnMain import ConnMain
from Design import Style
from Design import Color


class TableTimeBusiness(QTableWidget):
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
        self.columnBusiness, self.dfBusiness = self.connMain.ColumnAndDfTimeBusiness(self.year, self.userName)
        lstBusiness = [list(data) for data in self.dfBusiness.values]
        self.onlyRows = [3*(cnt//3-1) for cnt in range(3, len(lstBusiness)+1, 3)]
        self.alternateRows = []
        for x in range(3, len(self.dfBusiness), 6):
            for y in range(0, 3):
                self.alternateRows.append(x+y)

    def __component__(self):
        self.__tblBusiness__()

    def __tblBusiness__(self):
        self.setStyleSheet(Style.Table_Time)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnBusiness))
        self.setHorizontalHeaderLabels(self.columnBusiness)
        for row, lst in enumerate(self.dfBusiness.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                if row in self.onlyRows or col == 3:
                    item = QTableWidgetItem(str(data))
                else:
                    item = QTableWidgetItem('')
                if row in self.alternateRows:
                    item.setBackground(Color.AlternateRowColor)
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, item)
        self.resizeColumnsToContents()
        self.verticalHeader().setVisible(False)
        self.hideColumn(0)
        width = 0
        for col in range(1, 4):
            width += self.columnWidth(col)
        self.setFixedWidth(width)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
