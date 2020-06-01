from PyQt5.QtWidgets import *


class GeneralPushButton(QPushButton):
    def __init__(self, text, option=None):
        QPushButton.__init__(self)
        self.setText(text)
        self.option = option

    def __setting__(self):
        pass
        # if self.option == ""

    def __setOption__(self):
        if self.option == "Yes":
            # self.setStyleSheet()
            pass
        if self.option == "Close":
            # self.setStyleSheet()
            pass
        if self.option == "Confirm":
            # self.setStyleSheet()
            pass
