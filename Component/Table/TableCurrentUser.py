from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from Component.Material.PushButton import PushButton
from Component.Material.Item import Item
from Connector.ConnMain import ConnMain
from Connector.ConnUser import ConnUser
from Design import Style
from Design import Color


class TableCurrentUser(QTableWidget):
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

    def __variables__(self):
        self.columnUser, self.dfUser = self.connUser.ColumnAndDfUser()
        self.columnUser += ['DB 적용 상태']
        self.userUser = self.connUser.ReturnUserNames()
        self.userMain = self.connMain.ReturnUserNames(self.year)

    def __component__(self):
        self.__tblUser__()

    def __btnUserEnable__(self, table, row, col):
        btnItem = Item()
        btnEnable = PushButton(btnItem, '제외')
        btnEnable.setStyleSheet(Style.PushButton_NoApply)
        btnEnable.clicked.connect(self.btnUserEnableClick)
        table.setItem(row, col, btnItem)
        table.setCellWidget(row, col, btnEnable)

    def btnUserEnableClick(self):
        row = self.currentRow()
        userName = self.item(row, 1).text()
        _, businessData = self.connMain.ColumnAndDfBusiness(self.year)
        businessData = businessData.drop_duplicates()
        businessData = [list(data) for data in businessData.values]
        self.connMain.InsertUser(self.year, userName, businessData)
        self.widget.refresh()

    def __btnUserDisable__(self, table, row, col):
        btnItem = Item()
        btnDisable = PushButton(btnItem, '적용')
        btnDisable.setStyleSheet(Style.PushButton_Apply)
        btnDisable.clicked.connect(self.btnUserDisableClick)
        table.setItem(row, col, btnItem)
        table.setCellWidget(row, col, btnDisable)
        if len(self.userMain) < 2:
            btnDisable.setEnabled(False)

    def btnUserDisableClick(self):
        row = self.currentRow()
        userName = self.item(row, 1).text()
        self.connMain.DeleteUser(self.year, userName)
        self.widget.refresh()

    def __tblUser__(self):
        self.setStyleSheet(Style.Table_Standard)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnUser))
        self.setHorizontalHeaderLabels(self.columnUser)
        cols = self.columnCount()-1
        for row, lst in enumerate(self.dfUser.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            if lst[1] in self.userMain:
                self.__btnUserDisable__(self, row, cols)
            else:
                self.__btnUserEnable__(self, row, cols)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.setItem(row, col, item)
        self.resizeColumnsToContents()
        self.verticalHeader().setVisible(False)
        for col in range(5, 14):
            self.hideColumn(col)
        for col in [0, 15, 16]:
            self.hideColumn(col)
        width = 0
        for col in [1, 2, 3, 4, 14, 17]:
            width += self.columnWidth(col)
        self.setFixedWidth(width+5)
