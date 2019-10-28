import sys
from PyQt5.QtWidgets import *
class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample,self).__init__()
        self.setGeometry(300,50,10,10)
        self.setWindowTitle('StackedExample例子')
        self.resize(800,600)

        #左侧列表
        self.leftList = QListWidget()
        self.leftList.insertItem(0,'联系方式')
        self.leftList.insertItem(1,'个人信息')
        self.leftList.insertItem(2,'教育程度')

        #右侧布局信息
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stackUI1()
        self.stackUI2()
        self.stackUI3()

        #右侧布局添加到Stack
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        #设置整体布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.leftList)
        hbox.addWidget(self.Stack)
        self.setLayout(hbox)

        #关联信号与曹
        self.leftList.currentRowChanged.connect(self.display)

    def stackUI1(self):
        layout = QFormLayout()
        layout.addRow('姓名：',QLineEdit())
        layout.addRow('地址：',QLineEdit())
        self.stack1.setLayout(layout)
    def stackUI2(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())
        self.stack2.setLayout(layout)
    def stackUI3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.stack3.setLayout(layout)
    def display(self,i):
        self.Stack.setCurrentIndex(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())
