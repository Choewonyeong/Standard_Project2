from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QFileDialog
from Component.Material.ComboBox import ComboBox
from Connector.ConnBusiness import ConnBusiness
from Connector.ConnMain import ConnMain
from Component.Material.Item import Item
from Component.Material.PushButton import PushButton
from Component.Dialog.DialogNewBusiness import DialogNewBusiness
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Design import Style
from Design import Color
from pandas import ExcelWriter
from datetime import datetime


class WidgetAdminBusiness(QWidget):
    def __init__(self, dock=None):
        QWidget.__init__(self)
        self.dock = dock
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connBusiness = ConnBusiness()
        self.connMain = ConnMain()

    def __variables__(self):
        self.columnsBusiness, self.dfBusiness = self.connBusiness.ColumnAndDfBusiness()
        self.columnsBusiness += ['삭제']
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
        self.btnSave.setShortcut('Ctrl+S')
        self.btnSave.clicked.connect(self.btnSaveClick)
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
        row = self.tblBusiness.rowCount()-1
        lastNumber = self.tblBusiness.item(row, 0).text()
        nextNumber = str(int(lastNumber)+1)
        newBusiness = DialogNewBusiness(nextNumber, self)
        newBusiness.exec_()

    def btnDeleteTextClick(self):
        row = self.tblBusiness.currentRow()
        col = self.tblBusiness.currentColumn()
        item = QTableWidgetItem('')
        if row != 0 and row % 2 == 1:
            item.setBackground(Color.AlternateRowColor)
        if col != 5 or col != 13:
            item.setTextAlignment(Qt.AlignCenter)
        elif col == 13:
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.tblBusiness.setItem(row, col, item)
        self.currentCell = [row, col]
        self.refresh()

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption='엑셀로 내보내기', directory='', filter='*.xlsx')[0]
        if filePath != '':
            with ExcelWriter(filePath) as writer:
                _, df = self.connBusiness.ColumnAndDfBusiness()
                df.to_excel(writer, sheet_name='사업 정보(상세)', index=False)
                writer.close()

    def __btnDelete__(self, table, row, col):
        btnItem = Item()
        btnDelete = PushButton(btnItem, '삭제')
        btnDelete.setStyleSheet(Style.PushButton_NoApply)
        btnDelete.clicked.connect(self.btnDeleteClick)
        table.setItem(row, col, btnItem)
        table.setCellWidget(row, col, btnDelete)

    def btnDeleteClick(self, value):
        row = self.tblBusiness.currentRow()
        year = str(datetime.today().year)
        businessNumber = self.tblBusiness.item(row, 0).text()
        businessName = self.tblBusiness.item(row, 1).text()
        dig = DialogMessageBox('',
                               f"""<{businessName}>의 정보를 삭제합니까?
                                    \n삭제 후에는 되돌릴 수 없습니다.""",
                               True)
        dig.exec_()
        if dig.Yes:
            self.connBusiness.DeleteBusiness(businessNumber)
            self.connMain.DeleteBusiness(year, businessNumber)
            self.currentCell = [0, 0]
            self.refresh()

    def __comboBox__(self, row, col, items, text):
        item = Item()
        comboBox = ComboBox(item, items)
        comboBox.setStyleSheet(Style.ComboBox_InTable)
        comboBox.setCurrentText(text)
        comboBox.currentTextChanged.connect(self.updateComboBoxData)
        self.tblBusiness.setItem(row, col, item)
        self.tblBusiness.setCellWidget(row, col, comboBox)

    def updateComboBoxData(self, text):
        row = self.tblBusiness.currentRow()
        col = self.tblBusiness.currentColumn()
        column = self.tblBusiness.horizontalHeaderItem(col).text()
        businessNumber = self.tblBusiness.item(row, 0).text()
        self.connBusiness.UpdateBusiness(column, text, businessNumber)
        self.currentCell = [row, col]
        self.refresh()

    def __table__(self):
        self.tblBusiness = QTableWidget()
        self.tblBusiness.setStyleSheet(Style.Table_Standard)
        self.tblBusiness.setRowCount(0)
        self.tblBusiness.setColumnCount(len(self.columnsBusiness))
        self.tblBusiness.setHorizontalHeaderLabels(self.columnsBusiness)
        for col, header in enumerate(self.columnsBusiness):
            item = QTableWidgetItem(self.columnsBusiness[col])
            if col in range(3, 15) or col == 16:
                item.setForeground(Color.EditableHeaderColor)
            else:
                item.setForeground(Color.NoEditableHeaderColor)
            self.tblBusiness.setHorizontalHeaderItem(col, item)
        cols = self.tblBusiness.columnCount()-1
        for row, lst in enumerate(self.dfBusiness.values):
            self.tblBusiness.insertRow(row)
            self.tblBusiness.setRowHeight(row, 60)
            self.__comboBox__(row, 3, ['기술', '연구', '국책', '일반', '기타'], lst[3])
            self.__comboBox__(row, 14, ['진행', '중단', '준공', 'A/S'], lst[14])
            self.__btnDelete__(self.tblBusiness, row, cols)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                if col in [0, 1, 2, 15]:
                    item.setFlags(Qt.ItemIsEditable)
                if col in [0, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15]:
                    item.setTextAlignment(Qt.AlignCenter)
                elif col == 13:
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.tblBusiness.setItem(row, col, item)
        self.tblBusiness.resizeColumnsToContents()
        self.tblBusiness.setColumnWidth(1, 200)
        self.tblBusiness.setColumnWidth(5, 200)
        self.tblBusiness.verticalHeader().setVisible(False)
        self.tblBusiness.hideColumn(0)
        self.tblBusiness.cellChanged.connect(self.tblBusinessCellChange)

    def tblBusinessCellChange(self, row, col):
        column = self.tblBusiness.horizontalHeaderItem(col).text()
        text = self.tblBusiness.item(row, col).text()
        businessNumber = self.tblBusiness.item(row, 0).text()
        self.connBusiness.UpdateBusiness(column, text, businessNumber)
        self.currentCell = [row, col]
        self.refresh()

    def refresh(self):
        self.dock.currentCell = self.currentCell
        self.dock.refresh()

    def settingReformat(self):
        self.currentCell = self.dock.currentCell
        self.tblBusiness.setCurrentCell(self.currentCell[0], self.currentCell[1])

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnGroup)
        layout.addWidget(self.tblBusiness)
        self.setLayout(layout)
