from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from method.totalList import returnTotalPerUser
from method.valueTran import returnTranValue


class TableTotalPerUser(QTableWidget):
    def __init__(self, year, userName, columns, dataFrame):
        QTableWidget.__init__(self)
        self.year = year
        self.userName = userName
        self.columns = columns
        self.dataFrame = dataFrame
        self.__variables__()
        self.__setting__()
        self.__setData__()

    def __variables__(self):
        self.columns = returnTotalPerUser(self.year, column=True)

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row)
            for col, data in enumerate(lst):
                if col != 0:
                    data = returnTranValue(data)
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, item)
        self.resizeColumnsToContents()