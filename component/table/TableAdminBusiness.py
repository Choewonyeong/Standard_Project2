from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connBusiness import connBusiness
from material import TableLineEdit
from material import TableComboBox
from material import BtnTableBusinessDelete
from material.ComboBox import CbxFilterInTable, CbxToolInTable
from material.LineEdit import LdtAdminBusinessInTable
from material.PushButton import BtnDeleteInTable


class TableAdminBusiness(QTableWidget):
    def __init__(self, widget):
        QTableWidget.__init__(self)
        self.widget = widget
        print(1)
        self.__connector__()
        print(2)
        self.__variables__()
        print(3)
        self.__setting__()
        print(4)
        self.__setFilter__()
        print(5)
        self.__setData__()
        print(6)

    def __connector__(self):
        self.connBusiness = connBusiness()

    def __variables__(self):
        self.editLog = []
        self.objects = []
        self.columns = self.connBusiness.dataFrameBusiness(column=True)+['설정']
        self.dataFrame = self.connBusiness.dataFrameBusiness()

    def __setting__(self):
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels(self.columns)
        self.verticalHeader().setVisible(False)

    def __setFilter__(self):
        self.insertRow(0)
        for idx, header in enumerate(self.columns):
            if header in ['번호', '수정한날짜', '설정']:
                item = QTableWidgetItem('')
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(0, idx, item)
            else:
                items = self.dataFrame[header].tolist()
                items.remove(items[0])
                items.remove(items[-1])
                items = ['전체'] + list(tuple(set(items)))
                CbxFilterInTable(idx, items, self)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row+1)
            for col, data in enumerate(lst):
                data = str(data)
                item = QTableWidgetItem(data)
                self.setItem(row+1, col, item)
                if col in [1, 2, 4, 5, 10, 11, 12]:
                    widget = LdtAdminBusinessInTable(row+1, col, data, self)
                    self.objects.append(widget)
                elif col == 3:
                    widget = CbxToolInTable(row+1, col, ['기술', '연구', '국책', '일반', '기타'], data, self)
                    self.objects.append(widget)
                elif col in [6, 7]:
                    widget = LdtAdminBusinessInTable(row+1, col, data, self)
                    widget.textEdited.connect(self.TableLineEditChange)
                    self.objects.append(widget)
                elif col == 8:
                    widget = LdtAdminBusinessInTable(row+1, col, data, self)
                    widget.setEnabled(False)
                    self.objects.append(widget)
                elif col == 9:
                    widget = LdtAdminBusinessInTable(row+1, col, data, self)
                    self.objects.append(widget)
                elif col == 13:
                    widget = LdtAdminBusinessInTable(row+1, col, data, self)
                    self.objects.append(widget)
                elif col == 14:
                    widget = CbxToolInTable(row+1, col, ['수주', '진행', '중단', '준공', 'A/S'], data, self)
                    self.objects.append(widget)
            col = len(self.columns)-1
            BtnDeleteInTable('삭제', self, row+1, col)
        self.resizeColumnsToContents()
        self.hideColumn(0)
        self.hideRow(1)
        self.hideRow(len(self.dataFrame))
        self.setColumnWidth(2, 70)
        self.setColumnWidth(8, 50)
        for col in [6, 7, 9]:
            self.setColumnWidth(col, 100)
        for col in [10, 11, 12]:
            self.setColumnWidth(col, 80)

    def TableLineEditChange(self):
        row = self.sender().row
        widgetStart = self.cellWidget(row, 6)
        widgetEnd = self.cellWidget(row, 7)
        widgetTotal = self.cellWidget(row, 8)
        start = widgetStart.text()
        end = widgetEnd.text()
        try:
            start = datetime.strptime(start, "%Y-%m-%d")
            end = datetime.strptime(end, "%Y-%m-%d")
            yearCnt = (end.year - start.year)*12
            monthCnt = end.month - start.month
            totalCnt = yearCnt + monthCnt
            widgetTotal.setText(str(totalCnt))
        except:
            pass

    def Show(self):
        for row in range(2, self.rowCount()-1):
            self.showRow(row)

    def Filter(self, col, filterText):
        self.Show()
        for row in range(1, self.rowCount()):
            if self.cellWidget(0, col).currentText() == '전체':
                self.Show()
            elif col in [3, 14] and self.cellWidget(row, col).currentText() != filterText:
                self.hideRow(row)
            elif col not in [3, 14] and self.cellWidget(row, col).text() != filterText:
                self.hideRow(row)