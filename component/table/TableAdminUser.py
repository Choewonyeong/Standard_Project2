from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from component.material.TableLineEdit import TableLineEdit
from component.material.TableComboBox import TableComboBox
from component.material.TablePushButton import TablePushButton


class TableAdminUser(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__setData__()
        # self.__setWidth__()

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.editLog = []
        self.objects = []
        self.columns = self.connUser.dataFrameUser(column=True)+['']
        print(self.columns)
        self.dataFrame = self.connUser.dataFrameUser()
        del self.dataFrame[self.columns[14]]
        self.columns.pop(14)

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
                if col in [1, 2, 7, 8, 9, 10, 11]:
                    TableLineEdit(row, col, data, self)
                elif col == 3:
                    TableComboBox(row, col, ['', '이사', '부장', '차장', '과장', '대리', '사원'], data, self)
                elif col == 4:
                    TableLineEdit(row, col, data, self, option="identity")
                elif col == 5:
                    TableLineEdit(row, col, data, self, option="phone")
                elif col == 6:
                    TableComboBox(row, col, ['', '박사', '석사', '학사', '전문대졸', '고졸'], data, self)
                elif col == 12:
                    TableComboBox(row, col, ['', '재직', '휴직', '파견', '정직', '퇴직'], data, self)
                elif col == 13:
                    TableComboBox(row, col, ['사용자', '관리자'], data, self)
            col = len(self.columns)-1
            TablePushButton(row, col, '삭제', self, option='User')
        self.resizeColumnsToContents()
        self.setColumnWidth(1, 50)
        self.setColumnWidth(2, 100)
        self.setColumnWidth(4, 80)
        self.setColumnWidth(5, 100)
        self.setColumnWidth(6, 120)
        self.setColumnWidth(7, 120)
        self.setColumnWidth(8, 80)
        self.setColumnWidth(9, 80)
