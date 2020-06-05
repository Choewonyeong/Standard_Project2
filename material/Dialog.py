from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from design.style.Dialog import styleGeneral
from PyQt5.QtCore import Qt


class DigGeneral(QDialog):
    def __init__(self, parent=None, app=None):
        QDialog.__init__(self)
        self.parent = parent
        self.app = app
        background = QPalette()
        background.setBrush(10, QBrush(QColor(255, 255, 255)))
        self.setPalette(background)