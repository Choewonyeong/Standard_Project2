from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from pandas import ExcelWriter
from connector.connBusiness import connBusiness
from component.dialog.DialogNewBusiness import DialogNewBusiness
from component.table.TableAdminBusiness import TableAdminBusiness


class WidgetAdminBusiness(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__setting__()
        self.__connector__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __connector__(self):
        self.connBusiness = connBusiness()

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

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInput)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tbl)
        self.setLayout(layout)
