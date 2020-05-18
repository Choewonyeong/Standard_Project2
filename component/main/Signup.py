from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from setting import variables


class Signup(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        pass

    def __component__(self):
        self.__label__()
        self.__lineEdit__()
        self.__comboBox__()
        self.__radioButton__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        self.lblName = QLabel('성    명*')
        self.lblAccount = QLabel('계   정*')
        self.lblPassword = QLabel('비밀번호*')
        self.lblPasswordConfirm = QLabel('비밀번호 확인*')
        self.lblIdentity = QLabel('주민등록번호*')
        self.lblPhone = QLabel('연 락 처*')
        self.lblDegree = QLabel('학    력')
        self.lblSchool = QLabel('학    교')
        self.lblMajor = QLabel('전    공')
        self.lblCar = QLabel('차량소지여부')
        self.lblCarType = QLabel('차    종')
        self.lblCarType.setVisible(False)
        self.lblCarNumber = QLabel('차량번호')
        self.lblCarNumber.setVisible(False)

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
        self.ldtCarType.setVisible(False)
        self.ldtCarNumber = QLineEdit()
        self.ldtCarNumber.setVisible(False)
        self.ldtMajor = QLineEdit()

    def __comboBox__(self):
        self.cbxDegree = QComboBox()
        self.cbxDegree.addItems(variables.itemUserDegree)
        self.cbxDegree.setCurrentText(variables.setUserDegree)
        self.cbxDegree.setCursor(Qt.PointingHandCursor)

    def __radioButton__(self):
        self.rbtCarTrue = QRadioButton('유')
        self.rbtCarTrue.clicked.connect(self.rbtCarTrueClick)
        self.rbtCarFalse = QRadioButton('무')
        self.rbtCarFalse.clicked.connect(self.rbtCarFalseClick)
        self.rbtCarFalse.setChecked(True)
        layoutRbt = QHBoxLayout()
        layoutRbt.addWidget(self.rbtCarTrue)
        layoutRbt.addWidget(self.rbtCarFalse)
        self.gbxRadioButton = QGroupBox()
        self.gbxRadioButton.setLayout(layoutRbt)

    def rbtCarTrueClick(self):
        self.lblCarType.setVisible(True)
        self.lblCarNumber.setVisible(True)
        self.ldtCarType.setVisible(True)
        self.ldtCarNumber.setVisible(True)

    def rbtCarFalseClick(self):
        self.ldtCarType.setText('')
        self.ldtCarNumber.setText('')
        self.lblCarType.setVisible(False)
        self.lblCarNumber.setVisible(False)
        self.ldtCarType.setVisible(False)
        self.ldtCarNumber.setVisible(False)

    def __pushButton__(self):
        self.btnClose = QPushButton('닫기')
        self.btnClose.setCursor(Qt.PointingHandCursor)
        self.btnClose.clicked.connect(self.btnCloseClick)
        self.btnSignup = QPushButton('신청')
        self.btnSignup.setCursor(Qt.PointingHandCursor)
        self.btnSignup.clicked.connect(self.btnSignupClick)

    def btnCloseClick(self):
        self.close()

    def btnSignupClick(self):
        userInfo = [self.ldtName.text(),
                    self.ldtAccount.text(),
                    self.ldtPassword.text(),
                    self.ldtIdentity.text(),
                    self.ldtPhone.text(),
                    self.cbxDegree.currentText(),
                    self.ldtSchool.text(),
                    self.ldtMajor.text(),
                    self.ldtCarType.text(),
                    self.ldtCarNumber.text()]
        if userInfo[0] == '':
            print('이름 입력 하시오')
        elif userInfo[1] == '':
            print('계정을 입력하시오.')
        elif userInfo[2] == '':
            print('비밀번호를 입력하시오.')
        elif len(userInfo[2]) < 4:
            print('비밀번호는 4자리 이상입니다.')
        elif userInfo[2] != self.ldtPasswordConfirm.text():
            print('비밀번호가 맞지 않습니다.')
        elif userInfo[3] == '':
            print('주민등록번호를 입력하시오.')
        elif userInfo[4] == '':
            print('연락처를 입력하세요')

    def __layout__(self):
        widgets = [self.ldtName,
                   self.ldtAccount,
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
        titles = [self.lblName,
                  self.lblAccount,
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

