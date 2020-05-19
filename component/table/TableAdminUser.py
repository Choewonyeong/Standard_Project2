from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from component.material.comboBox import comboBox
from component.dialog.DialogMassage import DialogMassage


class TableAdminUser(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__connUser__()
        self.__variables__()
        self.__setting__()
        self.__setData__()

    def __connUser__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.columns = self.connUser.dataFrameUser(column=True)+['']
        self.dataFrame = self.connUser.dataFrameUser()

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __cbxPosition__(self, row):
        def cbxPositionChange():
            cbx = self.sender()
            r, c = cbx.row, cbx.col
            account = self.item(r, 0).text()
            position = self.cellWidget(r, c).currentText()
            self.connUser.updatePosition(account, position)
        col = self.columns.index('직급')
        currentPosition = self.item(row, col).text()
        cbxPosition = comboBox(row, col)
        cbxPosition.addItems(['', '이사', '부장', '차장', '과장', '대리', '사원'])
        cbxPosition.setCurrentText(currentPosition)
        cbxPosition.setFixedWidth(80)
        cbxPosition.currentTextChanged.connect(cbxPositionChange)
        self.setCellWidget(row, col, cbxPosition)

    def __cbxDegree__(self, row):
        def cbxDegreeChange():
            cbx = self.sender()
            r, c = cbx.row, cbx.col
            account = self.item(r, 0).text()
            degree = self.cellWidget(r, c).currentText()
            self.connUser.updateDegree(account, degree)

        col = self.columns.index('최종학력')
        currentDegree = self.item(row, col).text()
        cbxDegree = comboBox(row, col)
        cbxDegree.addItems(['', '박사', '석사', '학사', '전문대졸', '고졸'])
        cbxDegree.setCurrentText(currentDegree)
        cbxDegree.setFixedWidth(80)
        cbxDegree.currentTextChanged.connect(cbxDegreeChange)
        self.setCellWidget(row, col, cbxDegree)

    def __cbxStatus__(self, row):
        def cbxStatusChange():
            cbx = self.sender()
            r, c = cbx.row, cbx.col
            account = self.item(r, 0).text()
            status = self.cellWidget(r, c).currentText()
            self.connUser.updateStatus(account, status)

        col = self.columns.index('재직상태')
        currentStatus = self.item(row, col).text()
        cbxStatus = comboBox(row, col)
        cbxStatus.addItems(['', '재직', '휴직', '파견', '정직', '퇴직'])
        cbxStatus.setCurrentText(currentStatus)
        cbxStatus.setFixedWidth(80)
        cbxStatus.currentTextChanged.connect(cbxStatusChange)
        self.setCellWidget(row, col, cbxStatus)

    def __cbxAuthor__(self, row):
        def cbxAuthorChange():
            cbx = self.sender()
            r, c = cbx.row, cbx.col
            account = self.item(r, 0).text()
            author = self.cellWidget(r, c).currentText()
            self.connUser.updateAuthor(account, author)
        col = self.columns.index('접근권한')
        currentAuthor = self.item(row, col).text()
        cbxAuthor = comboBox(row, col)
        cbxAuthor.addItems(['사용자', '관리자'])
        cbxAuthor.setCurrentText(currentAuthor)
        cbxAuthor.setFixedWidth(80)
        cbxAuthor.currentTextChanged.connect(cbxAuthorChange)
        self.setCellWidget(row, col, cbxAuthor)

    def __btnDelete__(self, row):
        def btnDeleteClick():
            r = self.currentRow()
            account = self.item(r, 0).text()
            msgBox = DialogMassage('계정 정보를 지우시겠습니까?', True)
            if msgBox.value:
                self.connUser.deleteUser(account)
                self.removeRow(r)
        col = self.columns.index('')
        btnDelete = QPushButton('삭제')
        btnDelete.setFixedWidth(80)
        btnDelete.clicked.connect(btnDeleteClick)
        self.setCellWidget(row, col, btnDelete)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row)
            self.setRowHeight(50, row)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                if col == 0:
                    item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
            self.__cbxPosition__(row)
            self.__cbxDegree__(row)
            self.__cbxStatus__(row)
            self.__cbxAuthor__(row)
            self.__btnDelete__(row)
        self.resizeColumnsToContents()

        width = 10
        for col, header in enumerate(self.columns):
            width += self.columnWidth(col)
        self.setFixedWidth(width)
