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
        self.__setting__()

    def __setting__(self):
        self.ID = self.table.item(self.row, 0).text()
        self.clicked.connect(self.btnClick)
        if self.option == 'User':
            self.connUser = connUser()
        if self.option == 'Business':
            self.connBusiness = connBusiness()
        if self.option == 'Disable':
            self.setEnabled(False)
        self.table.setCellWidget(self.row, self.col, self)

    def btnClick(self):
        try:
            if self.option == 'User':
                msgBox = DialogMassage("계정 정보를 지우시겠습니까?", True)
                if msgBox.value:
                    self.connUser.deleteUser(self.ID)
                    self.table.removeRow(self.row)
            if self.option == 'Business':
                msgBox = DialogMassage("사업 정보를 지우시겠습니까?", True)
                if msgBox.value:
                    self.connBusiness.deleteBusiness(self.ID)
                    self.table.removeRow(self.row)
        except Exception as e:
            print(e)
