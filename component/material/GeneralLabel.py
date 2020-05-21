from PyQt5.QtWidgets import QLabel


class GeneralLabel(QLabel):
    def __init__(self, text='', option=None):
        QLabel.__init__(self)
        self.text = text
        self.setText(text)
        self.option = option

    def __setOption__(self):
        if self.option == 'title':
            # self.setStyleSheet()
            print('title')
        if self.option == '':
            # self.setStyleSheet()
            print('')
        if self.option == '':
            # self.setStyleSheet()
            print('')
