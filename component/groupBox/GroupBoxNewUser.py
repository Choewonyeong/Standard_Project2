from PyQt5.QtWidgets import *
from component.table.TableNewUser import TableNewUser
from PyQt5.QtCore import Qt


class GroupBoxNewUser(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __component__(self):
        self.__table__()
        self.__layout__()

    def __table__(self):
        self.tblNewUser = TableNewUser()

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.tblNewUser)
        self.setLayout(layout)

