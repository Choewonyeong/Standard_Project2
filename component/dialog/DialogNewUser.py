from PyQt5.QtWidgets import *
from component.table.TableNewUser import TableNewUser
from PyQt5.QtCore import Qt


class DialogNewUser(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__layout__()

    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('닫기')
        self.btnClose.setFixedWidth(80)
        self.btnClose.clicked.connect(btnCloseClick)

    def __table__(self):
        self.tblNewUser = TableNewUser()

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnClose)
        layout.addWidget(self.tblNewUser)
        self.setLayout(layout)

