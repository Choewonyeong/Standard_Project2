from PyQt5.QtWidgets import QApplication
from component.dialog.DialogNewUser import DialogNewUser
from component.dialog.DialogUserSelf import DialogUserSelf
from component.table.TableNewUser import TableNewUser
from component.table.TableAdminUser import TableAdminUser
from component.dialog.DialogInquiryUser import DialogInquiryUser
from component.table.TableInquiryUser import TableInquiryUser
from component.main.Windows import Windows
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    dig = DialogInquiryUser()
    dig.show()
    app.exec_()