import sys

from glodon.dlg.dlg_tools import DlgTools
class GlodonQuery():
    def __init__(self):
        super().__init__()
    
    def query(self,ui):
        ws_id = ui.input_ws_id.text()
        if len(ws_id) == 0:
            DlgTools().error('空间ID不能为空')