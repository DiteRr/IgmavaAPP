# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'host.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.resize(286, 235)
        dialog.setStyleSheet("alternate-background-color: rgb(238, 238, 236);")
        self.groupBox = QtWidgets.QGroupBox(dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 201, 81))
        self.groupBox.setStyleSheet("font: 57 12pt \"Ubuntu\";")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.ip = QtWidgets.QLineEdit(self.groupBox)
        self.ip.setObjectName("ip")
        self.gridLayout.addWidget(self.ip, 0, 0, 1, 1)
        self.link = QtWidgets.QPushButton(dialog)
        self.link.setGeometry(QtCore.QRect(160, 180, 89, 25))
        self.link.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.link.setObjectName("link")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Host"))
        self.groupBox.setTitle(_translate("dialog", "Host"))
        self.ip.setText(_translate("dialog", "127.0.0.1:8007"))
        self.link.setText(_translate("dialog", "Link"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
