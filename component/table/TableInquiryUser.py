from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from material.ComboBox import CbxFilterInTable
from design.style import Table


class TableInquiryUser(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.setStyleSheet(Table.styleDefault)
        self.__connUser__()
        self.__variables__()
        self.__setting__()
        self.__setFilter__()
        self.__setData__()

    def __connUser__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.columns = self.connUser.dataFrameUser(column=True)
        self.dataFrame = self.connUser.dataFrameUser()
        for col in [14, 13, 12, 2]:
            self.dataFrame = self.dataFrame.drop(self.dataFrame.columns[col], axis='columns')
            self.columns.pop(col)

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __setFilter__(self):
        self.insertRow(0)
        for idx, header in enumerate(self.columns):
            items = ['전체'] + self.dataFrame[header].drop_duplicates().tolist()
            CbxFilterInTable(idx, items, self)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row+1)
            self.setRowHeight(row+1, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row+1, col, item)
        self.resizeColumnsToContents()

    def Show(self):
        for row in range(1, self.rowCount()):
            self.showRow(row)

    def Filter(self, col, filterText):
        self.Show()
        for row in range(1, self.rowCount()):
            if self.cellWidget(0, col).currentText() == '전체':
                self.Show()
            elif self.item(row, col).text() != filterText:
                self.hideRow(row)
