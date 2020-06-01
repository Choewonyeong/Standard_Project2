from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connBusiness import connBusiness
from connector.connDB import connDB
from component.dialog.DialogMassage import DialogMassage
from material.GeneralLineEdit import GeneralLineEdit
from material.GeneralLabel import GeneralLabel
from material import GeneralTextEdit
from material import GeneralComboBox


class DialogNewBusiness(QDialog):
    def __init__(self, widget):
        QDialog.__init__(self)
        self.widget = widget
        self.__setting__()
        self.__connector__()
        self.__variables__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __connector__(self):
        self.connBusiness = connBusiness()
        self.connDB = connDB(self.widget.windows.CURRENT_YEAR)

    def __variables__(self):
        pass

    def __component__(self):
        self.__label__()
        self.__inputWidgets__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        lblTitle = GeneralLabel('사업명')
        lblCode = GeneralLabel('사업코드')
        lblForm = GeneralLabel('사업형태')
        lblOrder = GeneralLabel('발주처')
        lblSummary = GeneralLabel('사업요약')
        lblStart = GeneralLabel('시작일')
        lblEnd = GeneralLabel('종료일')
        lblMonth = GeneralLabel('개월수')
        lblMax = GeneralLabel('보존기간')
        lblMaster = GeneralLabel('사업책임자')
        lblPL = GeneralLabel('PL')
        lblAdmin = GeneralLabel('기술행정')
        lblPrice = GeneralLabel('사업비')
        lblStatus = GeneralLabel('진행상태')
        self.objectLabel = [lblTitle,
                            lblCode,
                            lblForm,
                            lblOrder,
                            lblSummary,
                            lblStart,
                            lblEnd,
                            lblMonth,
                            lblMax,
                            lblMaster,
                            lblPL,
                            lblAdmin,
                            lblPrice,
                            lblStatus]
        for lbl in self.objectLabel:
            lbl.setFixedWidth(80)

    def __inputWidgets__(self):
        ldtTitle = GeneralLineEdit()
        ldtCode = GeneralLineEdit()
        cbxForm = GeneralComboBox(['기술', '연구', '국책', '일반', '기타'], '기술')
        ldtOrder = GeneralLineEdit()
        tedSummary = GeneralTextEdit()
        tedSummary.setFixedHeight(80)
        ldtStart = GeneralLineEdit(option='dateFormat')

        def ldtStartEdit(text):
            start = text
            end = ldtEnd.text()
            try:
                start = datetime.strptime(start, '%Y-%m-%d')
                end = datetime.strptime(end, '%Y-%m-%d')
                yearCnt = (end.year - start.year)*12
                monthCnt = end.month - start.month
                totalCnt = yearCnt + monthCnt
                self.objectInput[7].setText(str(totalCnt))
            except:
                pass
        ldtStart.textEdited.connect(ldtStartEdit)

        def ldtEndEdit(text):
            start = ldtStart.text()
            end = text
            try:
                start = datetime.strptime(start, '%Y-%m-%d')
                end = datetime.strptime(end, '%Y-%m-%d')
                yearCnt = (end.year - start.year)*12
                monthCnt = end.month - start.month
                totalCnt = yearCnt + monthCnt
                self.objectInput[7].setText(str(totalCnt))
            except:
                pass
        ldtEnd = GeneralLineEdit(option='dateFormat')
        ldtEnd.textEdited.connect(ldtEndEdit)
        ldtMonth = GeneralLineEdit(option='disable')
        ldtMax = GeneralLineEdit(option='dateFormat')
        ldtMaster = GeneralLineEdit()
        ldtPL = QLineEdit()
        ldtAdmin = QLineEdit()
        ldtPrice = GeneralLineEdit(option='moneyFormat')
        cbxStatus = GeneralComboBox(['수주', '진행', '중단', '준공', 'A/S'], '진행')
        self.objectInput = [ldtTitle,
                            ldtCode,
                            cbxForm,
                            ldtOrder,
                            tedSummary,
                            ldtStart,
                            ldtEnd,
                            ldtMonth,
                            ldtMax,
                            ldtMaster,
                            ldtPL,
                            ldtAdmin,
                            ldtPrice,
                            cbxStatus]

    def __pushButton__(self):
        def btnCloseClick():
            self.close()
        self.btnClose = QPushButton('닫기')
        self.btnClose.setCursor(Qt.PointingHandCursor)
        self.btnClose.clicked.connect(btnCloseClick)

        def btnInsertClick():
            businessInfo = []
            for idx, info in enumerate(self.objectInput):
                if idx in [2, 13]:
                    businessInfo.append(info.currentText())
                elif idx == 4:
                    businessInfo.append(info.toPlainText())
                else:
                    businessInfo.append(info.text())
            if businessInfo[0] == '':
                DialogMassage('사업명을 입력하세요.')
            elif businessInfo[1] == '':
                DialogMassage('사업코드를 입력하세요.')
            else:
                number = self.connBusiness.insertBusiness(businessInfo)
                self.widget.windows.refresh()
                self.connDB.insertNewBusiness(number)
                DialogMassage('반영되었습니다.')
                self.close()

        self.btnInsert = QPushButton('입력')
        self.btnInsert.setCursor(Qt.PointingHandCursor)
        self.btnInsert.clicked.connect(btnInsertClick)
        self.btnInsert.setDefault(True)

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInsert)
        layout = QVBoxLayout()
        for lbl, widget in zip(self.objectLabel, self.objectInput):
            layoutObjects = QHBoxLayout()
            layoutObjects.addWidget(lbl)
            layoutObjects.addWidget(widget)
            layout.addLayout(layoutObjects)
        layout.addLayout(layoutBtn)
        self.setLayout(layout)