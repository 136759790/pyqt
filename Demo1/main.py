



import sys
sys.path.append("./")
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QMdiSubWindow
from demo1 import Ui_main,Ui_setting
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_main.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui_setting = Ui_setting.Ui_Setting()
    widget_setting = QWidget()
    ui_setting.setupUi(widget_setting)
    sub = QMdiSubWindow()
    sub.setWidget(widget_setting)
    ui.mdiArea.addSubWindow(sub)
    ui.btn_setting.clicked.connect(sub.show)
    MainWindow.show()
    sys.exit(app.exec_())