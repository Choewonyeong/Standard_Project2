from PyQt5.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def __init__(self, item, itemList):
        QComboBox.__init__(self)
        self.item = item
        self.itemList = itemList
        self.addItems(self.itemList)

    def getData(self):
        return self.item.text()

    def getRow(self):
        return self.item.row()
