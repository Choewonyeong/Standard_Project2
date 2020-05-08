from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from Setting import Path
from Component.Dialog.DialogUserSelf import DialogUserSelf
from Component.Dock.DockUserTime import DockUserTime
from Component.Dock.DockInquiryUser import DockInquiryUser
from Component.Dock.DockInquiryTimePerUser import DockInquiryTimePerUser
from Component.Dock.DockInquiryTimePerBusiness import DockTotalTimePerBusiness
from Component.Dock.DockAdminUser import DockAdminUser
from Component.Dock.DockAdminBusiness import DockAdminBusiness
from Component.Dock.DockCreateDatabase import DockCreateDatabase
from Component.Dock.DockSettingDatabase import DockSettingDatabase
from Design import Style


class Windows(QWidget):
    def __init__(self, userName, author):
        QWidget.__init__(self)
        self.userName = userName
        self.author = author
        self.__setting__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.showMaximized()
        self.setWindowTitle('화재안전팀 시간관리 프로그램 - (주)스탠더드시험연구소')
        self.setWindowIcon(QIcon(Path.icon))

    def __variables__(self):
        self.itemMainText = [self.userName,
                             '조회',
                             '관리자']
        self.itemMainIcon = [Path.user,
                             Path.people,
                             Path.setting]
        self.itemSubText = ['개인 정보 관리',  # 0
                            '시간 정보 입력',  # 1
                            '회원 정보 조회',  # 2
                            '연도별 시간 집계 현황',  # 3
                            '사업별 시간 집계 현황',  # 4
                            '회원 정보 관리',  # 5
                            '사업 정보 관리',  # 6
                            '데이터베이스 생성',  # 7
                            '데이터베이스 관리']  # 8
        self.currentTabs = []

    def __component__(self):
        self.__lstMain__()
        self.__lstSubUser__()
        self.__lstSubInquiry__()
        self.__lstSubAdmin__()
        self.__tabDock__()
        self.__layout__()

    def __lstMain__(self):
        self.lstMain = QListWidget(self)
        self.lstMain.setStyleSheet(Style.ListWidget_Main)
        self.lstMain.setFixedWidth(120)
        self.lstMain.itemClicked.connect(self.lstMainClick)
        for idx, (text, path) in enumerate(zip(self.itemMainText, self.itemMainIcon)):
            item = QListWidgetItem(text)
            item.setIcon(QIcon(path))
            if idx == 2:
                if text == self.author:
                    self.lstMain.addItem(item)
                else:
                    pass
            else:
                self.lstMain.addItem(item)

        self.lstMain.horizontalScrollBar().setVisible(False)
        self.lstMain.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def __lstSubAllHide__(self):
        self.lstSubUser.setVisible(False)
        self.lstSubInquiry.setVisible(False)
        self.lstSubAdmin.setVisible(False)

    def lstMainClick(self, item):
        text = item.text()
        self.__lstSubAllHide__()
        if text == self.itemMainText[0]:
            if self.lstSubUserValue == 0:
                self.lstSubUserValue = 1
                self.lstSubInquiryValue = 0
                self.lstSubAdminValue = 0
                self.lstSubUser.setVisible(True)
                self.lstSubAdmin.setVisible(False)
                self.lstSubInquiry.setVisible(False)
            elif self.lstSubUserValue == 1:
                self.lstSubUserValue = 0
                self.lstSubUser.setVisible(False)
        if text == self.itemMainText[1]:
            if self.lstSubInquiryValue == 0:
                self.lstSubUserValue = 0
                self.lstSubInquiryValue = 1
                self.lstSubAdminValue = 0
                self.lstSubUser.setVisible(False)
                self.lstSubAdmin.setVisible(False)
                self.lstSubInquiry.setVisible(True)
            elif self.lstSubInquiryValue == 1:
                self.lstSubInquiryValue = 0
                self.lstSubInquiry.setVisible(False)
        if text == self.itemMainText[2]:
            if self.lstSubAdminValue == 0:
                self.lstSubUserValue = 0
                self.lstSubInquiryValue = 0
                self.lstSubAdminValue = 1
                self.lstSubUser.setVisible(False)
                self.lstSubAdmin.setVisible(True)
                self.lstSubInquiry.setVisible(False)
            elif self.lstSubAdminValue == 1:
                self.lstSubAdminValue = 0
                self.lstSubAdmin.setVisible(False)

    def __lstSubUser__(self):
        itemText = self.itemSubText[:2]
        self.lstSubUserValue = 0
        self.lstSubUser = QListWidget()
        self.lstSubUser.setStyleSheet(Style.ListWidget_Sub)
        self.lstSubUser.setFixedWidth(150)
        self.lstSubUser.itemClicked.connect(self.lstSubClick)
        self.lstSubUser.setVisible(False)
        for text in itemText:
            item = QListWidgetItem(text)
            self.lstSubUser.addItem(item)

    def __lstSubInquiry__(self):
        itemText = self.itemSubText[2:5]
        self.lstSubInquiryValue = 0
        self.lstSubInquiry = QListWidget()
        self.lstSubInquiry.setStyleSheet(Style.ListWidget_Sub)
        self.lstSubInquiry.setFixedWidth(150)
        self.lstSubInquiry.itemClicked.connect(self.lstSubClick)
        self.lstSubInquiry.setVisible(False)
        for text in itemText:
            item = QListWidgetItem(text)
            self.lstSubInquiry.addItem(item)

    def __lstSubAdmin__(self):
        itemText = self.itemSubText[5:]
        self.lstSubAdminValue = 0
        self.lstSubAdmin = QListWidget()
        self.lstSubAdmin.setStyleSheet(Style.ListWidget_Sub)
        self.lstSubAdmin.setFixedWidth(150)
        self.lstSubAdmin.itemClicked.connect(self.lstSubClick)
        self.lstSubAdmin.setVisible(False)
        for text in itemText:
            item = QListWidgetItem(text)
            self.lstSubAdmin.addItem(item)

    def lstSubClick(self, item):
        text = item.text()
        tabCounts = self.tabDock.count()
        if text in self.currentTabs:
            self.tabDock.setCurrentIndex(self.currentTabs.index(text))
        elif text == self.itemSubText[0]:
            dig = DialogUserSelf(self.userName, self)
            dig.setWindowTitle(text)
            dig.setWindowIcon(QIcon(Path.icon))
            dig.exec_()
        elif text == self.itemSubText[1]:
            dock = DockUserTime(self.userName, self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[2]:
            dock = DockInquiryUser(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[3]:
            dock = DockInquiryTimePerUser(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[4]:
            dock = DockTotalTimePerBusiness(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[5]:
            dock = DockAdminUser(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[6]:
            dock = DockAdminBusiness(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[7]:
            dock = DockCreateDatabase(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        elif text == self.itemSubText[8]:
            dock = DockSettingDatabase(self)
            dock.setWindowTitle(text)
            self.tabDock.addTab(dock, text)
            self.currentTabs.append(text)
        self.tabDock.setCurrentIndex(tabCounts)

    def __tabDock__(self):
        self.tabDock = QTabWidget()
        self.tabDock.setTabsClosable(True)
        self.tabDock.tabCloseRequested.connect(self.tabDockCloseTab)
        self.tabDock.tabBarClicked.connect(self.tabDockTabBarClick)

    def tabDockCloseTab(self, idx):
        tabText = self.tabDock.tabText(idx)
        self.tabDock.removeTab(idx)
        self.currentTabs.remove(tabText)

    def tabDockTabBarClick(self, idx):
        dock = self.tabDock.widget(idx)
        dock.refresh()

    def __layout__(self):
        layout = QHBoxLayout(self)
        layout.addWidget(self.lstMain, 0)
        layout.addWidget(self.lstSubUser, 0)
        layout.addWidget(self.lstSubInquiry, 0)
        layout.addWidget(self.lstSubAdmin, 0)
        layout.addWidget(self.tabDock, 10)
        self.setLayout(layout)
        pixmap = QPixmap(Path.logo)
        lblLogo = QLabel(self)
        lblLogo.setPixmap(pixmap)
        lblLogo.setAlignment(Qt.AlignCenter)
        lblLogo.setGeometry(0, 0, 400, 300)


