from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from connector.connUser import connUser
from component.main.Login import Login
from component.material.WindowMainList import WindowMainList
from component.material.WindowSubList import WindowSubList
from component.dialog.DialogUserSelf import DialogUserSelf
from component.dialog.DialogMassage import DialogMassage
from component.dialog.DialogNewUser import DialogNewUser
from component.dialog.DialogInquiryUser import DialogInquiryUser
from component.dialog.DialogAdminUser import DialogAdminUser
from component.dialog.DialogAdminBusiness import DialogAdminBusiness
from component.groupBox.GroupBoxAdminBusiness import GroupBoxAdminBusiness
from component.groupBox.GroupBoxAdminUser import GroupBoxAdminUser
from component.groupBox.GroupBoxInquiryUser import GroupBoxInquiryUser
from component.groupBox.GroupBoxNewUser import GroupBoxNewUser
import setting


class Windows(QWidget):
    def __init__(self, account, author, app):
        QWidget.__init__(self)
        self.account = account
        self.author = author
        self.app = app
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setWindowTitle('화재안전팀 시간관리 프로그램 - (주)스탠더드시험연구소')
        self.setWindowIcon(QIcon(setting.iconIcon))
        self.showMaximized()
        background = QPalette()
        background.setBrush(10, QBrush(QColor(255, 255, 255)))
        self.setPalette(background)

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.lstMainIterator = []
        self.name = self.connUser.returnName(self.account)
        self.itemMain = [self.name, '조회', '관리', '로그아웃']
        self.itemUser = ['개인정보', '시간관리']
        self.itemInquiry = ['부서원 정보 조회', '연도별시간집계', '사업별시간집계']
        self.itemAdmin = ['회원가입 신청 현황', '부서원 정보 관리', '사업 정보 관리', '데이터베이스 관리']
        self.valueUser = False
        self.valueInquiry = False
        self.valueAdmin = False
        self.currentTab = []
        self.currentIdx = 0

    def __component__(self):
        self.__listWidget__()
        self.__tab__()
        self.__layout__()

    def __listWidget__(self):
        def lstMainItemClick(item):
            menu = item.text()
            if menu == self.itemMain[0] and not self.valueUser:
                self.lstUser.setVisible(True)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(False)
                self.valueUser = True
                self.valueInquiry = False
                self.valueAdmin = False
            elif menu == self.itemMain[1] and not self.valueInquiry:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(True)
                self.lstAdmin.setVisible(False)
                self.valueUser = False
                self.valueInquiry = True
                self.valueAdmin = False
            elif menu == self.itemMain[2] and not self.valueAdmin:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(True)
                self.valueUser = False
                self.valueInquiry = False
                self.valueAdmin = True
            elif menu == self.itemMain[3]:
                mgs = DialogMassage('변경사항을 저장하셨나요?', True)
                if mgs.value:
                    self.close()
                    dig = Login(self.app)
                    dig.exec_()
            else:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(False)
                self.valueUser = False
                self.valueInquiry = False
                self.valueAdmin = False
        self.lstMain = WindowMainList(self.itemMain)
        self.lstMain.itemClicked.connect(lstMainItemClick)

        def lstUserItemClick(item):
            menu = item.text()
            if menu == self.itemUser[0]:
                dig = DialogUserSelf(self.account)
                dig.exec_()
                pass
            elif menu == self.itemUser[1]:
                pass
            else:
                self.tab.setCurrentIndex(self.currentTab.index(menu))

        self.lstUser = WindowSubList(self.itemUser)
        self.lstUser.itemClicked.connect(lstUserItemClick)

        def lstInquiryItemClick(item):
            menu = item.text()
            if menu == self.itemInquiry[0] and menu not in self.currentTab:
                self.tab.addTab(GroupBoxInquiryUser(), menu)
                self.currentTab.append(menu)
                self.tab.setCurrentIndex(self.currentIdx)
                self.currentIdx += 1
            elif menu == self.itemInquiry[1]:
                pass
            elif menu == self.itemInquiry[2]:
                pass
            else:
                self.tab.setCurrentIndex(self.currentTab.index(menu))

        self.lstInquiry = WindowSubList(self.itemInquiry)
        self.lstInquiry.itemClicked.connect(lstInquiryItemClick)

        def lstAdminItemClick(item):
            menu = item.text()
            if menu == self.itemAdmin[0] and menu not in self.currentTab:
                DialogNewUser()
                # self.tab.addTab(GroupBoxNewUser(), menu)
                # self.currentTab.append(menu)
                # self.tab.setCurrentIndex(self.currentIdx)
                # self.currentIdx += 1
            elif menu == self.itemAdmin[1] and menu not in self.currentTab:
                self.tab.addTab(GroupBoxAdminUser(), menu)
                self.currentTab.append(menu)
                self.tab.setCurrentIndex(self.currentIdx)
                self.currentIdx += 1
            elif menu == self.itemAdmin[2] and menu not in self.currentTab:
                self.tab.addTab(GroupBoxAdminBusiness(self), menu)
                self.currentTab.append(menu)
                self.tab.setCurrentIndex(self.currentIdx)
                self.currentIdx += 1
            elif menu == self.itemAdmin[3] and menu not in self.currentTab:
                pass
            else:
                self.tab.setCurrentIndex(self.currentTab.index(menu))

        self.lstAdmin = WindowSubList(self.itemAdmin)
        self.lstAdmin.itemClicked.connect(lstAdminItemClick)

    def __tab__(self):
        def tabCloseRequest(idx):
            menu = self.currentTab[idx]
            self.currentTab.remove(menu)
            self.tab.removeTab(idx)
            self.currentIdx -= 1
            if self.currentIdx < 0:
                self.currentIdx = 0
        self.tab = QTabWidget()
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(tabCloseRequest)

        def tabBarClick(idx):
            try:
                menu = self.currentTab[idx]
                self.tab.removeTab(idx)
                if menu == self.itemUser[0]:
                    pass
                elif menu == self.itemUser[1]:
                    pass
                elif menu == self.itemInquiry[0]:
                    self.tab.insertTab(idx, GroupBoxInquiryUser(), menu)
                elif menu == self.itemInquiry[1]:
                    pass
                elif menu == self.itemInquiry[2]:
                    pass
                elif menu == self.itemAdmin[0]:
                    self.tab.insertTab(idx, GroupBoxNewUser(), menu)
                elif menu == self.itemAdmin[1]:
                    self.tab.insertTab(idx, GroupBoxAdminUser(), menu)
                elif menu == self.itemAdmin[2]:
                    self.tab.insertTab(idx, GroupBoxAdminBusiness(self), menu)
                elif menu == self.itemAdmin[3]:
                    pass
            except Exception as e:
                print(e)
        self.tab.tabBarClicked.connect(tabBarClick)

    def __layout__(self):
        layout = QHBoxLayout()
        layout.addWidget(self.lstMain)
        layout.addWidget(self.lstUser)
        layout.addWidget(self.lstInquiry)
        layout.addWidget(self.lstAdmin)
        layout.addWidget(self.tab, 10)
        self.setLayout(layout)

    def refresh(self):
        try:
            idx = self.tab.currentIndex()
            menu = self.currentTab[idx]
            self.tab.removeTab(idx)
            if menu == self.itemUser[0]:
                pass
            elif menu == self.itemUser[1]:
                pass
            elif menu == self.itemInquiry[0]:
                self.tab.insertTab(idx, GroupBoxInquiryUser(), menu)
            elif menu == self.itemInquiry[1]:
                pass
            elif menu == self.itemInquiry[2]:
                pass
            elif menu == self.itemAdmin[0]:
                self.tab.insertTab(idx, GroupBoxNewUser(), menu)
            elif menu == self.itemAdmin[1]:
                self.tab.insertTab(idx, GroupBoxAdminUser(), menu)
            elif menu == self.itemAdmin[2]:
                self.tab.insertTab(idx, GroupBoxAdminBusiness(self), menu)
            elif menu == self.itemAdmin[3]:
                pass
        except Exception as e:
            print(e)
