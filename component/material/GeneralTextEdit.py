from PyQt5.QtWidgets import QTextEdit


class GeneralTextEdit(QTextEdit):
    def __init__(self, text=''):
        QTextEdit.__init__(self)
        # self.setStyleSheet()
        self.text = text
        self.setText(text)

