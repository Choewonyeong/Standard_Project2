from PyQt5.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    def __init__(self, item):
        QCheckBox.__init__(self)
        style = "QCheckBox{margin-left: 10px; background-color: rgba(255, 255, 255, 10);} "
        self.setStyleSheet(style)
        self.item = item

    def getRow(self):
        return self.item.row()
