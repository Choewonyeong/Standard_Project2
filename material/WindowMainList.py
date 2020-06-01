from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt


class WindowMainList(QListWidget):
    def __init__(self, items=None):
        QListWidget.__init__(self)
        if items is None:
            items = ['']
        self.items = items
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.addItems(items)
        self.setFixedWidth(120)
