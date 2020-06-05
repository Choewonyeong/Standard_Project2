from PyQt5.QtWidgets import QGroupBox
from design.style import GroupBox


class GbxSignup(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.setStyleSheet(GroupBox.styleSignup)
