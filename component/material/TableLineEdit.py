from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

style = """
QLineEdit{
    border: 0px solid white;
}
"""


class TableLineEdit(QLineEdit):
    def __init__(self, row, col, text, table, option=None):
        QLineEdit.__init__(self)
        # self.setStyleSheet(style)
        self.row = row
        self.col = col
        self.init = text
        self.setText(text)
        self.table = table
        self.option = option
        self.__setting__()
        self.__setOption__()

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
        self.textChanged.connect(getData)
        self.table.setCellWidget(self.row, self.col, self)

    def __setOption__(self):
        if self.option == 'disable':
            self.setEnabled(False)

        if self.option == 'dateFormat':
            self.setPlaceholderText('ex) 2014-03-01')

        if self.option == 'moneyFormat':
            def textFormat(text):
                try:
                    text = text.replace(',', '')
                    self.setText(format(int(text), ','))
                except:
                    pass
            self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.textEdited.connect(textFormat)

        if self.option == 'identity':
            self.setPlaceholderText('ex) 950302-1')

        if self.option == 'password':
            self.setEchoMode(QLineEdit.Password)
