from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from Connector.ConnMain import ConnMain
from Component.Table.TableCurrentWhole import TableCurrentWhole
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Design import Style
from datetime import datetime


class WidgetSettingDatabase(QWidget):
    def __init__(self, dock):
        QWidget.__init__(self)
        self.dock = dock
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        pass

    def __connector__(self):
        self.connMain = ConnMain()

    def __variables__(self):
        pass

    def __component__(self):
        self.__combobox__()
        self.__button__()
        self.__groupBox__()
        self.__tabSub__()
        self.__layout__()

    def __combobox__(self):
        self.cbxYear = QComboBox()
        self.cbxYear.setStyleSheet(Style.ComboBox_OutTable)
        years = self.connMain.ReturnTables()
        self.cbxYear.addItems(years)
        currentYear = str(datetime.today().year)
        self.cbxYear.setCurrentText(currentYear)
        self.cbxYear.currentTextChanged.connect(self.cbxYearTextChange)
        self.currentYear = self.cbxYear.currentText()

    def cbxYearTextChange(self, text):
        tabCounts = self.tabSub.count()
        currentYear = self.cbxYear.currentText()
        self.tabSub.clear()
        self.tabSub.addTab(TableCurrentWhole(currentYear, self), currentYear)
        self.tabSub.setCurrentIndex(tabCounts)
        self.dock.currentYear = text
        cbxYear = int(text)
        year = datetime.today().year
        if cbxYear <= year:
            self.btnDelete.setEnabled(False)
        else:
            self.btnDelete.setEnabled(True)

    def __button__(self):
        self.btnDelete = QPushButton('삭제')
        self.btnDelete.setStyleSheet(Style.PushButton_Delete)
        self.btnDelete.clicked.connect(self.btnDeleteClick)
        self.btnDelete.setEnabled(False)

    def __groupBox__(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('연도 선택'))
        layout.addWidget(self.cbxYear)
        layout.addWidget(self.btnDelete)
        layout.addWidget(QLabel(''), 10)
        self.btnGroup = QGroupBox()
        self.btnGroup.setLayout(layout)

    def btnDeleteClick(self):
        currentIndex = self.tabSub.currentIndex()
        tabText = self.tabSub.tabText(currentIndex)
        dig = DialogMessageBox('알림', f'{tabText}의 데이터를 삭제합니까?\n삭제한 이후에는 되돌릴 수 없습니다.', True)
        dig.exec_()
        if dig.Yes:
            self.connMain.DropTable(tabText)
            self.currentYear = str(int(self.currentYear)-1)
            self.currentTabText = self.currentYear
            self.refresh()
        else:
            pass

    def refresh(self):
        self.dock.currentYear = self.currentYear
        self.dock.refresh()

    def settingReformat(self):
        self.currentYear = self.dock.currentYear
        self.cbxYear.setCurrentText(self.currentYear)
        self.tabSub.clear()
        self.tabSub.addTab(TableCurrentWhole(self.currentYear, self), self.currentYear)

    def __tabSub__(self):
        self.tabSub = QTabWidget()
        year = self.cbxYear.currentText()
        self.tabSub.addTab(TableCurrentWhole(year, self), year)
        self.currentTabText = year

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.btnGroup)
        layout.addWidget(self.tabSub)
        self.setLayout(layout)
