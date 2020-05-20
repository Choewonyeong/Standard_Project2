from PyQt5.QtWidgets import *
from pandas import ExcelWriter
from component.dialog.DialogNewBusiness import DialogNewBusiness
from component.table.TableAdminBusiness import TableAdminBusiness


class DialogAdminBusiness(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        pass

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__layout__()

    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('닫기')
        self.btnClose.clicked.connect(btnCloseClick)
        self.btnClose.setFixedWidth(80)

        def btnInsertClick():
            dig = DialogNewBusiness()
            dig.exec_()
        self.btnInput = QPushButton('신규 입력')
        self.btnInput.clicked.connect(btnInsertClick)
        self.btnInput.setFixedWidth(80)

        def btnSaveClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath != '':
                with ExcelWriter(filePath) as writer:
                    dataFrame = self.tbl.dataFrame
                    dataFrame.to_excel(writer, sheet_name="화재안전팀 사업 현황", index=False)
                writer.close()
        self.btnSave = QPushButton('엑셀로 저장')
        self.btnSave.clicked.connect(btnSaveClick)
        self.btnSave.setFixedWidth(80)

    def __table__(self):
        self.tbl = TableAdminBusiness()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInput)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tbl)
        self.setLayout(layout)
