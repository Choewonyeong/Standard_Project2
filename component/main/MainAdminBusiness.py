from PyQt5.QtWidgets import *

from connector.connBusiness import connBusiness
from material.GeneralLabel import GeneralLabel
from component.dialog.DialogNewBusiness import DialogNewBusiness
from component.table.TableAdminBusiness import TableAdminBusiness
from component.dialog.DialogMassage import DialogMassage


class MainAdminBusiness(QWidget):
    def __init__(self, windows):
        QWidget.__init__(self)
        self.windows = windows
        self.__setting__()
        self.__connector__()
        self.__component__()

    def __setting__(self):
        pass

    def __connector__(self):
        self.connBusiness = connBusiness()

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__label__()
        self.__layout__()

    def __pushButton__(self):
        def btnInsertClick():
            try:
                dig = DialogNewBusiness(self)
                dig.exec_()
            except Exception as e:
                print(e)
        self.btnInput = QPushButton('신규 입력')
        self.btnInput.clicked.connect(btnInsertClick)
        self.btnInput.setFixedWidth(80)

        def btnSaveClick():
            for obj in self.tbl.objects:
                cnt = 0
                if obj.editLog:
                    self.connBusiness.updateBusiness(obj.header, obj.data, obj.ID)
                    obj.init = obj.data
                    obj.editLog = False
                    cnt += 1
                if cnt:
                    DialogMassage('저장되었습니다.')
        self.btnSave = QPushButton('저장')
        self.btnSave.clicked.connect(btnSaveClick)
        self.btnSave.setFixedWidth(80)

        # 엑셀로 저장 후 종료됨 -> 왜?
        def btnExcelClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath != '':
                dataFrame = self.tbl.dataFrame
                dataFrame.to_excel(filePath, sheet_name="화재안전팀 사업 현황", index=False)
                DialogMassage('엑셀로 내보내기가 완료되었습니다.')
        self.btnExcel = QPushButton('엑셀로 저장')
        self.btnExcel.clicked.connect(btnExcelClick)
        self.btnExcel.setFixedWidth(80)

    def __table__(self):
        self.tbl = TableAdminBusiness(self)

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
