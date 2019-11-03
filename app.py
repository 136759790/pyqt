import sys
sys.path.append('./')
from PyQt5.QtWidgets import *
from glodon.mainWindow import MainWindow

if __name__ =='__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showWin()
    sys.exit(app.exec_())
