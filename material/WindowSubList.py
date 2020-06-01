from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget


class WindowSubList(QListWidget):
    def __init__(self, items=None):
        QListWidget.__init__(self)
        if items is None:
            items = ['']
        self.items = items
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.addItems(items)
        self.setFixedWidth(180)
        self.setVisible(False)

