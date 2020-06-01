from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from material import FilterComboBox
from connector.connUser import connUser
from material import TableLineEdit
from material import TableComboBox
from material import BtnTableUserDelete
from material import BtnTableUserPassword


class TableAdminUser(QTableWidget):
    def __init__(self, widget):
        QTableWidget.__init__(self)
        self.widget = widget
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__setFilter__()
        self.__setData__()

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.editLog = []
        self.objects = []
        self.columns = self.connUser.dataFrameUser(column=True)+['비밀번호', '설정']
        self.dataFrame = self.connUser.dataFrameUser()
        del self.dataFrame[self.columns[14]]
        del self.dataFrame[self.columns[2]]
        self.columns.pop(14)
        self.columns.pop(2)

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __setFilter__(self):
        self.insertRow(0)
        self.setRowHeight(0, 20)
        for idx, header in enumerate(self.columns):
            if header in ['수정한날짜', '비밀번호', '설정']:
                item = QTableWidgetItem('')
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(0, idx, item)
            else:
                items = ['필터'] + self.dataFrame[header].drop_duplicates().tolist()
                FilterComboBox(idx, items, self)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row+1)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row+1, col, item)
                if col in [1, 6, 7, 8, 9, 10]:
                    TableLineEdit(row+1, col, data, self)
                elif col == 2:
                    TableComboBox(row+1, col, ['', '이사', '부장', '차장', '과장', '대리', '사원'], data, self)
                elif col == 3:
                    TableLineEdit(row+1, col, data, self, option="identity")
                elif col == 4:
                    TableLineEdit(row+1, col, data, self, option="phone")
                elif col == 5:
                    TableComboBox(row+1, col, ['', '박사', '석사', '학사', '전문대졸', '고졸'], data, self)
                elif col == 11:
                    TableComboBox(row+1, col, ['', '재직', '휴직', '파견', '정직', '퇴직'], data, self)
                elif col == 12:
                    TableComboBox(row+1, col, ['사용자', '관리자'], data, self)
            col = len(self.columns)-2
            BtnTableUserPassword(row+1, col, '확인', self)
            col = col+1
            BtnTableUserDelete(row+1, col, '삭제', self)
        self.resizeColumnsToContents()
        self.setColumnWidth(1, 60)
        self.setColumnWidth(3, 80)
        self.setColumnWidth(4, 100)
        self.setColumnWidth(5, 80)
        self.setColumnWidth(6, 120)
        self.setColumnWidth(7, 120)
        self.setColumnWidth(8, 80)
        self.setColumnWidth(9, 80)

    def UpdateEditDate(self, row, editDate):
        item = QTableWidgetItem(editDate)
        item.setFlags(Qt.ItemIsEditable)
        self.setItem(row, 13, item)

    def Show(self):
        for row in range(1, self.rowCount()):
            self.showRow(row)

    def Filter(self, col, filterText):
        self.Show()
        for row in range(1, self.rowCount()):
            if self.cellWidget(0, col).currentText() == '필터':
                self.Show()
            elif col == 0 and self.item(row, col).text() != filterText:
                self.hideRow(row)
            elif col in [2, 5, 11, 12] and self.cellWidget(row, col).currentText() != filterText:
                self.hideRow(row)
            elif col not in [0, 2, 5, 11, 12] and self.cellWidget(row, col).text() != filterText:
                self.hideRow(row)

