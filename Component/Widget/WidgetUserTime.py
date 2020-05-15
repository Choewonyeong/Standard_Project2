from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from Connector.ConnMain import ConnMain
from Component.Table.TableTimeBusiness import TableTimeBusiness
from Component.Table.TableTimeTime import TableTimeTime
from Component.Table.TableTimeHeader import TableTimeHeader
from Component.Table.TableTimeTotal import TableTimeTotal
from Component.Method.method import valueTransferBoxToInt
from datetime import datetime
from pandas import ExcelWriter
from Design import Style
from Design import Color


class WidgetUserTime(QWidget):
    def __init__(self, userName, dock=None):
        QWidget.__init__(self)
        self.userName = userName
        self.dock = dock
        self.__variables__()
        self.__component__()

    def __variables__(self):
        today = datetime.today()
        self.year = today.strftime("%Y")

    def __tables__(self):
        self.tblBusiness = TableTimeBusiness(self.userName, self.year, self)
        self.alternateRows = self.tblBusiness.alternateRows
        self.tblTime = TableTimeTime(self.userName, self.year, self.alternateRows, self)
        self.tblTotal = TableTimeTotal(self.userName, self.year, self)
        width = 0
        for col in range(1, 4):
            width += self.tblBusiness.columnWidth(col)
        height = self.tblTotal.height()
        self.tblHeader = TableTimeHeader(self.userName, self.year, width, height, self)

    def __component__(self):
        self.__tables__()
        self.__cbxMainFilter__()
        self.__cbxSubFilter__()
        self.__btnSave__()
        self.__btnDelete__()
        self.__btnToday__()
        self.__cbxGroup__()
        self.__connectEvent__()
        self.__scrollBar__()
        self.__layout__()

    def __cbxMainFilter__(self):
        self.cbxMainFilter = QComboBox()
        self.cbxMainFilter.setStyleSheet(Style.ComboBox_OutTable)
        self.cbxMainFilter.addItems(['필터', '분기별', '월별'])
        self.cbxMainFilter.currentTextChanged.connect(self.cbxMainFilterChange)

    def cbxMainFilterChange(self, text):
        self.cbxSubFilter.clear()
        if text == '필터':
            self.cbxSubFilter.addItem('전체')
        if text == '분기별':
            items = [f"{q}분기" for q in range(1, 5)]
            self.cbxSubFilter.addItem('전체')
            self.cbxSubFilter.addItems(items)
            self.cbxSubFilter.currentTextChanged.connect(self.cbxSubFilterChange)
        if text == '월별':
            items = [f"0{month}월" if month < 10 else f"{month}월" for month in range(1, 13)]
            self.cbxSubFilter.addItem('전체')
            self.cbxSubFilter.addItems(items)
            self.cbxSubFilter.currentTextChanged.connect(self.cbxSubFilterChange)

    def __cbxSubFilter__(self):
        self.cbxSubFilter = QComboBox()
        self.cbxSubFilter.setStyleSheet(Style.ComboBox_OutTable)
        self.cbxSubFilter.addItem('전체')

    def __tblAllColumnShow__(self):
        for col in range(5, self.tblTime.columnCount()):
            self.tblTime.showColumn(col)

    def __tblAllColumnHide__(self):
        for col in range(5, self.tblTime.columnCount()):
            self.tblTime.hideColumn(col)

    def cbxSubFilterChange(self, text):
        try:
            if text == '전체':
                self.__tblAllColumnShow__()
            elif text != '전체' and self.cbxMainFilter.currentText() == '월별':
                self.__tblAllColumnHide__()
                for col in range(5, self.tblTime.columnCount()):
                    horizontalHeaderItem = self.tblTime.horizontalHeaderItem(col).text()
                    if f"{text[:2]}/" in horizontalHeaderItem:
                        self.tblTime.showColumn(col)
            elif text != '전체' and self.cbxMainFilter.currentText() == '분기별':
                quarter = int(text[0])
                months = [f"0{month}/" if month < 10 else f"{month}/" for month in range(3*quarter-2, 3*quarter+1)]
                self.__tblAllColumnHide__()
                for col in range(5, self.tblTime.columnCount()):
                    horizontalHeaderItem = self.tblTime.horizontalHeaderItem(col).text()
                    for month in months:
                        if month in horizontalHeaderItem:
                            self.tblTime.showColumn(col)
        except Exception as e:
            print(e)

    def __btnSave__(self):
        self.btnSave = QPushButton('엑셀로 저장')
        self.btnSave.setStyleSheet(Style.PushButton_Excel)
        self.btnSave.setShortcut('Ctrl+S')
        self.btnSave.clicked.connect(self.btnSaveClick)

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption='엑셀로 내보내기', directory='', filter='*.xlsx')[0]
        if filePath != '':
            with ExcelWriter(filePath) as writer:
                connMain = ConnMain()
                _, df = connMain.ColumnAndDfTimeWhole(self.year, self.userName)
                del df['성명']
                df.to_excel(writer, sheet_name=f'{self.userName}-시간정보', index=False)
                writer.close()

    def __btnToday__(self):
        self.todayColumn = self.tblTime.todayColumn
        self.btnToday = QPushButton('오늘')
        self.btnToday.setStyleSheet(Style.PushButton_Tools)
        self.btnToday.clicked.connect(self.btnTodayClick)

    def btnTodayClick(self):
        self.tblTime.setCurrentCell(0, len(self.tblTime.columnWhole)-1)
        self.tblTime.setCurrentCell(0, self.todayColumn)

    def __btnDelete__(self):
        self.btnDelete = QPushButton('')
        self.btnDelete.setStyleSheet(Style.PushButton_Hide)
        self.btnDelete.setShortcut('Del')
        self.btnDelete.clicked.connect(self.btnDeleteClick)

    def btnDeleteClick(self):
        row = self.tblTime.currentRow()
        col = self.tblTime.currentColumn()
        item = QTableWidgetItem('')
        item.setTextAlignment(Qt.AlignCenter)
        if row in self.tblBusiness.alternateRows:
            item.setBackground(Color.AlternateRowColor)
        self.tblTime.setItem(row, col, item)

    def __cbxGroup__(self):
        layoutCbx = QHBoxLayout()
        layoutCbx.addWidget(self.cbxMainFilter)
        layoutCbx.addWidget(self.cbxSubFilter)
        layoutCbx.addWidget(self.btnSave)
        layoutCbx.addWidget(self.btnToday)
        layoutCbx.addWidget(QLabel(''), 10)
        layoutCbx.addWidget(self.btnDelete)
        self.cbxGroup = QGroupBox()
        self.cbxGroup.setLayout(layoutCbx)

    def __connectEvent__(self):
        self.tblTime.cellChanged.connect(self.tblTimeCellChange)

    def tblTimeCellChange(self, row, col):
        rows = self.tblTime.rowCount()
        values = []
        for row in range(0, rows):
            value = self.tblTime.item(row, col).text()
            value = valueTransferBoxToInt(value)
            values.append(value)
        total = sum(values)
        if total == 0:
            total = ''
        item = QTableWidgetItem(str(total))
        item.setTextAlignment(Qt.AlignCenter)
        item.setFlags(Qt.ItemIsEditable)
        if row in self.tblBusiness.alternateRows:
            item.setBackground(Color.AlternateRowColor)
        self.tblTotal.setItem(0, col, item)

    def __scrollBar__(self):
        self.scrVerticalTime = self.tblTime.verticalScrollBar()
        self.scrVerticalTime.valueChanged.connect(self.SyncVerticalScrollBar)
        self.scrVerticalBusiness = self.tblBusiness.verticalScrollBar()
        self.scrVerticalBusiness.valueChanged.connect(self.NoChangeVerticalScrollBar)
        self.scrHorizonTime = self.tblTime.horizontalScrollBar()
        self.scrHorizonTime.valueChanged.connect(self.SyncHorizontalScrollBar)
        self.scrHorizonTotal = self.tblTotal.horizontalScrollBar()

    def SyncVerticalScrollBar(self, value):
        self.scrVerticalBusiness.setValue(value)

    def NoChangeVerticalScrollBar(self, value):
        valueTime = self.scrVerticalTime.value()
        self.scrVerticalBusiness.setValue(valueTime)

    def SyncHorizontalScrollBar(self, value):
        self.scrHorizonTotal.setValue(value)

    def __layout__(self):
        layoutLeft = QVBoxLayout()
        layoutLeft.addWidget(self.tblHeader)
        layoutLeft.addWidget(self.tblBusiness)
        layoutRight = QVBoxLayout()
        layoutRight.addWidget(self.tblTotal)
        layoutRight.addWidget(self.tblTime)
        layoutTbl = QHBoxLayout()
        layoutTbl.addLayout(layoutLeft)
        layoutTbl.addLayout(layoutRight)
        layoutTbl.addWidget(self.scrVerticalTime)
        layout = QVBoxLayout()
        layout.addWidget(self.cbxGroup)
        layout.addLayout(layoutTbl)
        layout.addWidget(self.scrHorizonTime)
        self.setLayout(layout)
