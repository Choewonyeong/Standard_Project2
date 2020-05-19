from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from connector.connUser import connUser
from component.dialog.DialogUserSelf import DialogUserSelf
from component.dialog.DialogNewUser import DialogNewUser
from component.dialog.DialogInquiryUser import DialogInquiryUser
from component.dialog.DialogAdminUser import DialogAdminUser
import setting


class Windows(QWidget):
    def __init__(self, account, author):
        QWidget.__init__(self)
        self.account = account
        self.author = author
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setWindowTitle('화재안전팀 시간관리 프로그램 - (주)스탠더드시험연구소')
        # self.setWindowIcon(QIcon(setting.iconIcon))
        self.showMaximized()
        background = QPalette()
        background.setBrush(10, QBrush(QColor(255, 255, 255)))
        self.setPalette(background)

    def __connector__(self):
        self.connUser = connUser()

    def __variables__(self):
        self.lstMainIterator = []
        self.name = self.connUser.returnName(self.account)
        self.itemMain = [self.name, '조회', '관리']
        self.itemUser = ['개인정보', '시간관리']
        self.itemInquiry = ['부서원 정보 조회', '연도별시간집계', '사업별시간집계']
        self.itemAdmin = ['회원가입 신청 목록', '부서원 정보 관리', '사업 정보 관리', '데이터베이스 관리']
        # self.mainIcons

    def __component__(self):
        self.__listWidget__()
        self.__tab__()
        self.__layout__()

    def __listWidget__(self):
        def lstMainItemClick(item):
            menu = item.text()
            if menu == self.itemMain[0]:
                self.lstUser.setVisible(True)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(False)
            elif menu == self.itemMain[1]:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(True)
                self.lstAdmin.setVisible(False)
            elif menu == self.itemMain[2]:
                self.lstUser.setVisible(False)
                self.lstInquiry.setVisible(False)
                self.lstAdmin.setVisible(True)
        self.lstMain = QListWidget()
        self.lstMain.addItems(self.itemMain)
        self.lstMain.itemClicked.connect(lstMainItemClick)
        self.lstMain.setFixedWidth(120)

        def lstUserItemClick(item):
            menu = item.text()
            if menu == self.itemUser[0]:
                dig = DialogUserSelf(self.account)
                dig.exec_()
                pass
            elif menu == self.itemUser[1]:
                pass
        self.lstUser = QListWidget(self)
        self.lstUser.setVisible(False)
        self.lstUser.addItems(self.itemUser)
        self.lstUser.itemClicked.connect(lstUserItemClick)
        self.lstUser.setFixedWidth(230)

        def lstInquiryItemClick(item):
            menu = item.text()
            if menu == self.itemInquiry[0]:
                dig = DialogInquiryUser()
                dig.exec_()
            elif menu == self.itemInquiry[1]:
                pass
            elif menu == self.itemInquiry[2]:
                pass
        self.lstInquiry = QListWidget()
        self.lstInquiry.setVisible(False)
        self.lstInquiry.addItems(self.itemInquiry)
        self.lstInquiry.itemClicked.connect(lstInquiryItemClick)
        self.lstInquiry.setFixedWidth(230)

        def lstAdminItemClick(item):
            menu = item.text()
            if menu == self.itemAdmin[0]:
                dig = DialogNewUser()
                dig.exec_()
            elif menu == self.itemAdmin[1]:
                dig = DialogAdminUser()
                dig.exec_()
            elif menu == self.itemAdmin[2]:
                pass
            elif menu == self.itemAdmin[3]:
                pass
        self.lstAdmin = QListWidget()
        self.lstAdmin.setVisible(False)
        self.lstAdmin.addItems(self.itemAdmin)
        self.lstAdmin.itemClicked.connect(lstAdminItemClick)
        self.lstAdmin.setFixedWidth(230)

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
