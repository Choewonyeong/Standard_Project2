from PyQt5.QtWidgets import *
from method.totalList import returnTotalPerUser
import setting
from os import listdir
from component.table.TableTotalPerUser import TableTotalPerUser


class MainTotalPerUser(QGroupBox):
    def __init__(self, windows):
        QGroupBox.__init__(self)
        self.windows = windows
        self.__component__()

    def __component__(self):
        self.__comboBox__()
        self.__variables__()
        self.__table__()
        self.__tab__()
        self.__layout__()

    def __comboBox__(self):
        years = listdir(setting.databaseMain)
        years = [year.replace('.db', '') for year in years]

        def cbxYearChange(text):
            self.windows.TOTAL_YEAR = text
            self.windows.refreshTotalPerUser()
        self.cbxYear = QComboBox()
        self.cbxYear.addItems(years)
        self.cbxYear.setCurrentText(self.windows.TOTAL_YEAR)
        self.cbxYear.currentTextChanged.connect(cbxYearChange)

    def __variables__(self):
        self.columns = returnTotalPerUser(self.windows.TOTAL_YEAR, column=True)
        self.totalDict = returnTotalPerUser(self.windows.TOTAL_YEAR)

    def __table__(self):
        self.objectTable = []
        for userName in self.totalDict.keys():
            self.objectTable.append(TableTotalPerUser(self.windows.TOTAL_YEAR, userName,
                                                      self.columns, self.totalDict[userName]))

    def __tab__(self):
        self.tab = QTabWidget()
        self.tab.addTab(self.objectTable[-1], self.objectTable[-1].userName)
        self.objectTable.pop()
        for table in self.objectTable:
            self.tab.addTab(table, table.userName)

    def __layout__(self):
        layoutTop = QHBoxLayout()
        layoutTop.addWidget(self.cbxYear)
        layoutTop.addWidget(QLabel(''), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutTop)
        layout.addWidget(self.tab)
        self.setLayout(layout)
