# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cabinsAvailable.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cabinsAvailable(object):
    def setupUi(self, cabinsAvailable):
        cabinsAvailable.setObjectName("cabinsAvailable")
        cabinsAvailable.setWindowModality(QtCore.Qt.ApplicationModal)
        cabinsAvailable.resize(593, 283)
        cabinsAvailable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(cabinsAvailable)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cab1 = QtWidgets.QCheckBox(cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cab1.sizePolicy().hasHeightForWidth())
        self.cab1.setSizePolicy(sizePolicy)
        self.cab1.setIconSize(QtCore.QSize(20, 20))
        self.cab1.setShortcut("")
        self.cab1.setCheckable(True)
        self.cab1.setChecked(False)
        self.cab1.setAutoRepeat(True)
        self.cab1.setTristate(False)
        self.cab1.setObjectName("cab1")
        self.horizontalLayout_2.addWidget(self.cab1)
        self.cab2 = QtWidgets.QCheckBox(cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cab2.sizePolicy().hasHeightForWidth())
        self.cab2.setSizePolicy(sizePolicy)
        self.cab2.setObjectName("cab2")
        self.horizontalLayout_2.addWidget(self.cab2)
        self.cab3 = QtWidgets.QCheckBox(cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cab3.sizePolicy().hasHeightForWidth())
        self.cab3.setSizePolicy(sizePolicy)
        self.cab3.setObjectName("cab3")
        self.horizontalLayout_2.addWidget(self.cab3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cancelar = QtWidgets.QPushButton(cabinsAvailable)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout.addWidget(self.cancelar, 3, 1, 1, 1)
        self.precio = QtWidgets.QPushButton(cabinsAvailable)
        self.precio.setObjectName("precio")
        self.gridLayout.addWidget(self.precio, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)

        self.retranslateUi(cabinsAvailable)
        QtCore.QMetaObject.connectSlotsByName(cabinsAvailable)
        cabinsAvailable.setTabOrder(self.cab1, self.cab2)
        cabinsAvailable.setTabOrder(self.cab2, self.cab3)
        cabinsAvailable.setTabOrder(self.cab3, self.precio)
        cabinsAvailable.setTabOrder(self.precio, self.cancelar)

    def retranslateUi(self, cabinsAvailable):
        _translate = QtCore.QCoreApplication.translate
        cabinsAvailable.setWindowTitle(_translate("cabinsAvailable", "Dialog"))
        self.cab1.setText(_translate("cabinsAvailable", "1"))
        self.cab2.setText(_translate("cabinsAvailable", "2"))
        self.cab3.setText(_translate("cabinsAvailable", "3"))
        self.label.setText(_translate("cabinsAvailable", "Cabañas disponibles"))
        self.cancelar.setText(_translate("cabinsAvailable", "Cancelar"))
        self.precio.setText(_translate("cabinsAvailable", "Precio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cabinsAvailable = QtWidgets.QDialog()
    ui = Ui_cabinsAvailable()
    ui.setupUi(cabinsAvailable)
    cabinsAvailable.show()
    sys.exit(app.exec_())
