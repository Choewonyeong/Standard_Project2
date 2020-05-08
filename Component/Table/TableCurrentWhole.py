from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from Component.Table.TableCurrentUser import TableCurrentUser
from Component.Table.TableCurrentBusiness import TableCurrentBusiness


class TableCurrentWhole(QWidget):
    def __init__(self,  year, widget):
        QWidget.__init__(self)
        self.year = year
        self.widget = widget
        self.__component__()

    def __component__(self):
        self.__tables__()
        self.__layout__()

    def __tables__(self):
        self.tblUser = TableCurrentUser(self.year, self.widget)
        self.tblBusiness = TableCurrentBusiness(self.year, self.widget)

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.tblUser)
        layout.addWidget(self.tblBusiness)
        self.setLayout(layout)
