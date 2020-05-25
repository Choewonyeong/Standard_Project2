from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super(CheckableComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.Checked

    def setItemChecked(self, index, checked=True):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)


class Test(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__component__()

    def __component__(self):
        self.__listWidget__()
        self.__comboBox__()
        self.__layout__()

    def __listWidget__(self):
        self.listWidget = QListWidget()
        item = QListWidgetItem()
        item.setText('Exam')
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.listWidget.addItem(item)

    def __comboBox__(self):
        def comboBoxItemCheck(idx):
            print(idx)
        self.comboBox = CheckableComboBox()
        self.comboBox.addItems(['필터', 'TEST'])
        self.comboBox.setItemChecked(0, False)

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addWidget(self.comboBox)
        self.setLayout(layout)


if __name__ == "__main__":
    from sys import argv
    app = QApplication(argv)
    test = Test()
    test.show()
    app.exec_()