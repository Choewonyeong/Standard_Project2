from PyQt5.QtWidgets import QPushButton
from component.dialog.DialogMassage import DialogMassage
from connector.connUser import connUser
from connector.connDB import connDB


class BtnTableUserDelete(QPushButton):
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
        self.connDB = connDB(self.table.widget.windows.CURRENT_YEAR)

    def btnClick(self):
        msgBox = DialogMassage("해당 계정에 대한 모든 정보를 삭제합니까?\n삭제 후에는 되돌릴 수 없습니다.", True)
        if msgBox.value:
            self.connUser.deleteUser(self.ID)
            self.connDB.deleteUser(self.ID)
            self.table.removeRow(self.row)

