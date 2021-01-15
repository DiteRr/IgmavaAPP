# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Disable_cab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Disable_cab(object):
    def setupUi(self, Disable_cab):
        Disable_cab.setObjectName("Disable_cab")
        Disable_cab.setWindowModality(QtCore.Qt.ApplicationModal)
        Disable_cab.resize(673, 460)
        Disable_cab.setStyleSheet("background-color: rgb(255, 255, 255);")
        Disable_cab.setModal(True)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Disable_cab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(160, 100, 322, 27))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.checkin = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.checkin.setStyleSheet("background-color : #CDCDCD;\n"
"color: rgb(0,0,0);")
        self.checkin.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 28), QtCore.QTime(0, 0, 0)))
        self.checkin.setTime(QtCore.QTime(0, 0, 0))
        self.checkin.setCalendarPopup(True)
        self.checkin.setTimeSpec(QtCore.Qt.LocalTime)
        self.checkin.setDate(QtCore.QDate(2020, 12, 28))
        self.checkin.setObjectName("checkin")
        self.horizontalLayout_2.addWidget(self.checkin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.checkout = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.checkout.setStyleSheet("background-color : #CDCDCD;\n"
"color: rgb(0,0,0);")
        self.checkout.setCalendarPopup(True)
        self.checkout.setDate(QtCore.QDate(2020, 12, 28))
        self.checkout.setObjectName("checkout")
        self.horizontalLayout_2.addWidget(self.checkout)
        self.label_6 = QtWidgets.QLabel(Disable_cab)
        self.label_6.setGeometry(QtCore.QRect(210, 30, 321, 61))
        self.label_6.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.aceptar = QtWidgets.QPushButton(Disable_cab)
        self.aceptar.setGeometry(QtCore.QRect(470, 330, 131, 41))
        self.aceptar.setObjectName("aceptar")
        self.cancelar = QtWidgets.QPushButton(Disable_cab)
        self.cancelar.setGeometry(QtCore.QRect(280, 330, 131, 41))
        self.cancelar.setObjectName("cancelar")
        self.gridLayoutWidget = QtWidgets.QWidget(Disable_cab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 160, 441, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tipo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tipo.setObjectName("tipo")
        self.gridLayout.addWidget(self.tipo, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.descripcion = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.descripcion.setObjectName("descripcion")
        self.gridLayout.addWidget(self.descripcion, 1, 1, 1, 1)

        self.retranslateUi(Disable_cab)
        QtCore.QMetaObject.connectSlotsByName(Disable_cab)
        Disable_cab.setTabOrder(self.checkin, self.checkout)
        Disable_cab.setTabOrder(self.checkout, self.tipo)
        Disable_cab.setTabOrder(self.tipo, self.descripcion)
        Disable_cab.setTabOrder(self.descripcion, self.aceptar)
        Disable_cab.setTabOrder(self.aceptar, self.cancelar)

    def retranslateUi(self, Disable_cab):
        _translate = QtCore.QCoreApplication.translate
        Disable_cab.setWindowTitle(_translate("Disable_cab", "Deshabilitar cabaña"))
        self.label_4.setText(_translate("Disable_cab", "Desde"))
        self.label.setText(_translate("Disable_cab", "Hasta"))
        self.label_6.setText(_translate("Disable_cab", "Deshabilitar cabaña"))
        self.aceptar.setText(_translate("Disable_cab", "Aceptar"))
        self.cancelar.setText(_translate("Disable_cab", "Cancelar"))
        self.label_2.setText(_translate("Disable_cab", "       Tipo:"))
        self.label_3.setText(_translate("Disable_cab", "Descripción:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Disable_cab = QtWidgets.QDialog()
    ui = Ui_Disable_cab()
    ui.setupUi(Disable_cab)
    Disable_cab.show()
    sys.exit(app.exec_())
