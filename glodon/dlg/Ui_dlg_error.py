# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\zxt\python\pyqt\glodon\dlg\dlg_error.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_error(object):
    def setupUi(self, dlg_error):
        dlg_error.setObjectName("dlg_error")
        dlg_error.resize(249, 139)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlg_error)
        self.buttonBox.setGeometry(QtCore.QRect(50, 100, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(dlg_error)
        self.widget.setGeometry(QtCore.QRect(10, 10, 231, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_dlg = QtWidgets.QLabel(self.widget)
        self.label_dlg.setObjectName("label_dlg")
        self.horizontalLayout.addWidget(self.label_dlg)
        self.text_msg = QtWidgets.QTextEdit(self.widget)
        self.text_msg.setObjectName("text_msg")
        self.horizontalLayout.addWidget(self.text_msg)

        self.retranslateUi(dlg_error)
        self.buttonBox.accepted.connect(dlg_error.accept)
        self.buttonBox.rejected.connect(dlg_error.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_error)

    def retranslateUi(self, dlg_error):
        _translate = QtCore.QCoreApplication.translate
        dlg_error.setWindowTitle(_translate("dlg_error", "提示"))
        self.label_dlg.setText(_translate("dlg_error", "提示信息："))

