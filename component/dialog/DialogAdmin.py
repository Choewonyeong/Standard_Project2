from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from material.GeneralLineEdit import GeneralLineEdit
from material.GeneralLabel import GeneralLabel
from component.dialog.DialogPassword import DialogPassword
from component.dialog.DialogMassage import DialogMassage


class DialogAdmin(QDialog):
    def __init__(self, account, row, table):
        QDialog.__init__(self)
        self.account = account
        self.row = row
        self.table = table
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()
        self.exec_()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.password = ''
        self.adminPasswords = self.connUser.returnAdminPassword()

    def __component__(self):
        self.__label__()
        self.__lineEdit__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        self.lblPassword = GeneralLabel('관리자의 권한이 필요합니다.\n비밀번호를 입력하세요.')

    def __lineEdit__(self):
        self.ldtPassword = GeneralLineEdit()
        self.ldtPassword.setEchoMode(QLineEdit.Password)

    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('닫기')
        self.btnClose.clicked.connect(btnCloseClick)

        def btnConfirmClick():
            password = self.ldtPassword.text()
            if password in self.adminPasswords:
                userName = self.connUser.returnName(self.account)
                userPassword = self.connUser.returnPassword(self.account)
                self.close()
                DialogPassword(userName, self.account, userPassword, self.row, self.table)
            else:
                DialogMassage('비밀번호가 맞지 않습니다.')
        self.btnConfirm = QPushButton('확인')
        self.btnConfirm.clicked.connect(btnConfirmClick)
        self.btnConfirm.setShortcut('return')

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnConfirm)
        layout = QVBoxLayout()
        layout.addWidget(self.lblPassword)
        layout.addWidget(self.ldtPassword)
        layout.addLayout(layoutBtn)
        self.setLayout(layout)
