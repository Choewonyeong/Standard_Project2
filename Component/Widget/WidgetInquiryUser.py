from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from Connector.ConnUser import ConnUser
from Design import Style
from Design import Color
from pandas import ExcelWriter


class WidgetInquiryUser(QWidget):
    def __init__(self, dock=None):
        QWidget.__init__(self)
        self.dock = dock
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connUser = ConnUser()

    def __variables__(self):
        self.columnsUser, self.dfUser = self.connUser.ColumnAndDfUser()

    def __component__(self):
        self.__btnSave__()
        self.__table__()
        self.__layout__()

    def __btnSave__(self):
        btnSave = QPushButton('엑셀로 저장')
        btnSave.setStyleSheet(Style.PushButton_Excel)
        btnSave.setShortcut('Ctrl+S')
        btnSave.clicked.connect(self.btnSaveClick)
        layout = QHBoxLayout()
        layout.addWidget(btnSave)
        layout.addWidget(QLabel(), 10)
        self.btnGroup = QGroupBox()
        self.btnGroup.setLayout(layout)

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption='엑셀로 내보내기', directory='', filter='*.xlsx')[0]
        if filePath != '':
            with ExcelWriter(filePath) as writer:
                _, df = self.connUser.ColumnAndDfUser()
                for col in [0, 5, 14, 15, 16]:
                    del df[self.columnsUser[col]]
                df.to_excel(writer, sheet_name='회원 정보(일반)', index=False)
                writer.close()

    def __table__(self):
        self.tblUser = QTableWidget()
        self.tblUser.setStyleSheet(Style.Table_Standard)
        self.tblUser.setRowCount(0)
        self.tblUser.setColumnCount(len(self.columnsUser))
        self.tblUser.setHorizontalHeaderLabels(self.columnsUser)
        for row, lst in enumerate(self.dfUser.values):
            self.tblUser.insertRow(row)
            self.tblUser.setRowHeight(row, 50)
            for col, data in enumerate(lst):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEditable)
                if row != 0 and row % 2 == 1:
                    item.setBackground(Color.AlternateRowColor)
                self.tblUser.setItem(row, col, item)
        self.tblUser.resizeColumnsToContents()
        self.tblUser.verticalHeader().setVisible(False)
        for col in [0, 5, 14, 15, 16]:
            self.tblUser.hideColumn(col)

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnGroup)
        layout.addWidget(self.tblUser)
        self.setLayout(layout)
