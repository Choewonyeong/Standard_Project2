from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from connector.connBusiness import connBusiness
from component.dialog.DialogMassage import DialogMassage
from component.material.GeneralLineEdit import GeneralLineEdit


class DialogNewBusiness(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.__setting__()
        self.__component__()

    def __setting__(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def __connector__(self):
        self.connBusiness = connBusiness()

    def __variables__(self):
        numbers = self.connBusiness.returnNumbers()
        self.number = 0 if not numbers else max(numbers)

    def __component__(self):
        self.__label__()
        self.__inputWidgets__()
        self.__pushButton__()
        self.__layout__()

    def __label__(self):
        lblTitle = QLabel('사업명')
        lblCode = QLabel('사업코드')
        lblForm = QLabel('사업형태')
        lblOrder = QLabel('발주처')
        lblSummary = QLabel('사업요약')
        lblStart = QLabel('시작일')
        lblEnd = QLabel('종료일')
        lblMonth = QLabel('개월수')
        lblMax = QLabel('보존기간')
        lblMaster = QLabel('사업책임자')
        lblPL = QLabel('PL')
        lblAdmin = QLabel('기술행정')
        lblPrice = QLabel('사업비')
        lblStatus = QLabel('진행상태')
        lblEditDate = QLabel('수정한날짜')
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
                            lblStatus,
                            lblEditDate]
        for lbl in self.objectLabel:
            lbl.setFixedWidth(80)

    def __inputWidgets__(self):
        ldtTitle = QLineEdit()
        ldtCode = QLineEdit()
        cbxForm = QComboBox()
        cbxForm.addItems(['기술', '연구', '국책', '일반', '기타'])
        ldtOrder = QLineEdit()
        tedSummary = QTextEdit()
        tedSummary.setFixedHeight(80)
        ldtStart = QLineEdit()
        ldtEnd = QLineEdit()
        ldtMonth = QLineEdit()
        ldtMax = QLineEdit()
        ldtMaster = QLineEdit()
        ldtPL = QLineEdit()
        ldtAdmin = QLineEdit()
        ldtPrice = QLineEdit()
        cbxStatus = QComboBox()
        cbxStatus.addItems(['수주', '진행', '중단', '준공', 'A/S'])
        cbxStatus.setCurrentText('진행')
        ldtEditDate = QLineEdit()
        ldtEditDate.setEnabled(False)
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
                            cbxStatus,
                            ldtEditDate]

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
            print(businessInfo)
        self.btnInsert = QPushButton('입력')
        self.btnInsert.setCursor(Qt.PointingHandCursor)
        self.btnInsert.clicked.connect(btnInsertClick)
        self.btnInsert.setDefault(True)

    def __layout__(self):
        layoutBtn = QHBoxLayout()
        layoutBtn.addWidget(self.btnClose)
        layoutBtn.addWidget(self.btnInsert)
        layout = QVBoxLayout()
        # 내일 여기부터
        for lbl, widget in zip(self.objectLabel, self.objectInput):
            layoutObjects = QHBoxLayout()
            layoutObjects.addWidget(lbl)
            layoutObjects.addWidget(widget)
            layout.addLayout(layoutObjects)
        layout.addLayout(layoutBtn)
        self.setLayout(layout)