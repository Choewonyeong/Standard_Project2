from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DialogLoading(QDialog):
    def __init__(self, windows):
        QDialog.__init__(self, windows)
        self.__setting__()
        self.__component__()
        self.show()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def __component__(self):
        self.__lable__()
        self.__layout__()

    def __label__(self):
        self.lblText('데이터를 불러오는 중입니다.\n잠시만 기다려주시기 바랍니다.')

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.lblText)
        self.setLayout(layout)