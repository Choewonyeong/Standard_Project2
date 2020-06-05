from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from connector.connUser import connUser
from component.dialog.DialogMassage import DialogMassage
from design.style.Dialog import styleGeneral
from material.ComboBox import CbxUserSelf
from material.PushButton import BtnUserSelfSave
from material.PushButton import BtnUserSelfClose
from material.Label import LblUserSelf
from material.LineEdit import LdtUserSelf
from setting.variables import itemUserDegree


class DialogUserSelf(QDialog):
    def __init__(self, account):
        QDialog.__init__(self)
        self.account = account
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()
        self.exec_()

    def __setting__(self):
        self.setStyleSheet(styleGeneral)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(360)

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
            lbl = LblUserSelf(text)
            self.objectLabel.append(lbl)
            if cnt in [0, 11]:
                widget = LdtUserSelf(lock=True, text=info)
                widget.setEnabled(False)
            elif cnt == 2:
                widget = LdtUserSelf(text=info)
                widget.setEchoMode(LdtUserSelf.Password)
            elif cnt == 5:
                widget = CbxUserSelf(itemUserDegree, text=info)
            else:
                widget = LdtUserSelf(text=info)
            self.objectInput.append(widget)

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
            self.close()
        self.btnClose = BtnUserSelfClose('닫기(Esc)', btnCloseClick)
        self.btnApply = BtnUserSelfSave('저장(Enter)', btnApplyClick)

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
