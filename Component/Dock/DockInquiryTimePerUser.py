from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetInquiryTimePerUser import WidgetInquiryTimePerUser
from Design import Style


class DockInquiryTimePerUser(QDockWidget):
    def __init__(self, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        widget = WidgetInquiryTimePerUser(self)
        self.setWidget(widget)
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetInquiryTimePerUser(self)
        self.setWidget(widget)
