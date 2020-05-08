from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Component.Material.PushButton import PushButton
from Component.Material.Item import Item
from Connector.ConnMain import ConnMain
from Connector.ConnUser import ConnUser
from Connector.ConnBusiness import ConnBusiness
from Design import Style
from Design import Color


class TableCurrentBusiness(QTableWidget):
    def __init__(self, year, widget=None):
        QTableWidget.__init__(self)
        self.year = year
        self.widget = widget
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connUser = ConnUser()
        self.connMain = ConnMain()
        self.connBusiness = ConnBusiness()

    def __variables__(self):
        self.columnBusiness, self.dfBusiness = self.connBusiness.ColumnAndDfBusiness()
        self.columnBusiness += ['DB 적용 상태']
        self.businessBusiness = self.connBusiness.ReturnBusinessData()
        _, dfBusinessMain = self.connMain.ColumnAndDfBusiness(self.year)
        self.businessMain = [list(businessData)[1] for businessData in dfBusinessMain.values]
        self.businessDict = {}
        for businessData in self.businessBusiness:
            self.businessDict[businessData[1]] = businessData

    def __component__(self):
        self.__tblBusiness__()

    def __btnBusinessEnable__(self, table, row, col):
        btnItem = Item()
        btnEnable = PushButton(btnItem, '제외')
        btnEnable.setStyleSheet(Style.PushButton_NoApply)
        btnEnable.clicked.connect(self.btnBusinessEnable)
        table.setItem(row, col, btnItem)
        table.setCellWidget(row, col, btnEnable)

    def btnBusinessEnable(self):
        row = self.currentRow()
        businessName = self.item(row, 1).text()
        businessData = self.businessDict[businessName]
        userNames = self.connMain.ReturnUserNames(self.year)
        self.connMain.InsertBusiness(self.year, businessData, userNames)
        self.widget.refresh()

    def __btnBusinessDisable__(self, table, row, col):
        btnItem = Item()
        btnDisable = PushButton(btnItem, '적용')
        btnDisable.setStyleSheet(Style.PushButton_Apply)
        btnDisable.clicked.connect(self.btnBusinessDisable)
        table.setItem(row, col, btnItem)
        table.setCellWidget(row, col, btnDisable)
        if table.item(row, 1).text() in ['일반업무', '타 부서 업무 지원']:
            btnDisable.setEnabled(False)
            
    def btnBusinessDisable(self):
        row = self.currentRow()
        businessNumber = self.item(row, 0).text()
        self.connMain.DeleteBusiness(self.year, businessNumber)
        self.widget.refresh()

    def __tblBusiness__(self):
        self.setStyleSheet(Style.Table_Standard)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnBusiness))
        self.setHorizontalHeaderLabels(self.columnBusiness)
        cols = self.columnCount()-1
        for row, lst in enumerate(self.dfBusiness.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.setItem(row, col, item)
            if lst[1] in self.businessMain:
                self.__btnBusinessDisable__(self, row, cols)
            else:
                self.__btnBusinessEnable__(self, row, cols)
        self.resizeColumnsToContents()
        self.verticalHeader().setVisible(False)
        for col in [0, 5, 12, 13, 15]:
            self.hideColumn(col)
        width = 0
        for col in [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 14, 16]:
            width += self.columnWidth(col)
        self.setFixedWidth(width+5)
