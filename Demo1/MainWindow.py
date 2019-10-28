import sys
sys.path.append("./")
from PyQt5 import QtCore,QtGui,QtWidgets
from demo1.Ui_main import Ui_MainWindow
from demo1.Ui_setting import Ui_Setting
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.btn_setting.clicked.connect(self.initSetting)

    def initSetting(self):
        ui_setting = Ui_Setting()
