from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGroupBox
from Connector.ConnMain import ConnMain
from Component.Table.TableInquiryTimePerUser import TableInquiryTimePerUser
from Component.Table.TableInquiryTotalFinalUser import TableInquiryTotalFinalUser
from Design import Style
from pandas import ExcelWriter
from datetime import datetime


class WidgetInquiryTimePerUser(QWidget):
    def __init__(self, dock=None):
        QWidget.__init__(self)
        self.dock = dock
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connMain = ConnMain()

    def __variables__(self):
        self.years = self.connMain.ReturnTables()

    def __component__(self):
        self.__cbxYear__()
        self.__btnSearch__()
        self.__btnSave__()
        self.__cbxGroup__()
        self.__tab__()
        self.__layout__()
        self.__importTable__()

    def __cbxYear__(self):
        currentYear = str(datetime.today().year)
        self.cbxYear = QComboBox()
        self.cbxYear.setStyleSheet(Style.ComboBox_OutTable)
        self.cbxYear.addItems(self.years)
        self.cbxYear.setCurrentText(currentYear)

    def __btnSearch__(self):
        self.btnSearch = QPushButton('조회')
        self.btnSearch.setStyleSheet(Style.PushButton_Tools)
        self.btnSearch.clicked.connect(self.btnSearchClick)

    def __btnSave__(self):
        self.btnSave = QPushButton('엑셀로 저장')
        self.btnSave.setStyleSheet(Style.PushButton_Excel)
        self.btnSave.setShortcut('Ctrl+S')
        self.btnSave.clicked.connect(self.btnSaveClick)
        self.btnSave.setEnabled(False)

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption='엑셀로 내보내기', directory='', filter='*.xlsx')[0]
        if filePath != '':
            year = self.cbxYear.currentText()
            userNames = self.connMain.ReturnUserNames(year)
            with ExcelWriter(filePath) as writer:
                df = self.tab.widget(0).dfFinalTotal
                df.to_excel(writer, sheet_name=f'연도별 시간 집계', index=False)
                for idx, userName in enumerate(userNames):
                    df = self.tab.widget(idx + 1).dfTotal
                    df.to_excel(writer, sheet_name=f'{userName}', index=False)
                writer.close()

    def __importTable__(self):
        year = self.cbxYear.currentText()
        userNames = self.connMain.ReturnUserNames(year)
        userName = userNames.pop(0)
        tblTimeUser = TableInquiryTimePerUser(year, userName, self)
        self.tab.addTab(tblTimeUser, userName)
        dfTotal = tblTimeUser.dfTotal
        columnsTotal = list(dfTotal.keys())
        businessNames = dfTotal['사업명']
        dfFinalTotal = tblTimeUser.dfTotal
        for userName in userNames:
            tblTimeUser = TableInquiryTimePerUser(year, userName, self)
            self.tab.addTab(tblTimeUser, userName)
            dfFinalTotal += tblTimeUser.dfTotal
        dfFinalTotal['사업명'] = businessNames
        self.tab.insertTab(0, TableInquiryTotalFinalUser(columnsTotal, dfFinalTotal, self), '전체')
        self.tab.setCurrentIndex(0)
        self.btnSave.setEnabled(True)

    def btnSearchClick(self):
        self.tab.clear()
        year = self.cbxYear.currentText()
        userNames = self.connMain.ReturnUserNames(year)
        userName = userNames.pop(0)
        tblTimeUser = TableInquiryTimePerUser(year, userName, self)
        self.tab.addTab(tblTimeUser, userName)
        dfTotal = tblTimeUser.dfTotal
        columnsTotal = list(dfTotal.keys())
        businessNames = dfTotal['사업명']
        dfFinalTotal = tblTimeUser.dfTotal
        for userName in userNames:
            tblTimeUser = TableInquiryTimePerUser(year, userName, self)
            self.tab.addTab(tblTimeUser, userName)
            dfFinalTotal += tblTimeUser.dfTotal
        dfFinalTotal['사업명'] = businessNames
        self.tab.insertTab(0, TableInquiryTotalFinalUser(columnsTotal, dfFinalTotal, self), '전체')
        self.tab.setCurrentIndex(0)
        self.btnSave.setEnabled(True)

    def __cbxGroup__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.cbxYear)
        layout.addWidget(self.btnSearch)
        layout.addWidget(self.btnSave)
        layout.addWidget(QLabel(''), 10)
        self.cbxGroup = QGroupBox()
        self.cbxGroup.setLayout(layout)

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.cbxGroup)
        layout.addWidget(self.tab)
        self.setLayout(layout)
