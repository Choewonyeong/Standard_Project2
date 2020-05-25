from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from component.dialog.DialogMassage import DialogMassage


class TableNewUser(QTableWidget):
    def __init__(self, columns, dataFrame):
        QTableWidget.__init__(self)
        self.columns = columns
        self.dataFrame = dataFrame
        self.__setting__()
        self.__setData__()

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __btnAccept__(self, row):
        def btnAcceptClick():
            r = self.currentRow()
            account = self.item(r, 0).text()
            self.connUser.acceptNewUser(account)
            self.removeRow(r)
        btnAccept = QPushButton('승인')
        btnAccept.setFixedWidth(80)
        btnAccept.clicked.connect(btnAcceptClick)
        self.setCellWidget(row, 3, btnAccept)

    def __btnReject__(self, row):
        def btnRejectClick():
            r = self.currentRow()
            account = self.item(r, 0).text()
            self.connUser.rejectNewUser(account)
            msgBox = DialogMassage('계정 정보를 지우시겠습니까?', True)
            if msgBox.value:
                self.connUser.deleteUser(account)
                self.removeRow(r)
        btnReject = QPushButton('거절')
        btnReject.setFixedWidth(80)
        btnReject.clicked.connect(btnRejectClick)
        self.setCellWidget(row, 4, btnReject)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row)
            self.setRowHeight(50, row)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
            self.__btnAccept__(row)
            self.__btnReject__(row)
        self.resizeColumnsToContents()
