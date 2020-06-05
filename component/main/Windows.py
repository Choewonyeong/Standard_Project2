from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from connector.connUser import connUser
from component.dialog.DialogUserSelf import DialogUserSelf
from component.dialog.DialogMassage import DialogMassage
from component.main.MainUserTime import MainUserTime
from component.main.MainAdminBusiness import MainAdminBusiness
from component.main.MainAdminUser import MainAdminUser
from component.main.MainInquiryUser import MainInquiryUser
from component.main.MainNewUser import MainNewUser
from component.main.MainDatabase import MainDatabase
from component.main.MainTotalPerYear import MainTotalPerYear
from component.main.MainTotalPerUser import MainTotalPerUser
from datetime import date
import setting
from material.ListWidget import LstMain, LstSub


class Windows(QWidget):
    CURRENT_YEAR = str(date.today().year)
    TIME_YEAR = str(date.today().year)
    DB_YEAR = str(date.today().year)
    TOTAL_YEAR = str(date.today().year)

    def __init__(self, account, author, app, dig):
        QWidget.__init__(self)
        self.account = account
        self.author = author
        self.app = app
        self.dig = dig
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
        if self.author != "관리자":
            self.itemMain.remove('관리')
        self.itemUser = ['개인정보', '시간관리']
        self.itemInquiry = ['부서원 정보 조회', '연도별시간집계', '부서원별시간집계']
        self.itemAdmin = ['회원가입 신청 현황', '부서원 정보 관리', '사업 정보 관리', '데이터베이스 관리']
        self.valueUser = False
        self.valueInquiry = False
        self.valueAdmin = False
        self.currentTabs = []

    def __component__(self):
        self.__listWidget__()
        self.__tab__()
        self.__layout__()

    def __listWidget__(self):
        def lstMainItemClick(item):
            menu = item.text()
            if menu == self.name and not self.valueUser:
                self.lstUser.setVisible(True)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(False)
                self.valueUser = True
                self.valueInquiry = False
                self.valueAdmin = False
            elif menu == '조회' and not self.valueInquiry:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(True)
                self.lstAdmin.setVisible(False)
                self.valueUser = False
                self.valueInquiry = True
                self.valueAdmin = False
            elif menu == '관리' and not self.valueAdmin:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(True)
                self.valueUser = False
                self.valueInquiry = False
                self.valueAdmin = True
            elif menu == '로그아웃':
                mgs = DialogMassage('변경사항을 저장하셨나요?', True)
                if mgs.value:
                    self.close()
                    self.dig.exec_()
            else:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(False)
                self.valueUser = False
                self.valueInquiry = False
                self.valueAdmin = False
        self.lstMain = LstMain(self.itemMain, lstMainItemClick)

        def lstUserItemClick(item):
            menu = item.text()
            if menu == self.itemUser[0]:
                DialogUserSelf(self.account)
            # 시간관리 -> 완료 : 새로고침 기능만 넣으면 됨(근데 로딩 너무 느림 : 로직 확인 필요)
            elif menu == self.itemUser[1] and menu not in self.currentTabs:
                self.tab.addTab(MainUserTime(self), menu)
                self.currentTabs.append(menu)
                self.tab.setCurrentIndex(self.currentTabs.index(menu))
            else:
                self.tab.setCurrentIndex(self.currentTabs.index(menu))
        self.lstUser = LstSub(self.itemUser, lstUserItemClick)

        def lstInquiryItemClick(item):
            menu = item.text()
            # 부서원 정보 조회 -> 완료 : 새로고침 기능만 넣으면 됨
            if menu == self.itemInquiry[0] and menu not in self.currentTabs:
                self.tab.addTab(MainInquiryUser(self), menu)
                self.currentTabs.append(menu)
                self.tab.setCurrentIndex(self.currentTabs.index(menu))
            # 연도별시간집계 -> 완료 : 새로고침 기능만 넣으면 됨
            elif menu == self.itemInquiry[1] and menu not in self.currentTabs:
                self.tab.addTab(MainTotalPerYear(self), menu)
                self.currentTabs.append(menu)
                self.tab.setCurrentIndex(self.currentTabs.index(menu))
            # 부서원별시간집계 -> 완료 : 새로고침 기능만 넣으면 됨
            elif menu == self.itemInquiry[2] and menu not in self.currentTabs:
                try:
                    self.tab.addTab(MainTotalPerUser(self), menu)
                    self.currentTabs.append(menu)
                    self.tab.setCurrentIndex(self.currentTabs.index(menu))
                except Exception as e:
                    print(e)
            else:
                self.tab.setCurrentIndex(self.currentTabs.index(menu))
        self.lstInquiry = LstSub(self.itemInquiry, lstInquiryItemClick)

        def lstAdminItemClick(item):
            try:
                menu = item.text()
                # 회원가입 신청 현황 -> 새로고침 기능만 추가하면 됨
                if menu == self.itemAdmin[0] and menu not in self.currentTabs:
                    widget = MainNewUser(self)
                    if len(widget.dataFrame):
                        self.tab.addTab(widget, menu)
                        self.currentTabs.append(menu)
                    else:
                        DialogMassage('신청 대상이 없습니다.')
                # 부서원 정보 관리 -> 새로고침 기능만 추가하면 됨
                elif menu == self.itemAdmin[1] and menu not in self.currentTabs:
                    self.tab.addTab(MainAdminUser(self), menu)
                    self.currentTabs.append(menu)
                # 사업 정보 관리 -> 내일 수정, 디자인, 기능 추가(엑셀) 할 것
                elif menu == self.itemAdmin[2] and menu not in self.currentTabs:
                    self.tab.addTab(MainAdminBusiness(self), menu)
                    self.currentTabs.append(menu)
                # 데이터베이스 관리 -> 내일 수정, 디자인, 기능 추가(엑셀) 할 것
                elif menu == self.itemAdmin[3] and menu not in self.currentTabs:
                    self.tab.addTab(MainDatabase(self), menu)
                    self.currentTabs.append(menu)
                else:
                    self.tab.setCurrentIndex(self.currentTabs.index(menu))
            except Exception as e:
                print(e)
        self.lstAdmin = LstSub(self.itemAdmin, lstAdminItemClick)

    def __tab__(self):
        self.tab = QTabWidget()
        self.tab.tabBar().setVisible(False)

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
            menu = self.currentTabs[idx]
            self.tab.removeTab(idx)
            if menu == self.itemUser[0]:
                pass
            elif menu == self.itemUser[1]:
                self.tab.insertTab(idx, MainUserTime(self), menu)
            elif menu == self.itemInquiry[0]:
                self.tab.insertTab(idx, MainInquiryUser(self), menu)
            elif menu == self.itemInquiry[1]:
                self.tab.insertTab(idx, MainTotalPerYear(self), menu)
            elif menu == self.itemInquiry[2]:
                self.tab.insertTab(idx, MainTotalPerUser(self), menu)
            elif menu == self.itemAdmin[0]:
                self.tab.insertTab(idx, MainNewUser(self), menu)
            elif menu == self.itemAdmin[1]:
                self.tab.insertTab(idx, MainAdminUser(self), menu)
            elif menu == self.itemAdmin[2]:
                self.tab.insertTab(idx, MainAdminBusiness(self), menu)
            elif menu == self.itemAdmin[3]:
                self.tab.insertTab(idx, MainDatabase(self), menu)
        except Exception as e:
            print(e)

    def refreshAdminDB(self):
        menu = self.itemAdmin[3]
        idx = self.currentTabs.index(menu)
        self.tab.removeTab(idx)
        self.tab.insertTab(idx, MainDatabase(self), menu)
        self.tab.setCurrentIndex(idx)

    def refreshTotalPerUser(self):
        menu = self.itemInquiry[2]
        idx = self.currentTabs.index(menu)
        self.tab.removeTab(idx)
        self.tab.insertTab(idx, MainTotalPerUser(self), menu)
        self.tab.setCurrentIndex(idx)
