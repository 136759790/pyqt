from PyQt5.QtWidgets import QDialog
from glodon.dlg.Ui_dlg_error import Ui_dlg_error
class DlgTools():
    def __init__(self):
        super().__init__()
        self.dlg = QDialog()
        self.ui = Ui_dlg_error()
    def error(self,msg):
        self.ui.setupUi(self.dlg)
        self.ui.text_msg.setText(msg)
        self.dlg.exec_()
    