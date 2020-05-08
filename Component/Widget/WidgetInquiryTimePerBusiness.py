from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGroupBox
from Connector.ConnMain import ConnMain
from Connector.ConnBusiness import ConnBusiness
from Connector.ConnUser import ConnUser
from Component.Table.TableInquiryTimePerBusiness import TableInquiryTimePerBusiness
from Design import Style
from pandas import ExcelWriter


class WidgetInquiryTimePerBusiness(QWidget):
    def __init__(self, dock=None):
        QWidget.__init__(self)
        self.dock = dock
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __connector__(self):
        self.connMain = ConnMain()
        self.connUser = ConnUser()
        self.connBusiness = ConnBusiness()

    def __variables__(self):
        self.currentText = None

    def __component__(self):
        self.__cbxBusinessName__()
        self.__btnSearch__()
        self.__btnSave__()
        self.__cbxGroup__()
        self.__tab__()
        self.__layout__()

    def __cbxBusinessName__(self):
        businessNames = self.connBusiness.ReturnBusinessNames()
        self.cbxBusinessName = QComboBox()
        self.cbxBusinessName.setStyleSheet(Style.ComboBox_OutTable)
        self.cbxBusinessName.addItems(businessNames)

    def __btnSearch__(self):
        self.btnSearch = QPushButton('조회')
        self.btnSearch.setStyleSheet(Style.PushButton_Tools)
        self.btnSearch.clicked.connect(self.btnSearchClick)

    def btnSearchClick(self):
        businessName = self.cbxBusinessName.currentText()
        self.currentText = businessName
        self.tab.clear()
        tblTimeBusiness = TableInquiryTimePerBusiness(businessName, self)
        self.tab.addTab(tblTimeBusiness, businessName)
        tabCounts = self.tab.count()
        if tabCounts > 0:
            self.btnSave.setEnabled(True)

    def __btnSave__(self):
        self.btnSave = QPushButton('엑셀로 저장')
        self.btnSave.setStyleSheet(Style.PushButton_Excel)
        self.btnSave.setShortcut('Ctrl+S')
        self.btnSave.clicked.connect(self.btnSaveClick)
        self.btnSave.setEnabled(False)

    def btnSaveClick(self):
        dig = QFileDialog(self)
        filePath = dig.getSaveFileName(caption='엑셀로 내보내기', directory='', filter='*.xlsx')[0]
        if filePath != '':
            with ExcelWriter(filePath) as writer:
                df = self.tab.widget(0).dfTotal
                df.to_excel(writer, sheet_name=f'{self.tab.tabText(0)}', index=False)
                writer.close()

    def __cbxGroup__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.cbxBusinessName, 3)
        layout.addWidget(self.btnSearch)
        layout.addWidget(self.btnSave)
        layout.addWidget(QLabel(''), 10)
        self.cbxGroup = QGroupBox()
        self.cbxGroup.setLayout(layout)

    def __tab__(self):
        self.tab = QTabWidget()
        self.tab.tabBar().setVisible(False)

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.cbxGroup)
        layout.addWidget(self.tab)
        self.setLayout(layout)
