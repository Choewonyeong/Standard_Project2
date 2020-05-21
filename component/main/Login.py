from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from connector.connUser import connUser
from component.dialog.DialogMassage import DialogMassage
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
        self.account = ''
        self.author = ''
        self.accounts = self.connUser.returnAccounts()

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
        def btnCloseClick():
            self.app.quit()

        def btnLoginClick():
            account = self.ldtAccount.text()
            password = self.ldtPassword.text()
            if account == '':
                DialogMassage('계정을 입력하세요.')
            elif account not in self.accounts:
                DialogMassage('등록되지 않은 계정입니다.')
            elif password == '':
                DialogMassage('비밀번호를 입력하세요.')
            elif password != self.connUser.returnPassword(account):
                DialogMassage('비밀번호가 일치하지 않습니다.')
                self.ldtPassword.setText('')
            else:
                try:
                    from component.main.Windows import Windows
                    author = self.connUser.returnAuthor(account)
                    window = Windows(account, author, self.app)
                    window.show()
                    self.close()
                    self.app.exec_()
                except Exception as e:
                    print(e)

        def btnSignupClick():
            from component.dialog.DialogSignup import Signup
            signup = Signup()
            signup.exec_()

        self.btnClose = QPushButton('닫기')
        self.btnClose.setCursor(Qt.PointingHandCursor)
        self.btnClose.clicked.connect(btnCloseClick)
        self.btnLogin = QPushButton('로그인')
        self.btnLogin.setCursor(Qt.PointingHandCursor)
        self.btnLogin.setShortcut('return')
        self.btnLogin.setDefault(True)
        self.btnLogin.clicked.connect(btnLoginClick)
        self.btnSignup = QPushButton('회원가입')
        self.btnSignup.setCursor(Qt.PointingHandCursor)
        self.btnSignup.clicked.connect(btnSignupClick)

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
