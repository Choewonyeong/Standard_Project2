from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connBusiness import connBusiness
from component.material.TableLineEdit import TableLineEdit
from component.material.TableComboBox import TableComboBox
from component.material.TablePushButton import TablePushButton
from component.material.TableTextEdit import TableTextEdit


class TableAdminBusiness(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__setData__()
        self.__setWidth__()

    def __connector__(self):
        self.connBusiness = connBusiness()

    def __variables__(self):
        self.editLog = []
        self.objects = []
        self.columns = self.connBusiness.dataFrameBusiness(column=True)+['']
        self.dataFrame = self.connBusiness.dataFrameBusiness()
        for idx, col in enumerate(self.columns):
            print(idx, col)

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
                if col in [1, 2, 4, 10, 11, 12]:
                    TableLineEdit(row, col, data, self)
                elif col == 3:
                    TableComboBox(row, col, ['기술', '연구', '국책', '일반', '기타'], data, self)
                elif col == 5:
                    TableTextEdit(row, col, data, self)
                elif col in [6, 7, 9]:
                    TableLineEdit(row, col, data, self, option='dateFormat')
                elif col == 13:
                    TableLineEdit(row, col, data, self, option='moneyFormat')
                elif col == 14:
                    TableComboBox(row, col, ['수주', '진행', '중단', '준공', 'A/S'], data, self)

    def __setWidth__(self):
        width = 10
        for col, header in enumerate(self.columns):
            width += self.columnWidth(col)
        self.setFixedWidth(width)
