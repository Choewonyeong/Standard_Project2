from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetAdminBusiness import WidgetAdminBusiness
from Design import Style


class DockAdminBusiness(QDockWidget):
    def __init__(self, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        widget = WidgetAdminBusiness(self)
        self.currentCell = widget.currentCell
        self.setWidget(widget)
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetAdminBusiness(self)
        widget.settingReformat()
        self.setWidget(widget)
