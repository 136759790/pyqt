# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\zxt\workspace_py\pyqt\Demo1\setting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(608, 429)
        self.formLayoutWidget = QtWidgets.QWidget(Setting)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 90, 441, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pushButton = QtWidgets.QPushButton(Setting)
        self.pushButton.setGeometry(QtCore.QRect(140, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Setting)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "设置"))
        self.label.setText(_translate("Setting", "Appkey："))
        self.label_2.setText(_translate("Setting", "Secret："))
        self.label_3.setText(_translate("Setting", "广联云地址:"))
        self.label_4.setText(_translate("Setting", "用户中心地址:"))
        self.pushButton.setText(_translate("Setting", "保存"))
        self.pushButton_2.setText(_translate("Setting", "确定"))
