from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from Connector.ConnBusiness import ConnBusiness
from Connector.ConnMain import ConnMain
from Connector.ConnUser import ConnUser
from Component.Method.method import valueTransferBoxToWhole
from Design import Style
from Design import Color


class TableInquiryTimePerBusiness(QTableWidget):
    def __init__(self, businessName, widget=None):
        QTableWidget.__init__(self)
        self.businessName = businessName
        self.widget = widget
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connMain = ConnMain()
        self.connUser = ConnUser()
        self.connBusiness = ConnBusiness()

    def __variables__(self):
        userNames = self.connUser.ReturnUserNames()
        self.columnTotal, self.dfTotal = self.connMain.ColumnAndDfTotalTimePerBusiness(self.businessName, userNames)

    def __component__(self):
        self.__tblTotal__()

    def __tblTotal__(self):
        self.setStyleSheet(Style.Table_Standard)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnTotal))
        self.setHorizontalHeaderLabels(self.columnTotal)
        col = len(self.columnTotal)-1
        item = QTableWidgetItem(self.columnTotal[col])
        item.setTextAlignment(Qt.AlignCenter)
        item.setForeground(Color.FinalTotalColumnColor)
        self.setHorizontalHeaderItem(col, item)
        for row, lst in enumerate(self.dfTotal.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                value = valueTransferBoxToWhole(data)
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEditable)
                if col == 0:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                if col == len(self.columnTotal)-1:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                    item.setForeground(Color.FinalTotalColumnColor)
                if row == len(self.dfTotal)-1:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                    item.setForeground(Color.FinalTotalColumnColor)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                    self.setColumnWidth(col, 100)
                self.setItem(row, col, item)
        self.verticalHeader().setVisible(False)
