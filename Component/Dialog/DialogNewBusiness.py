from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from Connector.ConnBusiness import ConnBusiness
from Component.Dialog.DialogMessageBox import DialogMessageBox
from Design import Style
from Setting import Path
from datetime import datetime


class DialogNewBusiness(QDialog):
    def __init__(self, businessNumber, widget=None):
        QDialog.__init__(self)
        self.businessNumber = businessNumber
        self.widget = widget
        self.__setting__()
        self.__variables__()
        self.__connector__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon(Path.icon))
        self.setWindowTitle('신규 사업 등록')
        self.setStyleSheet(Style.Components_Dialog)
        self.setFixedWidth(360)

    def __variables__(self):
        self.objText = ['사업명',
                        '사업코드',
                        '사업형태',
                        '발주처',
                        '사업요약',
                        '시작일',
                        '종료일',
                        '개월수',
                        '보존기간',
                        '사업책임자',
                        'PL',
                        '기술행정',
                        '사업비',
                        '진행상태']

    def __connector__(self):
        self.connBusiness = ConnBusiness()

    def __component__(self):
        self.__lineEdit__()
        self.__button__()
        self.__layout__()

    def __lineEdit__(self):
        self.inputBusinessName = QLineEdit()    # 0 사업명
        self.inputBusinessCode = QLineEdit()    # 1 사업코드
        self.inputForm = QComboBox()            # 2 사업형태
        self.inputForm.addItems(['기술', '연구', '국책', '일반', '기타'])
        self.inputOrder = QLineEdit()           # 3 발주처
        self.inputSummary = QTextEdit()         # 4 사업요약
        self.inputSummary.setFixedHeight(100)
        self.inputStartDate = QLineEdit()       # 5 시작일
        self.inputStartDate.setPlaceholderText('ex) YYYY-MM-DD')
        self.inputStartDate.editingFinished.connect(self.lineEditStartAndFinishDateChange)
        self.inputFinishDate = QLineEdit()      # 6 종료일
        self.inputFinishDate.setPlaceholderText('ex) YYYY-MM-DD')
        self.inputFinishDate.editingFinished.connect(self.lineEditStartAndFinishDateChange)
        self.inputTotalMonth = QLineEdit()      # 7 개월수
        self.inputTotalMonth.setEnabled(False)
        self.inputRetention = QLineEdit()       # 8 보존기간
        self.inputRetention.setPlaceholderText('ex) YYYY-MM-DD')
        self.inputRetention.editingFinished.connect(self.lineEditRetentionDateChange)
        self.inputMaster = QLineEdit()          # 9 사업책임자
        self.inputPL = QLineEdit()              # 10 PL
        self.inputAdministrator = QLineEdit()   # 11 기술행정
        self.inputPrice = QLineEdit()           # 12 사업비
        self.inputPrice.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.inputPrice.textChanged.connect(self.lineEditPriceChange)
        self.inputStatus = QComboBox()          # 13 진행상태
        self.inputStatus.addItems(['진행', '중단', '준공', 'A/S'])
        self.objects = [self.inputBusinessName,
                        self.inputBusinessCode,
                        self.inputForm,
                        self.inputOrder,
                        self.inputSummary,
                        self.inputStartDate,
                        self.inputFinishDate,
                        self.inputTotalMonth,
                        self.inputRetention,
                        self.inputMaster,
                        self.inputPL,
                        self.inputAdministrator,
                        self.inputPrice,
                        self.inputStatus]

    def lineEditPriceChange(self, text):
        try:
            if ',' in text:
                text = int(text.replace(',', ''))
                text = format(text, ',')
                self.inputPrice.setText(text)
        except:
            pass

    def lineEditStartAndFinishDateChange(self):
        startDate = self.inputStartDate.text()
        finishDate = self.inputFinishDate.text()
        try:
            startDate = datetime.strptime(startDate, '%Y-%m-%d')
            finishDate = datetime.strptime(finishDate, '%Y-%m-%d')
            yearCount = (finishDate.year-startDate.year)*12
            monthCount = finishDate.month-startDate.month
            totalMonth = yearCount+monthCount
            self.inputTotalMonth.setText(f'{totalMonth}개월')
        except:
            pass

    def lineEditRetentionDateChange(self):
        try:
            text = self.sender().text()
            date = datetime.strptime(text, '%Y-%m-%d').strftime('%Y-%m-%d')
            self.inputIncome.setText(date)
        except:
            pass

    def __button__(self):
        self.btnClose = QPushButton('닫기')
        self.btnInsert = QPushButton('입력')
        self.btnClose.setStyleSheet(Style.PushButton_Close)
        self.btnInsert.setStyleSheet(Style.PushButton_Tools)
        self.btnInsert.setDefault(True)
        self.btnClose.clicked.connect(self.close)
        self.btnInsert.clicked.connect(self.btnInsertClick)

    def btnInsertClick(self):
        if not self.inputBusinessName.text():
            dig = DialogMessageBox('', '사업명을 입력하세요.')
            dig.exec_()
        elif not self.inputBusinessCode.text():
            dig = DialogMessageBox('', '사업코드를 입력하세요.')
            dig.exec_()
        else:
            businessData = [self.businessNumber,
                            self.inputBusinessName.text(),
                            self.inputBusinessCode.text(),
                            self.inputForm.currentText(),
                            self.inputOrder.text(),
                            self.inputSummary.toPlainText(),
                            self.inputStartDate.text(),
                            self.inputFinishDate.text(),
                            self.inputTotalMonth.text(),
                            self.inputRetention.text(),
                            self.inputMaster.text(),
                            self.inputPL.text(),
                            self.inputAdministrator.text(),
                            self.inputPrice.text(),
                            self.inputStatus.currentText()]
            self.connBusiness.InsertBusiness(businessData)
            for idx, obj in enumerate(self.objects):
                if idx not in [2, 13]:
                    obj.setText('')
            self.inputForm.setCurrentText('기술')
            self.inputStatus.setCurrentText('진행')
            self.widget.refresh()

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(QLabel(''), 10)
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInsert)
        layoutBtn.addWidget(QLabel(''), 10)
        layoutInput = QFormLayout()
        for text, obj in zip(self.objText, self.objects):
            layoutInput.addRow(text, obj)
        layout = QVBoxLayout()
        layout.addLayout(layoutInput)
        layout.addWidget(QLabel(''))
        layout.addLayout(layoutBtn)
        self.setLayout(layout)
