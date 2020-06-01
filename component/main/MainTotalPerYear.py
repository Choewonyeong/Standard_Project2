from PyQt5.QtWidgets import *
from pandas import ExcelWriter
from component.dialog.DialogMassage import DialogMassage
from component.table.TableTotalPerYear import TableTotalPerYear


class MainTotalPerYear(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        pass

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__layout__()

    def __pushButton__(self):
        def btnExcelClick():
            dig = QFileDialog(self)
            filePath = dig.getSaveFileName(caption="엑셀로 저장", directory='', filter='*.xlsx')[0]
            if filePath != '':
                with ExcelWriter(filePath) as writer:
                    dataFrame = self.tbl.dataFrame
                    dataFrame.to_excel(writer, sheet_name="화재안전팀 연도별 시간 집계", index=False)
                    DialogMassage('엑셀로 내보내기가 완료되었습니다.')
                writer.close()
        self.btnExcel = QPushButton('엑셀로 저장')
        self.btnExcel.clicked.connect(btnExcelClick)
        self.btnExcel.setFixedWidth(80)

    def __table__(self):
        self.tbl = TableTotalPerYear()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(''), 10)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addWidget(self.tbl)
        self.setLayout(layout)
