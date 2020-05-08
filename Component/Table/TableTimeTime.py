from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Connector.ConnMain import ConnMain
from Component.Method.method import valueTransferBoxToStr
from Component.Method.method import todayReturnBoxToStr
from Design import Style
from Design import Color


class TableTimeTime(QTableWidget):
    def __init__(self, userName, year, alternateRows, widget=None):
        QTableWidget.__init__(self)
        self.userName = userName
        self.year = year
        self.alternateRows = alternateRows
        self.widget = widget
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connMain = ConnMain()

    def __variables__(self):
        self.columnWhole, self.dfWhole = self.connMain.ColumnAndDfTimeWhole(self.year, self.userName)
        self.connMain.ReturnTotalDays(self.year, self.userName, self.columnWhole)
        self.currentCellValue = ''
        todayText = todayReturnBoxToStr()
        self.todayColumn = self.columnWhole.index(todayText)

    def __component__(self):
        self.__tblTime__()

    def __tblTime__(self):
        self.setStyleSheet(Style.Table_Time)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnWhole))
        self.setHorizontalHeaderLabels(self.columnWhole)
        for col in range(self.columnCount()):
            headerItem = self.horizontalHeaderItem(col).text()
            item = QTableWidgetItem(self.columnWhole[col])
            item.setTextAlignment(Qt.AlignCenter)
            if '(토)' in headerItem:
                item.setForeground(Color.SaturdayHeaderColor)
            elif '(일)' in headerItem:
                item.setForeground(Color.SundayHeaderColor)
            self.setHorizontalHeaderItem(col, item)
        for row, lst in enumerate(self.dfWhole.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if row in self.alternateRows:
                    item.setBackground(Color.AlternateRowColor)
                self.setItem(row, col, item)

        self.resizeColumnsToContents()
        self.verticalHeader().setVisible(False)
        for col in range(0, 5):
            self.hideColumn(col)
        self.currentCellChanged.connect(self.getCurrentCellValue)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cellChanged.connect(self.tblTimeChange)

    def getCurrentCellValue(self, row, col, old_row, old_col):
        self.currentCellValue = self.item(row, col).text()

    def tblTimeChange(self, row, col):
        self.changeCellValue = self.item(row, col).text()
        if self.changeCellValue != self.currentCellValue:
            self.currentCellValue = self.changeCellValue
            column = self.horizontalHeaderItem(col).text()
            value = self.item(row, col).text()
            businessNumber = self.item(row, 0).text()
            businessOption = self.item(row, 3).text()
            value = valueTransferBoxToStr(value)
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(Qt.AlignCenter)
            if row in self.alternateRows:
                item.setBackground(Color.AlternateRowColor)
            self.setItem(row, col, item)
            self.connMain.UpdateUserTime(self.year,
                                         self.userName,
                                         column,
                                         value,
                                         businessNumber,
                                         businessOption)
        else:
            pass

