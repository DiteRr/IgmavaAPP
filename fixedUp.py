# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fixedUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fixedUp(object):
    def setupUi(self, fixedUp):
        fixedUp.setObjectName("fixedUp")
        fixedUp.resize(366, 253)
        fixedUp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox = QtWidgets.QCheckBox(fixedUp)
        self.checkBox.setGeometry(QtCore.QRect(160, 120, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.label_6 = QtWidgets.QLabel(fixedUp)
        self.label_6.setGeometry(QtCore.QRect(130, 60, 91, 21))
        self.label_6.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.aceptar = QtWidgets.QPushButton(fixedUp)
        self.aceptar.setGeometry(QtCore.QRect(220, 180, 89, 25))
        self.aceptar.setObjectName("aceptar")

        self.retranslateUi(fixedUp)
        QtCore.QMetaObject.connectSlotsByName(fixedUp)

    def retranslateUi(self, fixedUp):
        _translate = QtCore.QCoreApplication.translate
        fixedUp.setWindowTitle(_translate("fixedUp", "Cabaña"))
        self.checkBox.setText(_translate("fixedUp", "Si"))
        self.label_6.setText(_translate("fixedUp", "Arreglado"))
        self.aceptar.setText(_translate("fixedUp", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fixedUp = QtWidgets.QDialog()
    ui = Ui_fixedUp()
    ui.setupUi(fixedUp)
    fixedUp.show()
    sys.exit(app.exec_())
