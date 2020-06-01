from PyQt5.QtWidgets import QTextEdit


class TableTextEdit(QTextEdit):
    def __init__(self, row, col, text, table):
        QTextEdit.__init__(self)
        self.row = row
        self.col = col
        self.init = text
        self.setText(text)
        self.table = table
        self.__setting__()

    def __setting__(self):
        def getData(text):
            self.data = text
            if self.init == self.data:
                self.editLog = False
            elif self.init != self.data:
                self.editLog = True
        self.header = self.table.horizontalHeaderItem(self.col)
        self.ID = self.table.item(self.row, 0).text()
        self.data = None
        self.editLog = False
        self.textChanged.connect(getData)
        self.table.setCellWidget(self.row, self.col, self)

