from PyQt5.QtWidgets import QApplication
from component.dialog.DialogUserSelf import DialogUserSelf
from component.table.TableNewUser import TableNewUser
from component.table.TableAdminUser import TableAdminUser
from component.table.TableInquiryUser import TableInquiryUser
from component.main.Windows import Windows
from component.dialog.DialogNewBusiness import DialogNewBusiness
from component.table.TableTotalPerYear import TableTotalPerYear
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    dig = TableTotalPerYear()
    dig.show()
    app.exec_()