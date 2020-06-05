from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from component.dialog.DialogMassage import DialogMassage
from connector.connUser import connUser
from component.table.TableInquiryUser import TableInquiryUser
from material.PushButton import BtnTool, BtnTabClose


class MainInquiryUser(QWidget):
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
        self.__layout__()

    def __pushButton__(self):
        def btnCloseClick():
            idx = self.windows.tab.currentIndex()
            self.windows.tab.removeTab(idx)
            self.windows.currentTabs.pop(idx)
        self.btnClose = BtnTabClose('닫기(Esc)', btnCloseClick)

        def btnExcelClick():
            dig = QFileDialog()
            filePath = dig.getSaveFileName(caption='엑셀로 내보내기', filter='*.xlsx')[0]
            if filePath != '':
                df = self.connUser.dataFrameUser()
                del df['비밀번호']
                del df['재직상태']
                del df['접근권한']
                del df['가입승인여부']
                df.to_excel(filePath, sheet_name='화재안전팀 부서원 현황(일반)', index=False)
                DialogMassage(f'저장되었습니다.\n\n○ 파일 경로 : {filePath}')
        self.btnExcel = BtnTool('엑셀로 저장\n(Ctrl+E)', btnExcelClick)

        def btnRefreshClick():
            pass

        self.btnRefresh = BtnTool('새로고침(F5)', btnRefreshClick)

    def __table__(self):
        self.tbl = TableInquiryUser()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(self.btnRefresh)
        layoutBtn.addWidget(QLabel(), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tbl)
        self.setLayout(layout)