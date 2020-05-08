from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtCore import Qt
from Connector.ConnUser import ConnUser
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Design import Style


class DialogUserSelf(QDialog):
    def __init__(self, userName, windows=None):
        QDialog.__init__(self)
        self.userName = userName
        self.windows=windows
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setStyleSheet(Style.Components_Dialog)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(360)
    
    def __connector__(self):
        self.connUser = ConnUser()

    def __variables__(self):
        self.columnUser, self.listSelf = self.connUser.ColumnAndListSelf(self.userName)
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
                        '수정한날짜']

    def __component__(self):
        self.__lineEdit__()
        self.__button__()
        self.__layout__()

    def __lineEdit__(self):
        self.lineEditName = QLineEdit(self.listSelf[0])
        self.lineEditName.setEnabled(False)
        self.lineEditIncome = QLineEdit(self.listSelf[1])
        self.lineEditIncome.setEnabled(False)
        self.lineEditTeam = QLineEdit(self.listSelf[2])
        self.lineEditTeam.setEnabled(False)
        self.lineEditPosition = QLineEdit(self.listSelf[3])
        self.lineEditPosition.setEnabled(False)
        self.lineEditPassword = QLineEdit(self.listSelf[4])
        self.lineEditPassword.setEchoMode(QLineEdit.Password)
        self.lineEditIdentity = QLineEdit(self.listSelf[5])
        self.lineEditIdentity.textEdited.connect(self.IdentityChange)
        self.lineEditIdentity.setMaxLength(8)
        self.lineEditPhone = QLineEdit(self.listSelf[6])
        self.lineEditCar = QLineEdit(self.listSelf[7])
        self.lineEditCarNumber = QLineEdit(self.listSelf[8])
        self.lineEditUniversity = QLineEdit(self.listSelf[9])
        self.lineEditMajor = QLineEdit(self.listSelf[10])
        self.comboBoxDegree = QComboBox()
        self.comboBoxDegree.addItems(['고졸', '전문대졸', '학사', '석사', '박사'])
        self.comboBoxDegree.setCurrentText(self.listSelf[11])
        self.lineEditScienceNumber = QLineEdit(self.listSelf[12])
        self.lineEditEditData = QLineEdit(self.listSelf[13])
        self.lineEditEditData.setEnabled(False)
        self.objects = [self.lineEditName,
                        self.lineEditIncome,
                        self.lineEditTeam,
                        self.lineEditPosition,
                        self.lineEditPassword,
                        self.lineEditIdentity,
                        self.lineEditPhone,
                        self.lineEditCar,
                        self.lineEditCarNumber,
                        self.lineEditUniversity,
                        self.lineEditMajor,
                        self.comboBoxDegree,
                        self.lineEditScienceNumber,
                        self.lineEditEditData]

    def IdentityChange(self, text):
        if len(text) == 6:
            self.lineEditIdentity.setText(text+"-")

    def __button__(self):
        self.btnClose = QPushButton('닫기')
        self.btnApply = QPushButton('저장')
        self.btnClose.setStyleSheet(Style.PushButton_Close)
        self.btnApply.setStyleSheet(Style.PushButton_Tools)
        self.btnClose.clicked.connect(self.close)
        self.btnApply.clicked.connect(self.btnApplyClick)
        self.btnClose.setFixedWidth(200)
        self.btnApply.setFixedWidth(200)

    def btnApplyClick(self):
        if not self.lineEditPassword.text():
            dig = DialogMessageBox('알림', '비밀번호를 입력하세요.', False)
            dig.exec_()
        elif len(self.lineEditPassword.text()) < 4:
            dig = DialogMessageBox('알림', '비밀번호는 4자 이상입니다.', False)
            dig.exec_()
        elif not self.lineEditIdentity.text():
            dig = DialogMessageBox('알림', '주민등록번호를 입력하세요.', False)
            dig.exec_()
        elif len(self.lineEditIdentity.text()) < 8:
            dig = DialogMessageBox('알림', '주민등록번호를 확인하세요.', False)
            dig.exec_()
        else:
            userData = [self.lineEditPassword.text(),
                        self.lineEditIdentity.text(),
                        self.lineEditPhone.text(),
                        self.lineEditCar.text(),
                        self.lineEditCarNumber.text(),
                        self.lineEditUniversity.text(),
                        self.lineEditMajor.text(),
                        self.comboBoxDegree.currentText(),
                        self.lineEditScienceNumber.text()]
            self.connUser.UpdateSelf(userData, self.userName)

    def __layout__(self):
        layoutButton = QHBoxLayout()
        layoutButton.addWidget(QLabel(''), 10)
        layoutButton.addWidget(self.btnClose)
        layoutButton.addWidget(self.btnApply)
        layoutButton.addWidget(QLabel(''), 10)
        layoutLineEdit = QFormLayout()
        for text, obj in zip(self.objText, self.objects):
            layoutLineEdit.addRow(text, obj)
        layoutHorizontal = QHBoxLayout()
        layoutHorizontal.addWidget(QLabel(''), 1)
        layoutHorizontal.addLayout(layoutLineEdit)
        layoutHorizontal.addWidget(QLabel(''), 1)
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(QLabel(''), 2)
        layoutVertical.addLayout(layoutHorizontal)
        layoutVertical.addWidget(QLabel(''))
        layoutVertical.addLayout(layoutButton)
        layoutVertical.addWidget(QLabel(''), 2)
        self.setLayout(layoutVertical)
