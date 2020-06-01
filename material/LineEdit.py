from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from design.style.LineEdit import styleLogin


class LdtLogin(QLineEdit):
    def __init__(self, text=None, holderText=None):
        QLineEdit.__init__(self)
        self.setStyle(styleLogin)
        if text:
            self.setText(text)
        if holderText:
            self.setPlaceholderText(holderText)
        self.setMouseTracking(False)
        self.setAlignment(Qt.AlignCenter)
