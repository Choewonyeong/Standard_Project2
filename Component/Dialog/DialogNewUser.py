from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from Connector.ConnUser import ConnUser
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Setting import Path
from Design import Style
from datetime import datetime


class DialogNewUser(QDialog):
    def __init__(self, userNumber, dock=None):
        QDialog.__init__(self)
        self.userNumber = userNumber
        self.dock = dock
        self.__setting__()
        self.__variables__()
        self.__connector__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(Path.icon))
        self.setWindowTitle('신규 회원 등록')
        self.setStyleSheet(Style.Components_Dialog)
        self.setFixedWidth(360)

    def __variables__(self):
        self.objText = ['성명',
                        '입사일',
                        '소속',
                        '직위',
                        '비밀번호',
                        '주민등록번호',
                        '연락처',
                        '차종',
                        '차량번호',
                        '대학',
                        '전공',
                        '학위',
                        '과학기술인등록번호',
                        '재직상태',
                        '접근권한']

    def __connector__(self):
        self.connUser = ConnUser()

    def __component__(self):
        self.__lineEdit__()
        self.__button__()
        self.__layout__()

    def __lineEdit__(self):
        self.inputUserName = QLineEdit()

        self.inputIncome = QLineEdit()
        self.inputIncome.setMaxLength(10)
        self.inputIncome.editingFinished.connect(self.lineEditIncomeEditFinish)
        self.inputIncome.setPlaceholderText('ex) 2019-06-10')
        self.inputTeam = QLineEdit('화재안전팀')
        self.inputPosition = QComboBox()
        self.inputPosition.addItems(['이사', '부장', '차장', '과장', '대리',
                                     '사원', '신입'])
        self.inputPosition.setCurrentText('신입')
        self.inputPassword = QLineEdit()
        self.inputPassword.setEchoMode(QLineEdit.Password)
        self.inputIdentity = QLineEdit()
        self.inputIdentity.setPlaceholderText('ex) 950302-1')
        self.inputIdentity.setMaxLength(8)
        self.inputIdentity.textChanged.connect(self.lineEditIdentityChange)
        self.inputPhone = QLineEdit()
        self.inputPhone.setPlaceholderText('ex) 010-3351-6137')
        self.inputPhone.setMaxLength(13)
        self.inputPhone.textChanged.connect(self.lineEditPhoneChange)
        self.inputCar = QLineEdit()
        self.inputCarNumber = QLineEdit()
        self.inputUniversity = QLineEdit()
        self.inputMajor = QLineEdit()
        self.inputDegree = QComboBox()
        self.inputDegree.addItems(['고졸', '전문대졸', '학사', '석사', '박사'])
        self.inputDegree.setCurrentText('학사')
        self.inputScienceNumber = QLineEdit()
        self.inputStatus = QComboBox()
        self.inputStatus.addItems(['재직', '파견', '휴직', '정직', '퇴직'])
        self.inputAuthor = QComboBox()
        self.inputAuthor.addItems(['사용자', '관리자'])
        self.objects = [self.inputUserName,
                        self.inputIncome,
                        self.inputTeam,
                        self.inputPosition,
                        self.inputPassword,
                        self.inputIdentity,
                        self.inputPhone,
                        self.inputCar,
                        self.inputCarNumber,
                        self.inputUniversity,
                        self.inputMajor,
                        self.inputDegree,
                        self.inputScienceNumber,
                        self.inputStatus,
                        self.inputAuthor]

    def lineEditIncomeEditFinish(self):
        text = self.inputIncome.text()
        try:
            date = datetime.strptime(text, '%Y-%m-%d').strftime('%Y-%m-%d')
            self.inputIncome.setText(date)
        except:
            pass

    def lineEditIdentityChange(self, text):
        if len(text) == 6:
            self.inputIdentity.setText(text+"-")

    def lineEditPhoneChange(self, text):
        if len(text) == 3:
            self.inputPhone.setText(text+"-")
        elif len(text) == 8:
            self.inputPhone.setText(text+"-")

    def __button__(self):
        self.btnClose = QPushButton('닫기')
        self.btnInsert = QPushButton('입력')
        self.btnClose.setStyleSheet(Style.PushButton_Close)
        self.btnInsert.setStyleSheet(Style.PushButton_Tools)
        self.btnInsert.setDefault(True)
        self.btnClose.clicked.connect(self.close)
        self.btnInsert.clicked.connect(self.btnInsertClick)

    def btnInsertClick(self):
        if not self.inputUserName.text():
            dig = DialogMessageBox('', '비밀번호를 입력하세요.')
            dig.exec_()
        elif len(self.inputPassword.text()) < 4:
            dig = DialogMessageBox('', '비밀번호는 4자 이상입니다.')
            dig.exec_()
        elif not self.inputIdentity.text():
            dig = DialogMessageBox('', '주민등록번호를 입력하세요.')
            dig.exec_()
        elif len(self.inputIdentity.text()) < 8:
            dig = DialogMessageBox('', '주민등록번호를 확인하세요.')
            dig.exec_()
        else:
            userData = [self.userNumber,
                        self.inputUserName.text(),
                        self.inputIncome.text(),
                        self.inputTeam.text(),
                        self.inputPosition.currentText(),
                        self.inputPassword.text(),
                        self.inputIdentity.text(),
                        self.inputPhone.text(),
                        self.inputCar.text(),
                        self.inputCarNumber.text(),
                        self.inputUniversity.text(),
                        self.inputMajor.text(),
                        self.inputDegree.currentText(),
                        self.inputScienceNumber.text(),
                        self.inputStatus.currentText(),
                        self.inputAuthor.currentText()]
            self.connUser.InsertUser(userData)
            self.dock.refresh()
            for idx, obj in enumerate(self.objects):
                if idx not in [3, 11, 13, 14]:
                    obj.setText('')
            self.inputPosition.setCurrentText('신입')
            self.inputDegree.setCurrentText('학사')
            self.inputStatus.setCurrentText('재직')
            self.inputAuthor.setCurrentText('사용자')

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(QLabel(''), 10)
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInsert)
        layoutBtn.addWidget(QLabel(''), 10)
        layoutInput = QFormLayout()
        for text, obj in zip(self.objText, self.objects):
            layoutInput.addRow(text, obj)
        layout = QVBoxLayout()
        layout.addLayout(layoutInput)
        layout.addWidget(QLabel(''))
        layout.addLayout(layoutBtn)
        self.setLayout(layout)
