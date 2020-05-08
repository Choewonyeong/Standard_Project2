from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QPushButton
from Component.Widget.WidgetCreateDatabse import WidgetCreateDatabase
from Design import Style


class DockCreateDatabase(QDockWidget):
    def __init__(self, windows=None):
        QDockWidget.__init__(self)
        self.windows = windows
        widget = WidgetCreateDatabase(self)
        self.currentYear = widget.currentYear
        self.setWidget(widget)
        btnClose = QPushButton('')
        btnClose.setStyleSheet(Style.PushButton_Hide)
        btnClose.setEnabled(False)
        self.setTitleBarWidget(btnClose)

    def refresh(self):
        widget = WidgetCreateDatabase(self)
        widget.settingReformat()
        self.setWidget(widget)
