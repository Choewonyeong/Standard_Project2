from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from Connector.ConnUser import ConnUser
from Connector.ConnMain import ConnMain
from Component.Material.Item import Item
from Component.Material.PushButton import PushButton
from Component.Material.ComboBox import ComboBox
from Component.Dialog.DialogNewUser import DialogNewUser
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Design import Style
from Design import Color
from pandas import ExcelWriter
from datetime import datetime


class WidgetAdminUser(QWidget):
    def __init__(self, dock=None):
        QWidget.__init__(self)
        self.dock = dock
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connUser = ConnUser()
        self.connMain = ConnMain()

    def __variables__(self):
        self.columnsUser, self.dfUser = self.connUser.ColumnAndDfUser()
        self.columnsUser += ['삭제']
        self.currentCell = [0, 0]

    def __component__(self):
        self.__button__()
        self.__table__()
        self.__layout__()

    def __button__(self):
        self.btnInsert = QPushButton('신규')
        self.btnInsert.setStyleSheet(Style.PushButton_Tools)
        self.btnInsert.setShortcut('Ctrl+N')
        self.btnInsert.clicked.connect(self.btnInsertClick)
        self.btnSave = QPushButton('엑셀로 저장')
        self.btnSave.setStyleSheet(Style.PushButton_Excel)
        self.btnSave.clicked.connect(self.btnSaveClick)
        self.btnSave.setShortcut('Ctrl+S')
        self.btnDelete = QPushButton('')
        self.btnDelete.setStyleSheet(Style.PushButton_Hide)
        self.btnDelete.setShortcut('Del')
        self.btnDelete.clicked.connect(self.btnDeleteTextClick)
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnInsert)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnDelete)
        layoutBtn.addWidget(QLabel(''), 10)
        self.btnGroup = QGroupBox()
        self.btnGroup.setLayout(layoutBtn)

    def btnInsertClick(self):
        row = self.tblUser.rowCount()-1
        lastNumber = self.tblUser.item(row, 0).text()
        nextNumber = str(int(lastNumber)+1)
        signIn = DialogNewUser(nextNumber, self.dock)
        signIn.exec_()

    def btnDeleteTextClick(self):
        row = self.tblUser.currentRow()
        col = self.tblUser.currentColumn()
        item = QTableWidgetItem('')
        item.setTextAlignment(Qt.AlignCenter)
        self.tblUser.setItem(row, col, item)
        self.currentCell = [row, col]
        self.refresh()

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption='엑셀로 내보내기', directory='', filter='*.xlsx')[0]
        if filePath != '':
            with ExcelWriter(filePath) as writer:
                _, df = self.connUser.ColumnAndDfUser()
                df.to_excel(writer, sheet_name='회원 정보(상세)', index=False)
                writer.close()

    def __btnDelete__(self, table, row, col):
        btnItem = Item()
        btnDelete = PushButton(btnItem, '삭제')
        btnDelete.setStyleSheet(Style.PushButton_NoApply)
        btnDelete.clicked.connect(self.btnDeleteClick)
        table.setItem(row, col, btnItem)
        table.setCellWidget(row, col, btnDelete)

    def btnDeleteClick(self, value):
        row = self.tblUser.currentRow()
        year = str(datetime.today().year)
        userNumber = self.tblUser.item(row, 0).text()
        userName = self.tblUser.item(row, 1).text()
        dig = DialogMessageBox('',
                               f"""{userName}님의 정보를 삭제합니까?
                                    \n삭제 후에는 되돌릴 수 없습니다.""",
                               True)
        dig.exec_()
        if dig.Yes:
            self.connUser.DeleteUser(userNumber)
            try:
                self.connMain.DeleteUser(year, userName)
            except Exception as e:
                print(e)
            self.currentCell = [0, 0]
            self.refresh()
        else:
            pass

    def __comboBox__(self, row, col, items, text):
        item = Item()
        comboBox = ComboBox(item, items)
        comboBox.setStyleSheet(Style.ComboBox_InTable)
        comboBox.setCurrentText(text)
        comboBox.currentTextChanged.connect(self.updateComboBoxData)
        self.tblUser.setItem(row, col, item)
        self.tblUser.setCellWidget(row, col, comboBox)

    def updateComboBoxData(self, text):
        row = self.tblUser.currentRow()
        col = self.tblUser.currentColumn()
        column = self.tblUser.horizontalHeaderItem(col).text()
        userNumber = self.tblUser.item(row, 0).text()
        self.connUser.UpdateUser(column, text, userNumber)
        self.currentCell = [row, col]
        self.refresh()

    def __table__(self):
        self.tblUser = QTableWidget()
        self.tblUser.setStyleSheet(Style.Table_Standard)
        self.tblUser.setRowCount(0)
        self.tblUser.setColumnCount(len(self.columnsUser))
        self.tblUser.setHorizontalHeaderLabels(self.columnsUser)
        for col, header in enumerate(self.columnsUser):
            item = QTableWidgetItem(self.columnsUser[col])
            if col in [1, 2, 3, 4, 14, 15, 17]:
                item.setForeground(Color.EditableHeaderColor)
            else:
                item.setForeground(Color.NoEditableHeaderColor)
            self.tblUser.setHorizontalHeaderItem(col, item)
        cols = self.tblUser.columnCount()-1
        for row, lst in enumerate(self.dfUser.values):
            self.tblUser.insertRow(row)
            self.tblUser.setRowHeight(row, 60)
            self.__btnDelete__(self.tblUser, row, cols)
            self.__comboBox__(row, 4, ['이사', '부장', '차장', '과장', '대리', '사원', '신입'], lst[4])
            self.__comboBox__(row, 14, ['재직', '파견', '휴직', '정직', '퇴직'], lst[14])
            self.__comboBox__(row, 15, ['사용자', '관리자'], lst[15])
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                if col in [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]:
                    item.setFlags(Qt.ItemIsEditable)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                item.setTextAlignment(Qt.AlignCenter)
                self.tblUser.setItem(row, col, item)
        self.tblUser.resizeColumnsToContents()
        self.tblUser.verticalHeader().setVisible(False)
        self.tblUser.hideColumn(0)
        self.tblUser.cellChanged.connect(self.tblUserCellChange)

    def tblUserCellChange(self, row, col):
        column = self.tblUser.horizontalHeaderItem(col).text()
        text = self.tblUser.item(row, col).text()
        userNumber = self.tblUser.item(row, 0).text()
        self.connUser.UpdateUser(column, text, userNumber)
        self.currentCell = [row, col]
        self.refresh()

    def refresh(self):
        self.dock.currentCell = self.currentCell
        self.dock.refresh()

    def settingReformat(self):
        self.currentCell = self.dock.currentCell
        self.tblUser.setCurrentCell(self.currentCell[0], self.currentCell[1])

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnGroup)
        layout.addWidget(self.tblUser)
        self.setLayout(layout)
