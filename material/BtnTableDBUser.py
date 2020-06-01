from PyQt5.QtWidgets import QPushButton
from component.dialog.DialogMassage import DialogMassage
from connector.connDB import connDB


class BtnTableDBUser(QPushButton):
    def __init__(self, row, col, text, table, year, enable=True):
        QPushButton.__init__(self)
        self.row = row
        self.col = col
        self.table = table
        self.year = year
        self.enable = enable
        self.setText(text)
        self.setFixedWidth(80)
        self.clicked.connect(self.btnClick)
        self.table.setCellWidget(row, col, self)
        self.__variables__()

    def __variables__(self):
        self.ID = self.table.item(self.row, 0).text()
        self.connDB = connDB(self.year)

    def btnClick(self):
        try:
            if self.text() == '적용':
                msgBox = DialogMassage("해당 계정을 현재의 데이터베이스에서 제외하시겠습니까?", True)
                if msgBox.value:
                    self.connDB.updateUserApplyStatus('제외', self.ID)
                    self.setText('제외')
            elif self.text() == '제외':
                msgBox = DialogMassage("해당 계정을 현재의 데이터베이스에 적용시키겠습니까?", True)
                if msgBox.value:
                    self.connDB.updateUserApplyStatus('적용', self.ID)
                    self.setText('적용')
        except Exception as e:
            print('btnClick', e)