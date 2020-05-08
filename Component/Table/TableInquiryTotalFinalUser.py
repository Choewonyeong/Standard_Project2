from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from Component.Method.method import valueTransferBoxToWhole
from Design import Style
from Design import Color


class TableInquiryTotalFinalUser(QTableWidget):
    def __init__(self, columnsTotal, dfFinalTotal, widget=None):
        QTableWidget.__init__(self)
        self.columnsTotal = columnsTotal
        self.dfFinalTotal = dfFinalTotal
        self.widget = widget
        self.__component__()

    def __component__(self):
        self.__tblUserFinalTime__()

    def __tblUserFinalTime__(self):
        self.setStyleSheet(Style.Table_Standard)
        self.setRowCount(0)
        self.setColumnCount(len(self.columnsTotal))
        self.setHorizontalHeaderLabels(self.columnsTotal)
        for col in [4, 8, 12, 16, 17]:
            item = QTableWidgetItem(self.columnsTotal[col])
            item.setTextAlignment(Qt.AlignCenter)
            font = QFont()
            font.setBold(True)
            item.setFont(font)
            if col == 17:
                item.setForeground(Color.FinalTotalColumnColor)
            else:
                item.setForeground(Color.SubTotalColumnColor)
            self.setHorizontalHeaderItem(col, item)
        for row, lst in enumerate(self.dfFinalTotal.values):
            self.insertRow(row)
            self.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                value = valueTransferBoxToWhole(data)
                item = QTableWidgetItem(str(value))
                item.setFlags(Qt.ItemIsEditable)
                if col == 0:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                elif col in [4, 8, 12, 16]:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                    item.setForeground(Color.SubTotalColumnColor)
                elif col == 17:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                    item.setForeground(Color.FinalTotalColumnColor)
                if col != 0:
                    item.setTextAlignment(Qt.AlignCenter)
                    self.setColumnWidth(col, 70)
                elif row == len(self.dfFinalTotal)-1:
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setForeground(Color.FinalTotalColumnColor)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.setItem(row, col, item)
        self.resizeColumnToContents(0)
        self.verticalHeader().setVisible(False)

