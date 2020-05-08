from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetAdminUser import WidgetAdminUser
from Design import Style


class DockAdminUser(QDockWidget):
    def __init__(self, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        widget = WidgetAdminUser(self)
        self.currentCell = widget.currentCell
        self.setWidget(widget)
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetAdminUser(self)
        widget.settingReformat()
        self.setWidget(widget)

