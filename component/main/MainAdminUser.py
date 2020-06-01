from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pandas import ExcelWriter

from material.GeneralLabel import GeneralLabel
from connector.connUser import connUser
from component.table.TableAdminUser import TableAdminUser


class MainAdminUser(QWidget):
    def __init__(self, windows):
        QWidget.__init__(self)
        self.windows = windows
        self.__setting__()
        self.__connector__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __connector__(self):
        self.connUser = connUser()

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__label__()
        self.__layout__()

    def __pushButton__(self):
        def btnSaveClick():
            for obj in self.tbl.objects:
                if obj.editLog:
                    self.tbl.UpdateEditDate(obj.row, self.connUser.updateUser(obj.header, obj.data, obj.ID))
        self.btnSave = QPushButton('저장')
        self.btnSave.clicked.connect(btnSaveClick)
        self.btnSave.setFixedWidth(80)

        def btnExcelClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath != '':
                with ExcelWriter(filePath) as writer:
                    dataFrame = self.tbl.dataFrame
                    dataFrame.to_excel(writer, sheet_name="화재안전팀 부서원 현황(관리자)", index=False)
                writer.close()
        self.btnExcel = QPushButton('엑셀로 저장')
        self.btnExcel.clicked.connect(btnExcelClick)
        self.btnExcel.setFixedWidth(80)

    def __table__(self):
        self.tbl = TableAdminUser(self)

    def __label__(self):
        cnt = len(self.tbl.dataFrame)
        cnt = 0 if cnt < 0 else cnt
        self.lblCount = GeneralLabel(f"총 부서원 수 : {cnt} 명")

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.lblCount)
        layout.addWidget(self.tbl)
        self.setLayout(layout)