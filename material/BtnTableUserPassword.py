from PyQt5.QtWidgets import QPushButton
from component.dialog.DialogMassage import DialogMassage
from component.dialog.DialogPassword import DialogPassword
from component.dialog.DialogAdmin import DialogAdmin
from connector.connUser import connUser


class BtnTableUserPassword(QPushButton):
    def __init__(self, row, col, text, table, enable=True):
        QPushButton.__init__(self)
        self.row = row
        self.col = col
        self.table = table
        self.enable = enable
        self.setText(text)
        self.setFixedWidth(80)
        self.clicked.connect(self.btnClick)
        self.table.setCellWidget(row, col, self)
        self.__variables__()

    def __variables__(self):
        self.ID = self.table.item(self.row, 0).text()
        self.connUser = connUser()

    def btnClick(self):
        try:
            DialogAdmin(self.ID, self.row, self.table)
        except Exception as e:
            print(e)