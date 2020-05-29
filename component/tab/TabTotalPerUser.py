from PyQt5.QtWidgets import  *
from method.totalList import returnTotalPerUser


class TableTotalPerUser(QTabWidget):
    def __init__(self, year):
        QTabWidget.__init__(self)
        self.year = year
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        pass

    def __variables__(self):
        self.columns = returnTotalPerUser(self.year, column=True)
        self.totalDict = returnTotalPerUser(self.year)

    def __component__(self):
        self.__table__()
        self.__layout__()

    def __table__(self):
        pass

    def __layout__(self):
        pass