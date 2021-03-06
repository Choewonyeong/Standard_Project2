from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connDB import connDB
from material import BtnTableDBBusiness


class TableDBBusiness(QTableWidget):
    def __init__(self, year):
        QTableWidget.__init__(self)
        self.year = year
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__setData__()
        self.__setWidth__()

    def __connector__(self):
        self.connDB = connDB(self.year)

    def __variables__(self):
        self.columns = self.connDB.dataFrameBusiness(column=True)
        self.columns[-1] = '설정'
        self.dataFrame = self.connDB.dataFrameBusiness()
        self.dataFrame = self.dataFrame.reset_index(drop=True)
        self.dataFrame = self.dataFrame.drop(len(self.dataFrame)-1)
        self.dataFrame = self.dataFrame.drop(0)

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
                if col == self.columnCount()-1:
                    BtnTableDBBusiness(row, col, data, self, self.year)
            self.resizeColumnsToContents()
            self.hideColumn(0)

    def __setWidth__(self):
        width = 10
        for col in range(1, self.columnCount()):
            width += self.columnWidth(col)
        self.setFixedWidth(width)



