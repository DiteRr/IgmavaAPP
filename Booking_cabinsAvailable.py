# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Booking_cabinsAvailable.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Booking_cabinsAvailable(object):
    def setupUi(self, Booking_cabinsAvailable):
        Booking_cabinsAvailable.setObjectName("Booking_cabinsAvailable")
        Booking_cabinsAvailable.setWindowModality(QtCore.Qt.ApplicationModal)
        Booking_cabinsAvailable.resize(550, 342)
        Booking_cabinsAvailable.setStyleSheet("background-color: rgb(255, 255, 255);")
        Booking_cabinsAvailable.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Booking_cabinsAvailable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Booking_cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cab1_2 = QtWidgets.QCheckBox(Booking_cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cab1_2.sizePolicy().hasHeightForWidth())
        self.cab1_2.setSizePolicy(sizePolicy)
        self.cab1_2.setIconSize(QtCore.QSize(20, 20))
        self.cab1_2.setShortcut("")
        self.cab1_2.setCheckable(True)
        self.cab1_2.setChecked(False)
        self.cab1_2.setAutoRepeat(True)
        self.cab1_2.setTristate(False)
        self.cab1_2.setObjectName("cab1_2")
        self.horizontalLayout_3.addWidget(self.cab1_2)
        self.cab2_2 = QtWidgets.QCheckBox(Booking_cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cab2_2.sizePolicy().hasHeightForWidth())
        self.cab2_2.setSizePolicy(sizePolicy)
        self.cab2_2.setObjectName("cab2_2")
        self.horizontalLayout_3.addWidget(self.cab2_2)
        self.cab3_2 = QtWidgets.QCheckBox(Booking_cabinsAvailable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cab3_2.sizePolicy().hasHeightForWidth())
        self.cab3_2.setSizePolicy(sizePolicy)
        self.cab3_2.setObjectName("cab3_2")
        self.horizontalLayout_3.addWidget(self.cab3_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelar = QtWidgets.QPushButton(Booking_cabinsAvailable)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout.addWidget(self.cancelar)
        self.precio = QtWidgets.QPushButton(Booking_cabinsAvailable)
        self.precio.setObjectName("precio")
        self.horizontalLayout.addWidget(self.precio)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Booking_cabinsAvailable)
        QtCore.QMetaObject.connectSlotsByName(Booking_cabinsAvailable)
        Booking_cabinsAvailable.setTabOrder(self.cab1_2, self.cab2_2)
        Booking_cabinsAvailable.setTabOrder(self.cab2_2, self.cab3_2)
        Booking_cabinsAvailable.setTabOrder(self.cab3_2, self.precio)
        Booking_cabinsAvailable.setTabOrder(self.precio, self.cancelar)

    def retranslateUi(self, Booking_cabinsAvailable):
        _translate = QtCore.QCoreApplication.translate
        Booking_cabinsAvailable.setWindowTitle(_translate("Booking_cabinsAvailable", "Cabañas disponibles"))
        self.label.setText(_translate("Booking_cabinsAvailable", "Cabañas disponibles"))
        self.cab1_2.setText(_translate("Booking_cabinsAvailable", "1"))
        self.cab2_2.setText(_translate("Booking_cabinsAvailable", "2"))
        self.cab3_2.setText(_translate("Booking_cabinsAvailable", "3"))
        self.cancelar.setText(_translate("Booking_cabinsAvailable", "Cancelar"))
        self.precio.setText(_translate("Booking_cabinsAvailable", "Precio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Booking_cabinsAvailable = QtWidgets.QDialog()
    ui = Ui_Booking_cabinsAvailable()
    ui.setupUi(Booking_cabinsAvailable)
    Booking_cabinsAvailable.show()
    sys.exit(app.exec_())
