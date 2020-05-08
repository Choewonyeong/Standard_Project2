from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from Design import Style


class DialogMessageBox(QDialog):
    def __init__(self, title, text, btnYesOrNo=False):
        QDialog.__init__(self)
        self.setWindowTitle(title)
        self.text = text
        self.btnCloseBool = False if btnYesOrNo else True
        self.btnYesOrNoBool = False if self.btnCloseBool else True
        self.__component__()

    def __component__(self):
        self.__setting__()
        self.__label__()
        self.__buttons__()
        self.__layout__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(Style.Message_Dialog)
        self.setFixedWidth(350)

    def __label__(self):
        self.lblQuestion = QLabel(self.text)
        self.lblQuestion.setAlignment(Qt.AlignCenter)

    def __buttons__(self):
        if self.btnCloseBool:
            btnClose = QPushButton('확인')
            btnClose.setStyleSheet(Style.PushButton_Close)
            btnClose.clicked.connect(self.btnCloseClick)
            btnClose.setFixedWidth(300)
            self.layoutBtn = QHBoxLayout()
            self.layoutBtn.addWidget(btnClose)
        if self.btnYesOrNoBool:
            btnNo = QPushButton('아니오')
            btnNo.setStyleSheet(Style.PushButton_Close)
            btnNo.clicked.connect(self.btnNoClick)
            btnNo.setDefault(True)
            btnYes = QPushButton('예')
            btnYes.setStyleSheet(Style.PushButton_Tools)
            btnYes.clicked.connect(self.btnYesClick)
            btnNo.setFixedWidth(300)
            btnYes.setFixedWidth(300)
            self.layoutBtn = QHBoxLayout()
            self.layoutBtn.addWidget(QLabel(''), 10)
            self.layoutBtn.addWidget(btnNo)
            self.layoutBtn.addWidget(QLabel())
            self.layoutBtn.addWidget(btnYes)
            self.layoutBtn.addWidget(QLabel(''), 10)

    def btnCloseClick(self):
        self.Close = True
        self.close()

    def btnNoClick(self):
        self.No = True
        self.Yes = False
        self.close()

    def btnYesClick(self):
        self.Yes = True
        self.No = False
        self.close()
    
    def __layout__(self):
        lblNull = QLabel()
        lblNull.setFixedWidth(30)
        layoutLbl = QHBoxLayout()
        layoutLbl.addWidget(self.lblQuestion, 10)
        layout = QVBoxLayout()
        layout.addWidget(QLabel())
        layout.addLayout(layoutLbl)
        layout.addWidget(QLabel())
        layout.addWidget(QLabel())
        layout.addLayout(self.layoutBtn)
        self.setLayout(layout)
