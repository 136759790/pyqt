from PyQt5.QtWidgets import QDialog
from glodon.dlg.Ui_dlg_error import Ui_dlg_error
class DlgTools():
    def __init__(self):
        super().__init__()
        self.dlg = QDialog()
    def error(self,msg):
        ui = Ui_dlg_error()
        print(ui.__dict__)
        # ui.label_dlg.setText(msg)
        ui.setupUi(self.dlg)
        self.dlg.show()
    