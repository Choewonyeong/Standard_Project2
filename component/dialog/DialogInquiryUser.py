from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pandas import ExcelWriter
from component.table.TableInquiryUser import TableInquiryUser


class DialogInquiryUser(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __variables__(self):
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

        def btnSaveClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath != '':
                with ExcelWriter(filePath) as writer:
                    dataFrame = self.tbl.dataFrame
                    dataFrame.to_excel(writer, sheet_name="화재안전팀 부서원 현황(일반)", index=False)
                writer.close()
        self.btnSave = QPushButton('엑셀로 저장')
        self.btnSave.clicked.connect(btnSaveClick)
        self.btnSave.setFixedWidth(80)

    def __table__(self):
        self.tbl = TableInquiryUser()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tbl)
        self.setLayout(layout)