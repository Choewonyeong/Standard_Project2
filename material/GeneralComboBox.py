from PyQt5.QtWidgets import QComboBox


class GeneralComboBox(QComboBox):
    def __init__(self, items, text=''):
        QComboBox.__init__(self)
        # self.setStyleSheet()
        self.addItems(items)
        self.setCurrentText(text)

