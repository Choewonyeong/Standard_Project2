from PyQt5.QtWidgets import *


class Windows(QWidget):
    def __init__(self, account, author):
        QWidget.__init__(self)
        self.account = account
        self.author = author

    def __setting__(self):
        pass