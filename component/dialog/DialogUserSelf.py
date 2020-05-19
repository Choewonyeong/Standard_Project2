from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from component.dialog.DialogMassage import DialogMassage


class DialogUserSelf(QDialog):
    def __init__(self, account):
        QDialog.__init__(self)
        self.account = account
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.userInfo = self.connUser.returnUserInfo(self.account)
        self.textLbl = self.connUser.returnUserInfo(self.account, column=True)

    def __component__(self):
        self.__object__()
        self.__pushButton__()
        self.__layout__()

    def __object__(self):
        self.objectLabel = []
        self.objectInput = []
        for cnt, (text, info) in enumerate(zip(self.textLbl, self.userInfo)):
            lbl = QLabel(text)
            lbl.setFixedWidth(130)
            self.objectLabel.append(lbl)
            if cnt == 5:
                ldt = QComboBox()
                ldt.addItems(['박사', '석사', '학사', '전문대졸', '고졸'])
                ldt.setCurrentText(info)
            else:
                ldt = QLineEdit(info)
                ldt.setFixedWidth(160)
            self.objectInput.append(ldt)
        self.objectInput[0].setEnabled(False)
        self.objectInput[-1].setEnabled(False)
        self.objectInput[2].setEchoMode(QLineEdit.Password)

    def __pushButton__(self):
        def btnCloseClick():
            self.close()

        def btnApplyClick():
            userInfo = []
            for cnt, ldt in enumerate(self.objectInput):
                if cnt == 5:
                    userInfo.append(ldt.currentText())
                else:
                    userInfo.append(ldt.text())
            self.connUser.updateUserInfo(userInfo)
            editDate = self.connUser.returnEditDate(userInfo[0])
            self.objectInput[-1].setText(editDate)
            DialogMassage('저장되었습니다.')
        self.btnClose = QPushButton('닫기')
        self.btnClose.setFixedWidth(80)
        self.btnClose.clicked.connect(btnCloseClick)
        self.btnApply = QPushButton('저장')
        self.btnApply.setFixedWidth(80)
        self.btnApply.clicked.connect(btnApplyClick)

    def __layout__(self):
        layoutObject = QVBoxLayout()
        for lbl, ldt in zip(self.objectLabel, self.objectInput):
            layoutObjects = QHBoxLayout()
            layoutObjects.addWidget(lbl)
            layoutObjects.addWidget(ldt)
            layoutObject.addLayout(layoutObjects)
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnApply)
        layout = QVBoxLayout()
        layout.addLayout(layoutObject)
        layout.addLayout(layoutBtn)
        self.setLayout(layout)
