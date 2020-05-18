from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from connector.connUser import connUser
import setting


class Login(QDialog):
    def __init__(self, app):
        QDialog.__init__(self)
        self.app = app
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(400)
        self.setFixedHeight(600)

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.userId = ''
        self.author = ''
        self.userIds = self.connUser.returnAccounts()

    def __component__(self):
        self.__label__()
        self.__lineEdit__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        self.lblImg = QLabel()
        self.lblImg.setPixmap(QPixmap(setting.imgLogin).scaledToWidth(125))
        self.lblImg.setAlignment(Qt.AlignCenter)
        self.lblLogo = QLabel()
        self.lblLogo.setPixmap(QPixmap(setting.imgLogo).scaledToWidth(200))
        self.lblLogo.setAlignment(Qt.AlignCenter)

    def __lineEdit__(self):
        self.ldtAccount = QLineEdit()
        self.ldtAccount.setMouseTracking(False)
        self.ldtAccount.setPlaceholderText('Account')
        self.ldtAccount.setAlignment(Qt.AlignCenter)
        self.ldtPassword = QLineEdit()
        self.ldtPassword.setMouseTracking(False)
        self.ldtPassword.setPlaceholderText('Password')
        self.ldtPassword.setEchoMode(QLineEdit.Password)
        self.ldtPassword.setAlignment(Qt.AlignCenter)

    def __pushButton__(self):
        self.btnClose = QPushButton('닫기')
        self.btnClose.setCursor(Qt.PointingHandCursor)
        self.btnClose.clicked.connect(self.btnCloseClick)
        self.btnLogin = QPushButton('로그인')
        self.btnLogin.setCursor(Qt.PointingHandCursor)
        self.btnLogin.setShortcut('return')
        self.btnLogin.setDefault(True)
        self.btnLogin.clicked.connect(self.btnLoginClick)
        self.btnSignup = QPushButton('회원가입')
        self.btnSignup.setCursor(Qt.PointingHandCursor)
        self.btnSignup.clicked.connect(self.btnSignupClick)

    def btnCloseClick(self):
        self.app.quit()

    def btnLoginClick(self):
        account = self.ldtAccount.text()
        password = self.ldtPassword.text()
        if account == '':
            print('Error 1')     # 계정 입력
        elif password == '': 
            print('Error 2')     # 비밀번호 입력
        elif password != self.connUser.returnPassword(account):
            print('Error 3')     # 비밀번호 불일치
        else:
            from component.main.Windows import Windows
            author = self.connUser.returnAuthor(account)
            window = Windows(account, author)
            window.show()
            self.close()
            self.app.exec_()

    def btnSignupClick(self):
        from component.main.Signup import Signup
        signup = Signup()
        signup.exec_()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnLogin)
        layout = QVBoxLayout()
        layout.addWidget(self.ldtAccount)
        layout.addWidget(self.ldtPassword)
        layout.addLayout(layoutBtn)
        layout.addWidget(self.btnSignup)
        self.setLayout(layout)
