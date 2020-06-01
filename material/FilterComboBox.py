from PyQt5.QtWidgets import QComboBox


class FilterComboBox(QComboBox):
    def __init__(self, col, items, table):
        QComboBox.__init__(self)
        self.col = col
        self.addItems(items)
        self.table = table
        table.setCellWidget(0, col, self)
        self.__setEvent__()

    def __setEvent__(self):
        def textChange(text):
            self.table.Filter(self.col, text)
        self.currentTextChanged.connect(textChange)