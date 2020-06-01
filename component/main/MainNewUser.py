from PyQt5.QtWidgets import *
from component.dialog.DialogMassage import DialogMassage
from component.table.TableNewUser import TableNewUser
from PyQt5.QtCore import Qt
from connector.connUser import connUser


class MainNewUser(QWidget):
    def __init__(self, windows):
        QWidget.__init__(self)
        self.windows = windows
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__component__()

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.columns = self.connUser.dataFrameSignup(column=True)+['', '']
        self.dataFrame = self.connUser.dataFrameSignup()

    def __setting__(self):
        # self.setStyleSheet()
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__tableLayout__()

    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('닫기')
        self.btnClose.setFixedWidth(80)
        self.btnClose.clicked.connect(btnCloseClick)

    def __table__(self):
        self.tblNewUser = TableNewUser(self, self.columns, self.dataFrame)

    def __tableLayout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnClose)
        layout.addWidget(self.tblNewUser)
        self.setLayout(layout)

