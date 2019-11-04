# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\zxt\workspace_py\pyqt\glodon\dlg\dlg_error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlg_error(object):
    def setupUi(self, dlg_error):
        dlg_error.setObjectName("dlg_error")
        dlg_error.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlg_error)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_dlg = QtWidgets.QLabel(dlg_error)
        self.label_dlg.setGeometry(QtCore.QRect(130, 120, 72, 15))
        self.label_dlg.setText("")
        self.label_dlg.setObjectName("label_dlg")

        self.retranslateUi(dlg_error)
        self.buttonBox.accepted.connect(dlg_error.accept)
        self.buttonBox.rejected.connect(dlg_error.reject)
        QtCore.QMetaObject.connectSlotsByName(dlg_error)

    def retranslateUi(self, dlg_error):
        _translate = QtCore.QCoreApplication.translate
        dlg_error.setWindowTitle(_translate("dlg_error", "提示"))
