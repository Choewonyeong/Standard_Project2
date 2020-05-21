from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pandas import ExcelWriter
from connector.connBusiness import connBusiness
from component.material.GeneralLabel import GeneralLabel
from component.dialog.DialogNewBusiness import DialogNewBusiness
from component.table.TableAdminBusiness import TableAdminBusiness


class GroupBoxAdminBusiness(QGroupBox):
    def __init__(self, window):
        QGroupBox.__init__(self)
        self.window = window
        self.__setting__()
        self.__connector__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        background = QPalette()
        background.setBrush(10, QBrush(QColor(255, 255, 255)))
        self.setPalette(background)

    def __connector__(self):
        self.connBusiness = connBusiness()

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__label__()
        self.__layout__()

    def __pushButton__(self):
        def btnInsertClick():
            dig = DialogNewBusiness(self)
            dig.exec_()
        self.btnInput = QPushButton('신규 입력')
        self.btnInput.clicked.connect(btnInsertClick)
        self.btnInput.setFixedWidth(80)

        def btnSaveClick():
            for obj in self.tbl.objects:
                if obj.editLog:
                    self.connBusiness.updateBusiness(obj.header, obj.data, obj.ID)
        self.btnSave = QPushButton('저장')
        self.btnSave.clicked.connect(btnSaveClick)
        self.btnSave.setFixedWidth(80)

        def btnExcelClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath != '':
                with ExcelWriter(filePath) as writer:
                    dataFrame = self.tbl.dataFrame
                    dataFrame.to_excel(writer, sheet_name="화재안전팀 사업 현황", index=False)
                writer.close()
        self.btnExcel = QPushButton('엑셀로 저장')
        self.btnExcel.clicked.connect(btnExcelClick)
        self.btnExcel.setFixedWidth(80)

    def __table__(self):
        self.tbl = TableAdminBusiness()

    def __label__(self):
        cnt = len(self.tbl.dataFrame)-2
        cnt = 0 if cnt < 0 else cnt
        self.lblCount = GeneralLabel(f"총 사업 수 : {cnt} 건")

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnInput)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.lblCount)
        layout.addWidget(self.tbl)
        self.setLayout(layout)
