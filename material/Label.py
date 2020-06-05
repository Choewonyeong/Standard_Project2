from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from design.style import Label


class LblMessage(QLabel):
    def __init__(self, text):
        QLabel.__init__(self)
        self.setStyleSheet(Label.styleMessage)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)


class LblSignup(QLabel):
    def __init__(self, text):
        QLabel.__init__(self)
        self.setStyleSheet(Label.styleSignup)
        self.setText(text)


class LblImage(QLabel):
    def __init__(self, img, width):
        QLabel.__init__(self)
        from PyQt5.QtGui import QPixmap
        self.setPixmap(QPixmap(img).scaledToWidth(width))
        self.setAlignment(Qt.AlignCenter)


class LblNull(QLabel):
    def __init__(self):
        QLabel.__init__(self)
        self.setText('')


class LblUserSelf(QLabel):
    def __init__(self, text):
        QLabel.__init__(self)
        self.setStyleSheet(Label.styleUserSelf)
        self.setText(text)


class LblInformation(QLabel):
    def __init__(self, text):
        QLabel.__init__(self)
        self.setStyleSheet(Label.styleInformation)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
