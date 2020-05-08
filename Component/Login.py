from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QFormLayout
from Setting import Path
from Connector.ConnUser import ConnUser
from Component.Windows import Windows
from Design import Style


class Login(QWidget):
    def __init__(self, app):
        QWidget.__init__(self)
        self.app = app
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setStyleSheet(Style.Login_Dialog)
        self.setWindowTitle('로그인')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(Path.icon))
        self.setFixedHeight(600)
        self.setFixedWidth(400)

    def __connector__(self):
        self.connUser = ConnUser()

    def __variables__(self):
        self.userName = ''
        self.author = ''
        self.userNames = self.connUser.ReturnUserNames()

    def __component__(self):
        self.__img__()
        self.__cautions__()
        self.__userName__()
        self.__passWord__()
        self.__buttons__()
        self.__layout__()

    def __cautions__(self):
        self.noUserName = QLabel('성명을 입력하세요.')
        self.noUserName.setStyleSheet(Style.Label_Caution)
        self.noUserName.setAlignment(Qt.AlignCenter)
        self.noUserName.setVisible(False)
        self.noPassWord = QLabel('비밀번호를 입력하세요.')
        self.noPassWord.setStyleSheet(Style.Label_Caution)
        self.noPassWord.setAlignment(Qt.AlignCenter)
        self.noPassWord.setVisible(False)

    def __img__(self):
        self.img = QLabel()
        self.img.setPixmap(QPixmap(Path.login).scaledToWidth(125))
        self.img.setAlignment(Qt.AlignCenter)
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap(Path.logo).scaledToWidth(200))
        self.logo.setAlignment(Qt.AlignCenter)

    def __userName__(self):
        self.lineUserName = QLineEdit()
        self.lineUserName.setMouseTracking(False)
        self.lineUserName.setPlaceholderText('UserName')
        self.lineUserName.setAlignment(Qt.AlignCenter)
        self.lineUserName.textChanged.connect(self.HideCautionUserName)

    def __passWord__(self):
        self.linePassWord = QLineEdit()
        self.linePassWord.setMouseTracking(False)
        self.linePassWord.setPlaceholderText('Password')
        self.linePassWord.setEchoMode(QLineEdit.Password)
        self.linePassWord.setAlignment(Qt.AlignCenter)
        self.linePassWord.textChanged.connect(self.HideCautionPassWord)

    def HideCautionUserName(self, text):
        if text != '':
            self.noUserName.setVisible(False)

    def HideCautionPassWord(self, text):
        if text != '':
            self.noPassWord.setVisible(False)

    def __buttons__(self):
        btnClose = QPushButton()
        btnClose.setText('닫기')
        btnClose.setStyleSheet(Style.PushButton_Close)
        btnClose.clicked.connect(self.close)
        btnLogin = QPushButton()
        btnLogin.setText('로그인')
        btnLogin.setShortcut('Return')
        btnLogin.setStyleSheet(Style.PushButton_Tools)
        btnLogin.clicked.connect(self.btnLoginClicked)
        btnLogin.setDefault(True)
        self.layoutBtn = QHBoxLayout()
        self.layoutBtn.addWidget(btnClose)
        self.layoutBtn.addWidget(QLabel('    '))
        self.layoutBtn.addWidget(btnLogin)

    def __layout__(self):
        layoutHorizonCenter = QFormLayout()
        layoutHorizonCenter.addWidget(self.img)
        layoutHorizonCenter.addRow('', self.lineUserName)
        layoutHorizonCenter.addRow('', self.noUserName)
        layoutHorizonCenter.addRow('', self.linePassWord)
        layoutHorizonCenter.addRow('', self.noPassWord)
        layoutHorizonCenter.addItem(self.layoutBtn)
        layoutHorizon = QHBoxLayout()
        layoutHorizon.addWidget(QLabel(), 3)
        layoutHorizon.addLayout(layoutHorizonCenter, 0)
        layoutHorizon.addWidget(QLabel(), 3)
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(QLabel(), 3)
        layoutVertical.addLayout(layoutHorizon, 0)
        layoutVertical.addWidget(QLabel(), 3)
        layoutVertical.addWidget(self.logo)
        layoutVertical.addWidget(QLabel())
        self.setLayout(layoutVertical)

    def CheckLineUserName(self):
        self.userName = self.lineUserName.text()
        if self.userName == '':
            self.noUserName.setVisible(True)
        elif self.userName not in self.userNames:
            self.noUserName.setText('등록되지 않은 계정입니다.')
            self.noUserName.setVisible(True)

    def CheckLinePassWord(self):
        passWord = self.linePassWord.text()
        userPassWord = self.connUser.ReturnUserPassWord(self.userName)
        if passWord == '':
            self.noPassWord.setVisible(True)
        elif passWord != userPassWord:
            self.noPassWord.setText('비밀번호가 맞지 않습니다.')
            self.noPassWord.setVisible(True)

    def btnLoginClicked(self):
        self.userName = self.lineUserName.text()
        passWord = self.linePassWord.text()
        userPassWord = self.connUser.ReturnUserPassWord(self.userName)
        if self.userName == '':
            self.noUserName.setVisible(True)
        elif self.userName not in self.userNames:
            self.noUserName.setText('등록되지 않은 계정입니다.')
            self.noUserName.setVisible(True)
        elif passWord == '':
            self.noPassWord.setVisible(True)
        elif passWord != userPassWord:
            self.noPassWord.setText('비밀번호가 맞지 않습니다.')
            self.noPassWord.setVisible(True)
        else:
            self.lineUserName.setText('')
            self.linePassWord.setText('')
            self.author = self.connUser.ReturnUserAuthor(self.userName)
            windows = Windows(self.userName, self.author)
            windows.show()
            self.close()



