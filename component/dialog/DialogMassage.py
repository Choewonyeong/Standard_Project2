from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt


class DialogMassage(QDialog):
    def __init__(self, text, question=False):
        QDialog.__init__(self)
        self.text = text
        self.question = question
        self.value = False
        self.__setting__()
        self.__component__()
        self.exec_()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(350)
        background = QPalette()
        background.setBrush(10, QBrush(QColor(255, 255, 255)))
        self.setPalette(background)

    def __component__(self):
        self.__label__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        self.lblText = QLabel(self.text)
        self.lblText.setAlignment(Qt.AlignCenter)

    def __pushButton__(self):
        def btnOkClick():
            self.value = False
            self.close()
        self.btnOk = QPushButton('확인')
        self.btnOk.setFixedWidth(80)
        self.btnOk.clicked.connect(btnOkClick)
        # self.btnOk.setStyleSheet()

        def btnYesClick():
            self.value = True
            self.close()
        self.btnYes = QPushButton('예')
        self.btnYes.setFixedWidth(80)
        self.btnYes.clicked.connect(btnYesClick)
        # self.btnYes.setStyleSheet()

        def btnNoClick():
            self.value = False
            self.close()
        self.btnNo = QPushButton('아니오')
        self.btnNo.setFixedWidth(80)
        self.btnNo.clicked.connect(btnNoClick)
        # self.btnNo.setStyleSheet()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        if self.question:
            self.btnNo.setDefault(True)
            layoutBtn.addWidget(self.btnNo)
            layoutBtn.addWidget(self.btnYes)
        elif not self.question:
            self.btnOk.setDefault(True)
            layoutBtn.addWidget(self.btnOk)
        layout = QVBoxLayout()
        layout.addWidget(self.lblText)
        layout.addWidget(QLabel())
        layout.addLayout(layoutBtn)
        self.setLayout(layout)
