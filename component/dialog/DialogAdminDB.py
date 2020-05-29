from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from component.material.GeneralComboBox import GeneralComboBox
from component.table.TableDBUser import TableDBUser
from component.table.TableDBBusiness import TableDBBusiness
from method.dbList import returnMainList


class DialogAdminDB(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        pass

    def __component__(self):
        self.__pushButton__()
        self.__comboBox__()
        self.__table__()
        self.__layout__()

    def __pushButton__(self):
        self.btnClose = QPushButton('닫기')
        self.btnSave = QPushButton('저장')
        self.btnExcel = QPushButton('엑셀로 저장')

    def __comboBox__(self):
        def cbxYearChange(text):
            self.year = text
            self.close()
            self.exec_()
        self.cbxYear = GeneralComboBox(returnMainList())
        self.cbxYear.currentTextChanged.connect(cbxYearChange)
        self.year = self.cbxYear.currentText()

    def __table__(self):
        try:
            self.tblUser = TableDBUser(self.year)
            self.tblBusiness = TableDBBusiness(self.year)
        except Exception as e:
            print(e)

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.cbxYear)
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(''), 10)
        layoutTbl = QHBoxLayout()
        layoutTbl.addWidget(self.tblUser)
        layoutTbl.addWidget(self.tblBusiness)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addLayout(layoutTbl)
        self.setLayout(layout)
