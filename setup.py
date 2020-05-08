from PyQt5.QtWidgets import QApplication
from Component.Loading import Loading
from sys import argv


if __name__ == "__main__":
    app = QApplication(argv)
    loading = Loading()
    loading.show()
    from Component.Login import Login
    from Component.Windows import Windows
    from Connector.ConnUser import ConnUser

    connUser = ConnUser()
    userNames = connUser.ReturnUserNames()
    login = Login(app)
    login.show()
    loading.finish(login)
    app.exec_()
    if login.userName in userNames:
        windows = Windows(login.userName, login.author)
        windows.show()
        app.exec_()
