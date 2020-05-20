from PyQt5.QtWidgets import QComboBox


class TableComboBox(QComboBox):
    def __init__(self, row, col, items, text, table):
        QComboBox.__init__(self)
        self.row = row
        self.col = col
        self.addItems(items)
        self.table = table
        self.init = text
        self.setCurrentText(text)
        self.__setting__()

    def __setting__(self):
        def getData(text):
            self.data = text
            if self.init == self.data:
                self.editLog = False
            elif self.init != self.data:
                self.editLog = True
        self.header = self.table.horizontalHeaderItem(self.col).text()
        self.ID = self.table.item(self.row, 0).text()
        self.data = None
        self.editLog = False
        self.currentTextChanged.connect(getData)
        self.table.setCellWidget(self.row, self.col, self)
