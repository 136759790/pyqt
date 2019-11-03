import sys
sys.path.append('./')
from PyQt5.QtWidgets import *
from glodon.mainWin.Ui_mainWindow import Ui_MainWindow
from glodon.setting.setting import Setting
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
    

    def showWin(self):
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.btn_setting.clicked.connect(lambda:self.btn_setting(ui))
        self.show()
    
    def btn_query(self,ui):
        
    
    def btn_setting(self,ui):
        # appkey secret url
        set = Setting()
        appkey =ui.input_appkey.text()
        if set.selectSetting('appkey'):
            set.updateSetting('appkey',appkey)
        else:
            set.insertSetting('appkey',appkey)
        secret =ui.input_secret.text()
        if set.selectSetting('secret'):
            set.updateSetting('secret',secret)
        else:
            set.insertSetting('secret',secret)
        url=ui.input_url.text()
        if set.selectSetting('url'):
            set.updateSetting('url',url)
        else:
            set.insertSetting('url',url)