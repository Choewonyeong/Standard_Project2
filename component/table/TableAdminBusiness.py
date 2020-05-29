from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connBusiness import connBusiness
from component.material.TableLineEdit import TableLineEdit
from component.material.TableComboBox import TableComboBox
from component.material.BtnTableBusinessDelete import BtnTableBusinessDelete


class TableAdminBusiness(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.__connector__()
        self.__variables__()
        self.__setting__()
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

    def __setData__(self):
        for row, lst in enumerate(self.dataFrame.values):
            self.insertRow(row)
            # self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(data)
                item.setFlags(Qt.ItemIsEditable)
                self.setItem(row, col, item)
                if col in [1, 2, 4, 5, 10, 11, 12]:
                    obj = TableLineEdit(row, col, data, self)
                    self.objects.append(obj)
                elif col == 3:
                    obj = TableComboBox(row, col, ['기술', '연구', '국책', '일반', '기타'], data, self)
                    self.objects.append(obj)
                elif col in [6, 7]:
                    obj = TableLineEdit(row, col, data, self, option='dateFormat')
                    obj.textEdited.connect(self.TableLineEditChange)
                    self.objects.append(obj)
                elif col == 8:
                    obj = TableLineEdit(row, col, data, self, option='disable')
                    self.objects.append(obj)
                elif col == 9:
                    obj = TableLineEdit(row, col, data, self, option='dateFormat')
                    self.objects.append(obj)
                elif col == 13:
                    obj = TableLineEdit(row, col, data, self, option='moneyFormat')
                    self.objects.append(obj)
                elif col == 14:
                    obj = TableComboBox(row, col, ['수주', '진행', '중단', '준공', 'A/S'], data, self)
                    self.objects.append(obj)
            col = len(self.columns)-1
            if lst[0] in ['0', '99']:
                BtnTableBusinessDelete(row, col, '삭제', self)
            else:
                BtnTableBusinessDelete(row, col, '삭제', self)
        self.resizeColumnsToContents()
        self.hideColumn(0)
        self.hideRow(0)
        self.hideRow(len(self.dataFrame)-1)
        self.setColumnWidth(2, 70)
        self.setColumnWidth(8, 50)
        for col in [6, 7, 9]:
            self.setColumnWidth(col, 100)
        for col in [10, 11, 12]:
            self.setColumnWidth(col, 80)

    def insertNewBusiness(self, businessInfo):
        row = self.rowCount()
        self.setRowHeight(50, row)
        for col, data in enumerate(businessInfo):
            item = QTableWidgetItem(data)
            item.setFlags(Qt.ItemIsEditable)
            self.setItem(row, col, item)
            if col in [1, 2, 4, 5, 10, 11, 12]:
                obj = TableLineEdit(row, col, data, self)
                self.objects.append(obj)
            elif col == 3:
                TableComboBox(row, col, ['기술', '연구', '국책', '일반', '기타'], data, self)
                self.objects.append(obj)
            elif col in [6, 7]:
                obj = TableLineEdit(row, col, data, self, option='dateFormat')
                obj.textEdited.connect(self.TableLineEditChange)
                self.objects.append(obj)
            elif col == 8:
                obj = TableLineEdit(row, col, data, self, option='disable')
                self.objects.append(obj)
            elif col == 9:
                obj = TableLineEdit(row, col, data, self, option='dateFormat')
                self.objects.append(obj)
            elif col == 13:
                obj = TableLineEdit(row, col, data, self, option='moneyFormat')
                self.objects.append(obj)
            elif col == 14:
                obj = TableComboBox(row, col, ['수주', '진행', '중단', '준공', 'A/S'], data, self)
                self.objects.append(obj)
        col = len(self.columns)-1
        BtnTableBusinessDelete(row, col, '삭제', self)

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
