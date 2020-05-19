from PyQt5.QtWidgets import QComboBox


class comboBox(QComboBox):
    def __init__(self, row, col):
        QComboBox.__init__(self)
        self.row = row
        self.col = col

