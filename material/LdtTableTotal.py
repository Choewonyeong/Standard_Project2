from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

default = """
QLineEdit{
    color: black;
    font-weight: bold;
    border: 0px solid white;
    background: white;
}
"""


class LdtTableTotal(QLineEdit):
    def __init__(self, row, col, text, table):
        QLineEdit.__init__(self)
        self.setStyleSheet(default)
        self.row = row
        self.col = col
        self.setText(text)
        self.table = table
        self.__setting__()

    def __setting__(self):
        self.header = self.table.horizontalHeaderItem(self.col).text()
        self.number = self.table.item(self.row, 0).text()
        self.setAlignment(Qt.AlignCenter)
        self.table.setCellWidget(self.row, self.col, self)
        self.setFixedWidth(60)
        self.setEnabled(False)
