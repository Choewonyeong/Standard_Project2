from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetUserTime import WidgetUserTime
from Design import Style


class DockUserTime(QDockWidget):
    def __init__(self, userName, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        self.userName = userName
        widget = WidgetUserTime(userName, self)
        self.setWidget(widget)
        self.showMaximized()
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetUserTime(self.userName, self)
        self.setWidget(widget)
