from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from method import totalList
from method import valueTran


class TableTotalPerYear(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__variables__()
        self.__setting__()
        self.__setData__()

    def __variables__(self):
        self.columns = totalList.returnTotalPerYear(column=True)
        self.dataFrame = totalList.returnTotalPerYear()

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
                    data = valueTran.returnTranValue(data)
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                if col != 0:
                    item.setTextAlignment(Qt.AlignCenter)
                if col == 0 and data == '합계':
                    item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, item)
        self.resizeColumnsToContents()
