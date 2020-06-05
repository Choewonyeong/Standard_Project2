from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from design.style import PushButton


class BtnLogin(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleLogin)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnClose(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleClose)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnSignup(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleSignUp)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnOk(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleYes)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnNo(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleNo)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnYes(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleYes)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnSubmit(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleSubmit)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnCancel(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleCancel)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnUserSelfSave(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleUserSelf_Save)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnUserSelfClose(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleUserSelf_Close)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnUserTimeClose(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleDefault)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnTabClose(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleDefault)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnTool(QPushButton):
    def __init__(self, text, event, default=False, shortcut=None):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleDefault)
        self.setText(text)
        self.clicked.connect(event)
        self.setDefault(default)
        self.setCursor(Qt.PointingHandCursor)
        if shortcut:
            self.setShortcut(shortcut)


class BtnAcceptInTable(QPushButton):
    def __init__(self, text, event, table, row, col):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleInTable_Accept)
        self.setText(text)
        self.clicked.connect(event)
        self.setCursor(Qt.PointingHandCursor)
        table.setCellWidget(row, col, self)


class BtnRejectInTable(QPushButton):
    def __init__(self, text, event, table, row, col):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleInTable_Accept)
        self.setText(text)
        self.clicked.connect(event)
        self.setCursor(Qt.PointingHandCursor)
        table.setCellWidget(row, col, self)


class BtnPasswordInTable(QPushButton):
    def __init__(self, text, table, row, col):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleInTable_Default)
        self.setText(text)
        self.table = table
        self.row = row
        self.col = col
        self.setFixedWidth(80)
        self.clicked.connect(self.btnClick)
        table.setCellWidget(row, col, self)
        self.account = self.table.item(self.row, 0).text()

    def btnClick(self):
        from component.dialog.DialogAdmin import DialogAdmin
        DialogAdmin(self.account, self.row, self.table)


class BtnDeleteInTable(QPushButton):
    def __init__(self, text, table, row, col):
        QPushButton.__init__(self)
        self.setStyleSheet(PushButton.styleInTable_Default)
        self.setText(text)
        self.table = table
        self.row = row
        self.col = col
        self.setFixedWidth(80)
        self.clicked.connect(self.btnClick)
        table.setCellWidget(row, col, self)
        self.account = self.table.item(self.row, 0).text()

    def btnClick(self):
        from component.dialog.DialogMassage import DialogMassage
        question = DialogMassage('계정을 삭제하시겠습니까?\n삭제 시 해당 계정에 대한 정보는 전부 삭제되며\n삭제 후에는 되돌릴 수 없습니다.', question=True)
        if question.value:
            try:
                from connector.connDB import connDB
                from connector.connDB import connUser
                __connDB__ = connDB(self.table.widget.windows.CURRENT_YEAR)
                __connDB__.deleteUser(self.account)
                __connUser__ = connUser()
                __connUser__.deleteUser(self.account)
                self.table.removeRow(self.row)
                DialogMassage('계정이 삭제되었습니다.')
            except Exception as e:
                print('btnClick', e)