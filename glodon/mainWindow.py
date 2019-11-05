import sys
sys.path.append('./')
from PyQt5.QtWidgets import *
from glodon.mainWin.Ui_mainWindow import Ui_MainWindow
from glodon.setting.setting import Setting
from glodon.query.query import GlodonQuery
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
    

    def showWin(self):
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.btn_setting.clicked.connect(lambda:self.btn_setting(ui))
        ui.btn_query.clicked.connect(lambda:GlodonQuery().query(ui))
        self.show()
    
    def btn_query(self,ui):
        print(ui.input_ws_id.text())
    
    def btn_setting(self,ui):
        # appkey secret url
        set = Setting()
        appkey =ui.input_appkey.text()
        apk = set.selectSetting('appkey')
        if apk:
            set.updateSetting('appkey',appkey,apk[0][0])
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