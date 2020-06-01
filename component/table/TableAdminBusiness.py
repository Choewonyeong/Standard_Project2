from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from material import FilterComboBox
from connector.connBusiness import connBusiness
from material import TableLineEdit
from material import TableComboBox
from material import BtnTableBusinessDelete


class TableAdminBusiness(QTableWidget):
    def __init__(self, widget):
        QTableWidget.__init__(self)
        self.widget = widget
        self.__connector__()
        self.__variables__()
        self.__setting__()
        self.__setFilter__()
        self.__setData__()

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
        self.setRowHeight(0, 20)
        for idx, header in enumerate(self.columns):
            if header in ['번호', '수정한날짜', '설정']:
                item = QTableWidgetItem('')
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(0, idx, item)
            else:
                items = self.dataFrame[header].tolist()
                items.remove(items[0])
                items.remove(items[-1])
                items = ['필터'] + list(tuple(set(items)))
                FilterComboBox(idx, items, self)

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row+1)
            for col, data in enumerate(lst):
                data = str(data)
                item = QTableWidgetItem(data)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row+1, col, item)
                if col in [1, 2, 4, 5, 10, 11, 12]:
                    obj = TableLineEdit(row+1, col, data, self)
                    self.objects.append(obj)
                elif col == 3:
                    obj = TableComboBox(row+1, col, ['기술', '연구', '국책', '일반', '기타'], data, self)
                    self.objects.append(obj)
                elif col in [6, 7]:
                    obj = TableLineEdit(row+1, col, data, self, option='dateFormat')
                    obj.textEdited.connect(self.TableLineEditChange)
                    self.objects.append(obj)
                elif col == 8:
                    obj = TableLineEdit(row+1, col, data, self, option='disable')
                    self.objects.append(obj)
                elif col == 9:
                    obj = TableLineEdit(row+1, col, data, self, option='dateFormat')
                    self.objects.append(obj)
                elif col == 13:
                    obj = TableLineEdit(row+1, col, data, self, option='moneyFormat')
                    self.objects.append(obj)
                elif col == 14:
                    obj = TableComboBox(row+1, col, ['수주', '진행', '중단', '준공', 'A/S'], data, self)
                    self.objects.append(obj)
            col = len(self.columns)-1
            btn = BtnTableBusinessDelete(row+1, col, '삭제', self)
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
            if self.cellWidget(0, col).currentText() == '필터':
                self.Show()
            elif col in [3, 14] and self.cellWidget(row, col).currentText() != filterText:
                self.hideRow(row)
            elif col not in [3, 14] and self.cellWidget(row, col).text() != filterText:
                self.hideRow(row)