from PyQt5.QtWidgets import *


class WidgetUser(QWidget):
    def __init__(self, account):
        QWidget.__init__(self)
        self.account = account
        self.__setting__()
        self.__component__()

    def __setting__(self):
        pass

    def __component__(self):
        self.__listWidget__()
        self.__tab__()
        self.__layout__()

    def __listWidget__(self):
        itemList = ['개인정보', '시간관리']
        self.lst = QListWidget()
        self.lst.addItems(itemList)

    def __tab__(self):
        self.tab = QTabWidget()

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.lst)
        layout.addWidget(self.tab)
        self.setLayout(layout)

