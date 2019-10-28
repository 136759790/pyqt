import sys
sys.path.append("./")
from PyQt5.QtWidgets import *
from demo2.qt.Ui_tabDemo import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
    
