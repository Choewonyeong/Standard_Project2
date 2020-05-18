SplashScreenLoading = """
QSplashScreen{
    background: #ffffff;
}
"""





PushButton_Excel = """
QPushButton{
    color: white;
    background-color: #00a064;
    border: solid black 1px;
    border-radius: 5px;
    min-width: 80px;
    max-width: 80px;
    min-height: 30px;
}

QPushButton:hover{
    background-color: #00dc96;
}

QPushButton:pressed{
    background-color: #00dc96;
}

QPushButton::disabled
{
    color: gray;
    background-color: #e6e6e6;
}
"""

PushButton_Delete = """
QPushButton{
    color: white;
    background-color: #ffa096;
    border: solid black 1px;
    border-radius: 5px;
    min-width: 80px;
    max-width: 80px;
    min-height: 30px;
}

QPushButton:hover{
    background-color: #ffbeb4;
}

QPushButton:pressed{
    background-color: #ffbeb4;
}

QPushButton::disabled
{
    color: gray;
    background-color: #e6e6e6;
}
"""

PushButton_Tools = """
QPushButton{
    color: white;
    background-color: #0096ff;
    border: solid black 1px;
    border-radius: 5px;
    min-width: 80px;
    max-width: 80px;
    min-height: 30px;
}

QPushButton:hover{
    background-color: #00dcff;
}

QPushButton:pressed{
    background-color: #00dcff;
}
"""

PushButton_Close = """
QPushButton{
    color: white;
    background-color: #ffaa00;
    border: solid black 1px;
    border-radius: 5px;
    min-width: 80px;
    max-width: 80px;
    min-height: 30px;
}

QPushButton:hover{
    background-color: #ffd200;
}

QPushButton:pressed{
    background-color: #ffd200;
}
"""

PushButton_Hide = """
QPushButton{
    color: white;
    background-color: white;
    border: 0px;
    width: 0px;
    height: 0px;
}
"""

PushButton_Apply = """
QPushButton{
    background-color: #00dcfa;
    border: solid black 1px;
    border-radius: 5px;
    margin-top: 3px;
    margin-bottom: 3px;
    margin-left: 3px;
    margin-right: 3px;
    min-width: 80px;
    max-width: 80px;
}

QPushButton::disabled
{
    background-color: #e6e6e6;
}

QPushButton:hover{
    background-color: #00ffff;
}

QPushButton:pressed{
    background-color: #00ffff;
}
"""

PushButton_NoApply = """
QPushButton{
    background-color: #ffa096;
    border: solid black 1px;
    border-radius: 5px;
    margin-top: 3px;
    margin-bottom: 3px;
    margin-left: 3px;
    margin-right: 3px;
    min-width: 80px;
    max-width: 80px;
}

QPushButton:hover{
    background-color: #ffbeb4;
}

QPushButton:pressed{
    background-color: #ffbeb4;
}
"""

Table_Standard = """
QTableWidget{
    color: black;
}

QHeaderView{
    color: white;
}

QHeaderView::section{
    background-color: #003264;
    border: 1px solid white;
}

QHeaderView::selected{
    background-color: #003264;
    border: 1px solid white;
}
"""

Table_Time = """
QTableWidget{
    color: black;
}

QHeaderView{
    color: white;
}

QHeaderView::section{
    background-color: #003264;
    border: 1px solid white;
}

QHeaderView::selected{
    background-color: #003264;
    border: 1px solid white;
}
"""

Table_Header = """
QTableWidget{
    background-color: #003264;
    color: white;
    font-weight: bold;
}
"""

Table_TimeTotal = """
QTableWidget{
    color: black;
    font-weight: bold;
}
"""

GroupBox_Standard = """
QGroupBox{
    border: 0px;
}
"""

ComboBox_InTable = """
QComboBox{
    color: black;
    background-color: #ffffff;
    border: 1px solid gray;
    border-radius: 3px;
    min-width: 60px;
}
"""

ComboBox_OutTable = """
QComboBox{
    color: black;
    background-color: #ffffff;
    border: 1px solid #0096ff;
    border-radius: 3px;
    min-width: 80px;
    min-height: 30px;
}
"""

ListWidget_Main = """
QListView{
    border: 0px;
    background-color: #003264;
    font-size: 15px;
}

QListView::item {
    color: white;
    height: 50px;
}

QListView::item:hover {
    background-color: #001e50;
    border: 0px;
}

QListView::item:selected {
    background-color: #001e50;
    border: 0px;
}
"""

ListWidget_Sub = """
QListView{
    border: 0px;
}

QListView::item {
    height: 50px;
}
"""

MainWidget = """
QWidget{
    background-color: white;
}

QScrollBar:horizontal{
    border: 1px solid gray;
    background-color: #ffffff;
    height: 20px;
}

QScrollBar::handle:horizontal{
    background-color: #003264;
    min-width: 20px;
}

QScrollBar:vertical{
    border: 1px solid gray;
    background-color: #ffffff;
    width: 20px;
}

QScrollBar::handle:vertical{
    background-color: #003264;
    min-height: 20px;
}
"""

Components_Dialog = """
QDialog{
    background-color: white;
    border: 1px solid black;
    border-radius: 3px;
}

QLineEdit{
    border: 1px solid #0096ff;
    border-radius: 3px;
    min-height: 30px;    
    min-width: 80px;
    margin-bottom: 5px;
}

QLineEdit:disabled{
    border: 1px solid #ffa096;
    color: black;
}

QTextEdit{
    border: 1px solid #0096ff;
    border-radius: 5px;
    min-height: 30px;    
    min-width: 80px;
    margin-bottom: 5px;
}

QLabel{
    min-height: 30px;
    font-weight: bold;
}

QComboBox{
    color: black;
    background-color: #ffffff;
    border: 1px solid #0096ff;
    border-radius: 3px;
    min-width: 80px;
    min-height: 30px;    
}
"""

Login_Dialog = """
QDialog{
    background-color: white;
    border: 1px solid black;
    border-radius: 3px;
}

QLineEdit{
    border: 1px solid #0096ff;
    border-radius: 3px;
    min-height: 30px;    
    min-width: 120px;
}

QLabel{
    min-height: 30px;
}
"""

Message_Dialog = """
QDialog{
    background-color: white;
    border: 1px solid black;
    border-radius: 3px;
}

QLabel{
    min-width: 200px;
}
"""

Label_Caution = """
QLabel{
    color: red;
    margin-top: -20px;
    margin-bottom: 5px;
    padding-top: 0px;
    padding-bottom: 3px;
}
"""