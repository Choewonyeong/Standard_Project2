from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

default = """
QLineEdit{
    border: 0px solid white;
    background: white;
    color: black;
}
"""

backGround = """
QLineEdit{
    border: 0px solid white;
    background: #f7a6a9;
    color: white;
}
"""

whiteFont = """
QLineEdit{
    border: 2px solid white;
    background: white;
    color: white;
}
"""

colorFont = """
QLineEdit{
    border-top: 10px solid #f7a6a9;
    border-bottom: 10px solid #f7a6a9;
    border-left: 0px solid white;
    border-right: 0px solid white;
    background: #f7a6a9;
    color: #f7a6a9;
}
"""


class LdtTableTimeBusiness(QLineEdit):
    def __init__(self, row, col, text, table):
        QLineEdit.__init__(self)
        self.setStyleSheet(default)
        self.row = row
        self.col = col
        self.init = text
        self.setText(text)
        self.table = table
        self.__setting__()
        self.__setStyle__()

    def __setting__(self):
        def getData(text):
            self.data = text
            if self.init == self.data:
                self.editLog = False
            elif self.init != self.data:
                self.editLog = True
        self.header = self.table.horizontalHeaderItem(self.col).text()
        self.number = self.table.item(self.row, 0).text()
        self.data = None
        self.editLog = False
        self.textChanged.connect(getData)
        self.setAlignment(Qt.AlignCenter)
        self.table.setCellWidget(self.row, self.col, self)
        self.setEnabled(False)
        if self.col == 2:
            self.setFixedWidth(80)
        elif self.col == 3:
            self.setFixedWidth(80)

    def __setStyle__(self):
        count = (len(self.table.dataFrame)-3)//2
        colorRow = []
        init = 3
        colorRow.append(init)
        colorRow.append(init+1)
        for num in range(0, count):
            init += 4
            colorRow.append(init)
            colorRow.append(init+1)

        hideFonts = [1]
        for row in range(2, len(self.table.dataFrame)+1):
            if row % 2 == 0:
                hideFonts.append(row)

        if self.row in colorRow:
            self.setStyleSheet(backGround)

        if self.row in hideFonts and self.col in [1, 2]:
            if self.row in colorRow:
                self.setStyleSheet(colorFont)
            else:
                self.setStyleSheet(whiteFont)
