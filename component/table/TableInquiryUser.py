from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from component.dialog.DialogMassage import DialogMassage


class TableInquiryUser(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__connUser__()
        self.__variables__()
        self.__setting__()
        self.__setData__()

    def __connUser__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.columns = self.connUser.dataFrameUser(column=True)
        self.dataFrame = self.connUser.dataFrameUser()
        for col in [14, 13, 12, 2]:
            self.dataFrame = self.dataFrame.drop(self.dataFrame.columns[col],
                                                 axis='columns')
            self.columns.pop(col)

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row)
            self.setRowHeight(50, row)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
        self.resizeColumnsToContents()

        width = 10
        for col, header in enumerate(self.columns):
            width += self.columnWidth(col)
        self.setFixedWidth(width)
