from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, item, text):
        super().__init__()
        self.item = item
        self.clickValue = 0
        self.setText(text)
