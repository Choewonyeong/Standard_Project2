from PyQt5.QtWidgets import QPushButton
from component.dialog.DialogMassage import DialogMassage
from connector.connBusiness import connBusiness


class BtnTableBusinessDelete(QPushButton):
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
        self.connBusiness = connBusiness()

    def btnClick(self):
        msgBox = DialogMassage("해당 사업 정보를 삭제합니까?", True)
        if msgBox.value:
            self.connBusiness.deleteBusiness(self.ID)
            self.table.removeRow(self.row)
