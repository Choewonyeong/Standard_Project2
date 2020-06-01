from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

default = """
QLineEdit{
    border: 0px solid white;
    background: white;
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
    border: 0px solid white;
    background: white;
    color: white;
}
"""

colorFont = """
QLineEdit{
    border: 0px solid white;
    background: #f7a6a9;
    color: #f7a6a9;
}
"""


class LdtTableTime(QLineEdit):
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
        self.__setEvent__()

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
        self.setFixedWidth(60)

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

    def __setEvent__(self):
        def editEvent(text):
            item = QTableWidgetItem(text)
            item.setFlags(Qt.ItemIsEditable)
            self.table.setItem(self.row, self.col, item)
        self.textEdited.connect(editEvent)
