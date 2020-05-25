from PyQt5.QtWidgets import QApplication, QStyleFactory
from component.main.Loading import Loading
from sys import argv


def run():
    app = QApplication(argv)
    # app.setStyle(QStyleFactory.create('fusion'))
    # print(QStyleFactory.keys())
    loading = Loading()
    loading.show()
    from component.main.Login import Login
    login = Login(app)
    login.show()
    loading.finish(login)
    app.exec_()


if __name__ == "__main__":
    run()
