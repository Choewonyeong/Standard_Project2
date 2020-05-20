from PyQt5.QtWidgets import QPushButton
from component.dialog.DialogMassage import DialogMassage
from connector.connUser import connUser
from connector.connBusiness import connBusiness


class TablePushButton(QPushButton):
    def __init__(self, row, col, text, table, option=None):
        QPushButton.__init__(self)
        self.row = row
        self.col = col
        self.table = table
        self.option = option
        self.setText(text)
        self.setFixedWidth(80)
        self.clicked.connect(self.btnClick)
        self.__setting__()

    def __setting__(self):
        self.ID = self.table.item(self.row, 0).text()
        self.clicked.connect(self.btnClick)
        if self.option == 'User':
            self.connUser = connUser()
        if self.option == 'Business':
            self.connBusiness = connBusiness()
        self.table.setCellWidget(self.row, self.col, self)

    def btnClick(self):
        msgBox = DialogMassage("계정 정보를 지우시겠습니까?", True)
        if self.option == 'User' and msgBox.value:
            self.connUser.deleteUser(self.ID)
            self.table.removeRow(self.row)
        if self.optioin == 'Business' and msgBox.value:
            self.connBusiness.deleteBusiness(self.ID)
            self.table.removeRow(self.row)
