from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from Connector.ConnUser import ConnUser
from Connector.ConnBusiness import ConnBusiness
from Connector.ConnMain import ConnMain
from Component.Material.CheckBox import CheckBox
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Design import Style
from Design import Color
from datetime import datetime


class WidgetCreateDatabase(QWidget):
    def __init__(self, dock=None):
        QWidget.__init__(self)
        self.dock = dock
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connUser = ConnUser()
        self.connBusiness = ConnBusiness()
        self.connMain = ConnMain()

    def __variables__(self):
        self.columnsUser, self.dfUser = self.connUser.ColumnAndDfUser()
        self.columnsBusiness, self.dfBusiness = self.connBusiness.ColumnAndDfBusiness()
        self.columnsUser = ['선택']+self.columnsUser
        self.columnsBusiness = ['선택']+self.columnsBusiness
        self.currentTables = self.connMain.ReturnTables()
        self.checkUser = []
        self.checkBusiness = [0, 1]

    def __component__(self):
        self.__combobox__()
        self.__button__()
        self.__groupbox__()
        self.__lblUser__()
        self.__lblBusiness__()
        self.__tblUSer__()
        self.__tblBusiness__()
        self.__layout__()

    def __combobox__(self):
        self.cbxYear = QComboBox()
        self.cbxYear.setStyleSheet(Style.ComboBox_OutTable)
        year = datetime.today().year
        years = [f"{year-5+i}" for i in range(0, 8)]
        self.cbxYear.addItems(years)
        self.cbxYear.setCurrentText(f"{year+1}")
        self.cbxYear.currentTextChanged.connect(self.cbxYearTextChange)
        self.currentYear = self.cbxYear.currentText()

    def cbxYearTextChange(self):
        self.dock.currentYear = self.cbxYear.currentText()

    def __button__(self):
        self.btnComplete = QPushButton('생성')
        self.btnComplete.setStyleSheet(Style.PushButton_Tools)
        self.btnComplete.clicked.connect(self.btnCompleteClick)

    def __groupbox__(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('연도 선택'))
        layout.addWidget(self.cbxYear)
        layout.addWidget(self.btnComplete)
        layout.addWidget(QLabel(''), 10)
        self.btnGroup = QGroupBox()
        self.btnGroup.setLayout(layout)

    def btnCompleteClick(self):
        if not self.checkUser:
            dig = DialogMessageBox('알림',
                                   '데이터베이스를 생성하기 위한 \n부서원을 선택하세요.',
                                   False)
            dig.exec_()

        elif not self.checkBusiness:
            dig = DialogMessageBox('알림',
                                   '데이터베이스에 적용할 \n사업을 선택하세요',
                                   False)
            dig.exec_()
        elif self.cbxYear.currentText() in self.currentTables:
            dig = DialogMessageBox('알림',
                                   f"""{self.cbxYear.currentText()}년의 데이터베이스가 이미 존재합니다.
                                   \n해당년도의 데이터베이스를 새로 생성하시겠습니까?""",
                                   True)
            dig.exec_()
            if dig.Yes:
                self.connMain.DropTable(self.cbxYear.currentText())
                self.__createNewDataBase__()
                self.dock.refresh()
        else:
            self.__createNewDataBase__()
            self.dock.refresh()

    def __createNewDataBase__(self):
        userNames = []
        for row in self.checkUser:
            userNames.append(self.tblUser.item(row, 2).text())

        businessData = []
        for row in self.checkBusiness:
            businessList = [self.tblBusiness.item(row, 1).text(),
                            self.tblBusiness.item(row, 2).text(),
                            self.tblBusiness.item(row, 3).text()]
            businessData.append(businessList)
        year = self.cbxYear.currentText()
        self.connMain.CreateNewYear(year)
        self.connMain.InsertData(year, userNames, businessData)
        self.connMain.AlterColumns(year)

    def __lblUser__(self):
        self.lblUser = QLabel(f'부서원 선택 수 : {len(self.checkUser)}')
        self.lblUser.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def __lblBusiness__(self):
        self.lblBusiness = QLabel(f'사업 선택 수 : {len(self.checkBusiness)}')
        self.lblBusiness.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def __cbxUser__(self, table, row, col):
        cbxItem = QTableWidgetItem()
        checkBox = CheckBox(cbxItem)
        checkBox.stateChanged.connect(self.cbxUserStateChange)
        if row != 0 and row % 2 == 1:
            cbxItem.setBackground(Color.AlternateRowColor)
        table.setItem(row, col, cbxItem)
        table.setCellWidget(row, col, checkBox)

    def cbxUserStateChange(self, value):
        row = self.tblUser.currentRow()
        if value == 2:
            self.checkUser.append(row)
        if value == 0:
            self.checkUser.remove(row)
        self.lblUser.setText(f'부서원 선택 수 : {len(self.checkUser)}')

    def __cbxBusiness__(self, table, row, col):
        cbxItem = QTableWidgetItem()
        checkBox = CheckBox(cbxItem)
        if row in [0, 1]:
            checkBox.setChecked(True)
            checkBox.setEnabled(False)
        if row != 0 and row % 2 == 1:
            cbxItem.setBackground(Color.AlternateRowColor)
        checkBox.stateChanged.connect(self.cbxBusinessStateChange)
        table.setItem(row, col, cbxItem)
        table.setCellWidget(row, col, checkBox)

    def cbxBusinessStateChange(self, value):
        row = self.tblBusiness.currentRow()
        if value == 2:
            self.checkBusiness.append(row)
        if value == 0:
            self.checkBusiness.remove(row)
        self.lblBusiness.setText(f'사업 선택 수 : {len(self.checkBusiness)}')

    def __tblUSer__(self):
        self.tblUser = QTableWidget()
        self.tblUser.setStyleSheet(Style.Table_Standard)
        self.tblUser.setRowCount(0)
        self.tblUser.setColumnCount(len(self.columnsUser))
        self.tblUser.setHorizontalHeaderLabels(self.columnsUser)
        for row, lst in enumerate(self.dfUser.values):
            self.tblUser.insertRow(row)
            self.tblUser.setRowHeight(row, 50)
            self.__cbxUser__(self.tblUser, row, 0)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.tblUser.setItem(row, col+1, item)
        self.tblUser.resizeColumnsToContents()
        self.tblUser.verticalHeader().setVisible(False)
        self.tblUser.hideColumn(1)
        for col in range(6, 15):
            self.tblUser.hideColumn(col)
        width = 0
        for col in [0, 2, 3, 4, 5, 15, 16, 17]:
            width += self.tblUser.columnWidth(col)
        self.tblUser.setFixedWidth(width+10)

    def __tblBusiness__(self):
        self.tblBusiness = QTableWidget()
        self.tblBusiness.setStyleSheet(Style.Table_Standard)
        self.tblBusiness.setRowCount(0)
        self.tblBusiness.setColumnCount(len(self.columnsBusiness))
        self.tblBusiness.setHorizontalHeaderLabels(self.columnsBusiness)
        for row, lst in enumerate(self.dfBusiness.values):
            self.tblBusiness.insertRow(row)
            self.tblBusiness.setRowHeight(row, 50)
            self.__cbxBusiness__(self.tblBusiness, row, 0)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsEditable)
                item.setTextAlignment(Qt.AlignCenter)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.tblBusiness.setItem(row, col+1, item)
        self.tblBusiness.resizeColumnsToContents()
        self.tblBusiness.verticalHeader().setVisible(False)
        self.tblBusiness.hideColumn(1)
        self.tblBusiness.hideColumn(5)
        self.tblBusiness.hideColumn(6)
        self.tblBusiness.hideColumn(10)
        self.tblBusiness.hideColumn(13)
        self.tblBusiness.hideColumn(14)

    def refresh(self):
        self.dock.currentYear = self.currentYear
        self.dock.refresh()

    def settingReformat(self):
        self.currentYear = self.dock.currentYear
        self.cbxYear.setCurrentText(self.currentYear)

    def __layout__(self):
        layoutUser = QVBoxLayout()
        layoutUser.addWidget(self.lblUser)
        layoutUser.addWidget(self.tblUser)
        layoutBusiness = QVBoxLayout()
        layoutBusiness.addWidget(self.lblBusiness)
        layoutBusiness.addWidget(self.tblBusiness)
        layoutTbl = QHBoxLayout()
        layoutTbl.addLayout(layoutUser)
        layoutTbl.addLayout(layoutBusiness)
        layout = QVBoxLayout()
        layout.addWidget(self.btnGroup)
        layout.addLayout(layoutTbl)
        self.setLayout(layout)