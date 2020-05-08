from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetInquiryUser import WidgetInquiryUser
from Design import Style


class DockInquiryUser(QDockWidget):
    def __init__(self, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        widget = WidgetInquiryUser(self)
        self.setWidget(widget)
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetInquiryUser(self)
        self.setWidget(widget)
