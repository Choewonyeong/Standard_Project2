from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetSettingDatabase import WidgetSettingDatabase
from Design import Style


class DockSettingDatabase(QDockWidget):
    def __init__(self, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        widget = WidgetSettingDatabase(self)
        self.currentYear = widget.currentYear
        self.currentTabText = widget.currentTabText
        self.currentTabText = '2019'
        self.setWidget(widget)
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetSettingDatabase(self)
        widget.settingReformat()
        self.setWidget(widget)
