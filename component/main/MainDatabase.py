from PyQt5.QtWidgets import *
from material import GeneralComboBox
from component.table.TableDBUser import TableDBUser
from component.table.TableDBBusiness import TableDBBusiness
from component.dialog.DialogMassage import DialogMassage
from method.dbList import returnMainList
from connector.connDB import connDB


class MainDatabase(QGroupBox):
    def __init__(self, window):
        QGroupBox.__init__(self)
        self.window = window
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        pass

    def __variables__(self):
        pass

    def __component__(self):
        self.__label__()
        self.__pushButton__()
        self.__comboBox__()
        self.__table__()
        self.__layout__()

    def __label__(self):
        self.lblUser = QLabel('부서원 목록')
        self.lblBusiness = QLabel('사업 목록')

    def __pushButton__(self):
        def btnCreateClick():
            dig = DialogMassage(f'{int(self.cbxYear.currentText())+1}년 데이터베이스를 생성하시겠습니까?', question=True)
            if dig.value:
                conn = connDB(self.cbxYear.currentText())
                conn.createDB()
                DialogMassage('데이터베이스 생성이 완료되었습니다.')
                self.window.refreshAdminDB()
        self.btnCreate = QPushButton('다음 연도 생성')
        self.btnCreate.clicked.connect(btnCreateClick)

        def btnSaveClick():
            pass
        self.btnSave = QPushButton('저장')
        self.btnSave.clicked.connect(btnSaveClick)

        def btnExcelClick():
            pass
        self.btnExcel = QPushButton('엑셀로 저장')
        self.btnExcel.clicked.connect(btnExcelClick)

    def __comboBox__(self):
        def cbxYearChange(text):
            self.window.DB_YEAR = text
            self.window.refreshAdminDB()
        self.cbxYear = GeneralComboBox(returnMainList())
        self.cbxYear.setCurrentText(self.window.DB_YEAR)
        self.cbxYear.currentTextChanged.connect(cbxYearChange)

    def __table__(self):
        try:
            self.tblUser = TableDBUser(self.window.DB_YEAR)
            self.tblBusiness = TableDBBusiness(self.window.DB_YEAR)
        except:
            self.tblUser = QTableWidgetItem()
            self.tblBusiness = QTableWidget()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.cbxYear)
        layoutBtn.addWidget(self.btnCreate)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(''), 10)
        layoutTblUser = QVBoxLayout()
        layoutTblUser.addWidget(self.lblUser)
        layoutTblUser.addWidget(self.tblUser)
        layoutTblBusiness = QVBoxLayout()
        layoutTblBusiness.addWidget(self.lblBusiness)
        layoutTblBusiness.addWidget(self.tblBusiness)
        layoutTbl = QHBoxLayout()
        layoutTbl.addLayout(layoutTblUser)
        layoutTbl.addLayout(layoutTblBusiness)
        layoutTbl.addWidget(QLabel(''), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addLayout(layoutTbl)
        self.setLayout(layout)
