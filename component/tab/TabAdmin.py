from PyQt5.QtWidgets import *


class TabAdmin(QTabWidget):
    def __init__(self):

        def tabCloseEvent(idx):
            self.removeTab(idx)
        QTabWidget.__init__(self)
        self.__setting__()
        self.__component__()
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(tabCloseEvent)
