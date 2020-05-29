from PyQt5.QtWidgets import *
from connector.connDB import connDB
from method.dbList import returnMainList


class DialogCreateDB(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        pass

    def __variables__(self):
        self.DB_YEAR = None
        self.connDB = None

    def __component__(self):
        pass

    def __comboBox__(self):
        trueYear =
        falseYear = returnMainList()
        self.cbxYear = QComboBox()


    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('취소')
        self.btnClose.click.connect(btnCloseClick)

        def btnCreateClick():



    def __layout__(self):