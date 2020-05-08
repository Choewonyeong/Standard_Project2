from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt


class Item(QTableWidgetItem):
    def __init__(self):
        super().__init__()
        self.setData(Qt.UserRole, 0)

    def setdata(self, value):
        self.setData(Qt.UserRole, value)
