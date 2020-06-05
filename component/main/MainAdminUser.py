from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from component.dialog.DialogMassage import DialogMassage
from material.GeneralLabel import GeneralLabel
from connector.connUser import connUser
from component.table.TableAdminUser import TableAdminUser
from material.Label import LblNull
from material.PushButton import BtnTool, BtnTabClose


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
        def btnCloseClick():
            idx = self.windows.tab.currentIndex()
            self.windows.tab.removeTab(idx)
            self.windows.currentTabs.pop(idx)
        self.btnClose = BtnTabClose('닫기(Esc)', btnCloseClick)

        def btnSaveClick():
            saveValue = 0
            for obj in self.tbl.objects:
                if obj.editLog:
                    self.tbl.UpdateEditDate(obj.row, self.connUser.updateUser(obj.header, obj.data, obj.number))
                    obj.init = obj.data
                    obj.editLog = False
                    saveValue += 1
            if saveValue:
                DialogMassage('저장되었습니다.')
        self.btnSave = BtnTool('저장', btnSaveClick, shortcut='Ctrl+S')

        def btnRefreshClick():
            # windows에서 한꺼번에 구현할 것
            pass
        self.btnRefresh = BtnTool('새로고침(F5)', btnRefreshClick, shortcut='F5')

        def btnExcelClick():
            dig = QFileDialog()
            filePath = dig.getSaveFileName(caption='엑셀로 내보내기', filter='*.xlsx')[0]
            if filePath != '':
                df = self.connUser.dataFrameUser()
                del df[self.tbl.columns[14]]
                del df[self.tbl.columns[2]]
                df.to_excel(filePath, sheet_name=f'화재안전팀 부서원 현황(상세)', index=False)
                DialogMassage(f'저장되었습니다.\n\n○ 파일 경로 : {filePath}')
        self.btnExcel = BtnTool('엑셀로 저장\n(Ctrl+E)', btnExcelClick)

    def __table__(self):
        self.tbl = TableAdminUser(self)

    def __label__(self):
        cnt = len(self.tbl.dataFrame)
        cnt = 0 if cnt < 0 else cnt
        self.lblCount = GeneralLabel(f"총 부서원 수 : {cnt} 명")

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnRefresh)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(LblNull(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.lblCount)
        layout.addWidget(self.tbl)
        self.setLayout(layout)