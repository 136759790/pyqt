# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\zxt\workspace_py\pyqt\glodon\mainWin\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.iDLabel = QtWidgets.QLabel(self.tab)
        self.iDLabel.setObjectName("iDLabel")
        self.horizontalLayout_3.addWidget(self.iDLabel)
        self.input_ws_id = QtWidgets.QLineEdit(self.tab)
        self.input_ws_id.setObjectName("input_ws_id")
        self.horizontalLayout_3.addWidget(self.input_ws_id)
        self.btn_query = QtWidgets.QPushButton(self.tab)
        self.btn_query.setObjectName("btn_query")
        self.horizontalLayout_3.addWidget(self.btn_query)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_setting = QtWidgets.QPushButton(self.tab_2)
        self.btn_setting.setGeometry(QtCore.QRect(240, 250, 93, 28))
        self.btn_setting.setObjectName("btn_setting")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(11, 81, 581, 121))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.input_appkey = QtWidgets.QLineEdit(self.widget)
        self.input_appkey.setObjectName("input_appkey")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_appkey)
        self.label14 = QtWidgets.QLabel(self.widget)
        self.label14.setObjectName("label14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label14)
        self.input_secret = QtWidgets.QLineEdit(self.widget)
        self.input_secret.setObjectName("input_secret")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_secret)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.input_url = QtWidgets.QLineEdit(self.widget)
        self.input_url.setObjectName("input_url")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_url)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.listWidget.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "广联云"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.iDLabel.setText(_translate("MainWindow", "云空间ID："))
        self.btn_query.setText(_translate("MainWindow", "查询"))
        self.label.setText(_translate("MainWindow", "空间ID："))
        self.label_2.setText(_translate("MainWindow", "人员数量："))
        self.label_3.setText(_translate("MainWindow", "空间大小："))
        self.label_4.setText(_translate("MainWindow", "到期时间："))
        self.label_5.setText(_translate("MainWindow", "生效时间："))
        self.label_6.setText(_translate("MainWindow", "创建人："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "查询"))
        self.btn_setting.setText(_translate("MainWindow", "设置"))
        self.label_13.setText(_translate("MainWindow", "Appkey:"))
        self.label14.setText(_translate("MainWindow", "Secret:"))
        self.label_15.setText(_translate("MainWindow", "Url:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "设置"))
        self.menu.setTitle(_translate("MainWindow", "登录"))
