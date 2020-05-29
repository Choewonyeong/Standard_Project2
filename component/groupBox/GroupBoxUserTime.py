from PyQt5.QtWidgets import *
from component.dialog.DialogMassage import DialogMassage
from component.table.TableUserTime import TableUserTime
from component.table.TableTimeBusiness import TableTimeBusiness
from component.table.TableTimeHeader import TableTimeHeader
from component.table.TableTimeTotal import TableTimeTotal
from method.valueTran import returnTranValue
from connector.connDB import connDB


class GroupBoxUserTime(QGroupBox):
    def __init__(self, account, year):
        QGroupBox.__init__(self)
        self.account = account
        self.year = year
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()
        self.__setEvent__()

    def __setting__(self):
        pass

    def __connector__(self):
        self.connDB = connDB(self.year)

    def __variables__(self):
        pass

    def __component__(self):
        self.__pushButton__()
        self.__table__()
        self.__scrollBar__()
        self.__layout__()

    def __pushButton__(self):
        def btnSaveClick():
            for obj in self.tblTime.objects:
                if obj.editLog:
                    column = self.tblTime.horizontalHeaderItem(obj.col).text()
                    value = obj.data
                    number = self.tblTime.item(obj.row, 0).text()
                    option = self.tblTime.item(obj.row, 3).text()
                    self.connDB.updateUserTime(column, value, number, option, self.account)
            DialogMassage('저장되었습니다.')
        self.btnSave = QPushButton('저장')
        self.btnSave.clicked.connect(btnSaveClick)

        def btnExcelClick():
            # 구현 필요
            pass
            DialogMassage('엑셀로 내보내기가 완료되었습니다.')
        self.btnExcel = QPushButton('엑셀로 저장')
        self.btnExcel.clicked.connect(btnExcelClick)

    def __table__(self):
        self.tblBusiness = TableTimeBusiness(self.account, self.year)
        self.tblTime = TableUserTime(self.account, self.year)
        self.tblHeader = TableTimeHeader()
        self.tblHeader.setColumnWidth(0, self.tblBusiness.width)
        self.tblHeader.setFixedWidth(self.tblBusiness.width)
        self.tblHeader.setFixedHeight(self.tblHeader.rowHeight(0))
        self.tblTotal = TableTimeTotal(self.account, self.year, self.tblTime.columns[8:])
        self.tblTotal.setFixedHeight(self.tblHeader.rowHeight(0))

    def __scrollBar__(self):
        def verScrTimeChange(value):
            self.verScrBusiness.setValue(value)
        self.verScrBusiness = self.tblBusiness.verticalScrollBar()
        self.verScrTime = self.tblTime.verticalScrollBar()
        self.verScrTime.valueChanged.connect(verScrTimeChange)

        def horScrTimeChange(value):
            self.horScrTotal.setValue(value)
        self.horScrTotal = self.tblTotal.horizontalScrollBar()
        self.horScrTime = self.tblTime.horizontalScrollBar()
        self.horScrTime.valueChanged.connect(horScrTimeChange)

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnSave)
        layoutBtn.addWidget(self.btnExcel)
        layoutBtn.addWidget(QLabel(''), 10)
        layoutTop = QHBoxLayout()
        layoutTop.addWidget(self.tblHeader)
        layoutTop.addWidget(self.tblTotal)
        layoutBottom = QHBoxLayout()
        layoutBottom.addWidget(self.tblBusiness)
        layoutBottom.addWidget(self.tblTime)
        layoutTbl = QVBoxLayout()
        layoutTbl.addLayout(layoutTop)
        layoutTbl.addLayout(layoutBottom)
        layoutTbl.addWidget(self.horScrTime)
        layoutScr = QHBoxLayout()
        layoutScr.addLayout(layoutTbl)
        layoutScr.addWidget(self.verScrTime)
        layout = QVBoxLayout()
        layout.addLayout(layoutBtn)
        layout.addLayout(layoutScr)
        self.setLayout(layout)

    def __setEvent__(self):
        def tblTimeCellChange(_, col):
            try:
                values = []
                for row in range(self.tblTime.rowCount()):
                    value = self.tblTime.item(row, col).text()
                    try:
                        value = float(value)
                    except:
                        value = 0.0
                    values.append(value)
                value = returnTranValue(sum(values))
                self.tblTotal.cellWidget(0, col-8).setText(str(value))
            except Exception as e:
                print(e)
        self.tblTime.cellChanged.connect(tblTimeCellChange)
