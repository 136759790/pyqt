# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\zxt\workspace_py\pyqt\Demo1\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 131, 571))
        self.widget.setObjectName("widget")
        self.btn_setting = QtWidgets.QPushButton(self.widget)
        self.btn_setting.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.btn_setting.setObjectName("btn_setting")
        self.btn_gdoc = QtWidgets.QPushButton(self.widget)
        self.btn_gdoc.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.btn_gdoc.setObjectName("btn_gdoc")
        self.btn_user = QtWidgets.QPushButton(self.widget)
        self.btn_user.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.btn_user.setObjectName("btn_user")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(129, -1, 661, 571))
        self.widget_2.setObjectName("widget_2")
        self.mdiArea = QtWidgets.QMdiArea(self.widget_2)
        self.mdiArea.setGeometry(QtCore.QRect(-1, -1, 661, 581))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_setting, self.btn_user)
        MainWindow.setTabOrder(self.btn_user, self.btn_gdoc)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BIM-Tools"))
        self.btn_setting.setText(_translate("MainWindow", "设置"))
        self.btn_gdoc.setText(_translate("MainWindow", "广联云接口"))
        self.btn_user.setText(_translate("MainWindow", "用户接口"))
