from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from connector.connBusiness import connBusiness
from material.GeneralLabel import GeneralLabel
from component.dialog.DialogNewBusiness import DialogNewBusiness
from component.table.TableAdminBusiness import TableAdminBusiness
from component.dialog.DialogMassage import DialogMassage
from material.Label import LblNull
from material.PushButton import BtnTool
from material.PushButton import BtnTabClose


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
        def btnCloseClick():
            idx = self.windows.tab.currentIndex()
            self.windows.tab.removeTab(idx)
            self.windows.currentTabs.pop(idx)
        self.btnClose = BtnTabClose('닫기(Esc)', btnCloseClick)

        def btnInsertClick():
            try:
                dig = DialogNewBusiness(self)
                dig.exec_()
            except Exception as e:
                print(e)
        self.btnInput = BtnTool('신규 입력', btnInsertClick, shortcut='Ctrl+N')

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
        self.btnSave = BtnTool('저장', btnSaveClick, shortcut='Ctrl+S')

        def btnRefreshClick():
            # windows에서 한꺼번에 구현할 것
            pass
        self.btnRefresh = BtnTool('새로고침(F5)', btnRefreshClick, shortcut='F5')

        def btnExcelClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 내보내기", directory='', filter='*.xlsx')[0]
            if filePath != '':
                dataFrame = self.tbl.dataFrame
                dataFrame.to_excel(filePath, sheet_name="화재안전팀 사업 현황", index=False)
                DialogMassage('엑셀로 내보내기가 완료되었습니다.')
        self.btnExcel = BtnTool('엑셀로 저장', btnExcelClick, shortcut='Ctrl+E')
        self.btnExcel.clicked.connect(btnExcelClick)

    def __table__(self):
        self.tbl = TableAdminBusiness(self)

    def __label__(self):
        cnt = len(self.tbl.dataFrame)-2
        cnt = 0 if cnt < 0 else cnt
        self.lblCount = GeneralLabel(f"총 사업 수 : {cnt} 건")

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInput)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnRefresh)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(LblNull(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.lblCount)
        layout.addWidget(self.tbl)
        self.setLayout(layout)
