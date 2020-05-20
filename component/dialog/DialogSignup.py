from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting import variables
from connector.connUser import connUser
from component.dialog.DialogMassage import DialogMassage


class Signup(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(250)

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.accounts = self.connUser.returnAccounts()

    def __component__(self):
        self.__label__()
        self.__lineEdit__()
        self.__comboBox__()
        self.__radioButton__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        self.lblAccount = QLabel('계정')
        self.lblName = QLabel('성명')
        self.lblPassword = QLabel('비밀번호   ')
        self.lblPasswordConfirm = QLabel('비밀번호 확인')
        self.lblIdentity = QLabel('주민등록번호')
        self.lblPhone = QLabel('연락처')
        self.lblDegree = QLabel('학력')
        self.lblSchool = QLabel('학교')
        self.lblMajor = QLabel('전공')
        self.lblCar = QLabel('차량소지여부')
        self.lblCarType = QLabel('차종')
        self.lblCarNumber = QLabel('차량번호')

    def __lineEdit__(self):
        self.ldtAccount = QLineEdit()
        self.ldtName = QLineEdit()
        self.ldtPassword = QLineEdit()
        self.ldtPassword.setEchoMode(QLineEdit.Password)
        self.ldtPasswordConfirm = QLineEdit()
        self.ldtPasswordConfirm.setEchoMode(QLineEdit.Password)
        self.ldtIdentity = QLineEdit()
        self.ldtIdentity.setPlaceholderText('ex) 950302-1')
        self.ldtIdentity.setMaxLength(8)
        self.ldtPhone = QLineEdit()
        self.ldtPhone.setPlaceholderText('ex) 010-3351-6137')
        self.ldtPhone.setMaxLength(13)
        self.ldtSchool = QLineEdit()
        self.ldtCarType = QLineEdit()
        self.ldtCarNumber = QLineEdit()
        self.ldtMajor = QLineEdit()

    def __comboBox__(self):
        self.cbxDegree = QComboBox()
        self.cbxDegree.addItems(variables.itemUserDegree)
        self.cbxDegree.setCurrentText(variables.setUserDegree)
        self.cbxDegree.setCursor(Qt.PointingHandCursor)

    def __radioButton__(self):
        def rbtCarTrueClick():
            self.lblCarType.setVisible(True)
            self.lblCarNumber.setVisible(True)
            self.ldtCarType.setVisible(True)
            self.ldtCarNumber.setVisible(True)

        def rbtCarFalseClick():
            self.ldtCarType.setText('')
            self.ldtCarNumber.setText('')
            self.lblCarType.setVisible(False)
            self.lblCarNumber.setVisible(False)
            self.ldtCarType.setVisible(False)
            self.ldtCarNumber.setVisible(False)

        self.rbtCarTrue = QRadioButton('유')
        self.rbtCarTrue.clicked.connect(rbtCarTrueClick)
        self.rbtCarTrue.setChecked(True)
        self.rbtCarFalse = QRadioButton('무')
        self.rbtCarFalse.clicked.connect(rbtCarFalseClick)
        layoutRbt = QHBoxLayout()
        layoutRbt.addWidget(self.rbtCarTrue)
        layoutRbt.addWidget(self.rbtCarFalse)
        self.gbxRadioButton = QGroupBox()
        self.gbxRadioButton.setLayout(layoutRbt)

    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('닫기')
        self.btnClose.setCursor(Qt.PointingHandCursor)
        self.btnClose.clicked.connect(btnCloseClick)

        def btnSignupClick():
            userInfo = [self.ldtAccount.text(),
                        self.ldtName.text(),
                        self.ldtPassword.text(),
                        self.ldtIdentity.text(),
                        self.ldtPhone.text(),
                        self.cbxDegree.currentText(),
                        self.ldtSchool.text(),
                        self.ldtMajor.text(),
                        self.ldtCarType.text(),
                        self.ldtCarNumber.text()]
            if userInfo[0] == '':
                DialogMassage('계정을 입력하세요.')
            elif userInfo[0] in self.accounts:
                DialogMassage('이미 존재하는 계정입니다.')
            elif userInfo[1] == '':
                DialogMassage('성명을 입력하세요.')
            elif userInfo[2] == '':
                DialogMassage('비밀번호를 입력하세요.')
            elif len(userInfo[2]) < 4:
                DialogMassage('비밀번호는 4자리 이상으로 입력하세요.')
            elif userInfo[2] != self.ldtPasswordConfirm.text():
                DialogMassage('비밀번호가 일치하지 않습니다.')
            elif userInfo[3] == '':
                DialogMassage('주민등록번호를 입력하세요.')
            elif userInfo[4] == '':
                DialogMassage('연락처를 입력하세요.')
            else:
                self.connUser.insertNewUser(userInfo)
                admins = self.connUser.returnAdmins()
                DialogMassage(f"회원가입 신청이 완료되었습니다.\n관리자에게 승인을 요청하세요.\n관리자 : {', '.join(admins)}")
        self.btnSignup = QPushButton('신청')
        self.btnSignup.setDefault(True)
        self.btnSignup.setCursor(Qt.PointingHandCursor)
        self.btnSignup.clicked.connect(btnSignupClick)

    def __layout__(self):
        widgets = [self.ldtAccount,
                   self.ldtName,
                   self.ldtPassword,
                   self.ldtPasswordConfirm,
                   self.ldtIdentity,
                   self.ldtPhone,
                   self.cbxDegree,
                   self.ldtSchool,
                   self.ldtMajor,
                   self.gbxRadioButton,
                   self.ldtCarType,
                   self.ldtCarNumber]
        titles = [self.lblAccount,
                  self.lblName,
                  self.lblPassword,
                  self.lblPasswordConfirm,
                  self.lblIdentity,
                  self.lblPhone,
                  self.lblDegree,
                  self.lblMajor,
                  self.lblSchool,
                  self.lblCar,
                  self.lblCarType,
                  self.lblCarNumber]
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnSignup)
        layoutWidget = QFormLayout()
        for title, widget in zip(titles, widgets):
            layoutZip = QHBoxLayout()
            layoutZip.addWidget(title, 1)
            layoutZip.addWidget(widget, 2)
            layoutWidget.addItem(layoutZip)
        layout = QVBoxLayout()
        layout.addLayout(layoutWidget)
        layout.addLayout(layoutBtn)
        self.setLayout(layout)

