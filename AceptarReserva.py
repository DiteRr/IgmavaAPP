# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AceptarReserva.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Aceptar_Reserva(object):
    def setupUi(self, Aceptar_Reserva):
        Aceptar_Reserva.setObjectName("Aceptar_Reserva")
        Aceptar_Reserva.setWindowModality(QtCore.Qt.ApplicationModal)
        Aceptar_Reserva.resize(441, 284)
        Aceptar_Reserva.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Aceptar_Reserva)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 271, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.precio = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.precio.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.precio.setObjectName("precio")
        self.horizontalLayout.addWidget(self.precio)
        self.aceptar = QtWidgets.QPushButton(Aceptar_Reserva)
        self.aceptar.setGeometry(QtCore.QRect(330, 220, 89, 25))
        self.aceptar.setObjectName("aceptar")
        self.cancelar = QtWidgets.QPushButton(Aceptar_Reserva)
        self.cancelar.setGeometry(QtCore.QRect(230, 220, 89, 25))
        self.cancelar.setObjectName("cancelar")

        self.retranslateUi(Aceptar_Reserva)
        QtCore.QMetaObject.connectSlotsByName(Aceptar_Reserva)

    def retranslateUi(self, Aceptar_Reserva):
        _translate = QtCore.QCoreApplication.translate
        Aceptar_Reserva.setWindowTitle(_translate("Aceptar_Reserva", "Reserva"))
        self.label.setText(_translate("Aceptar_Reserva", "Precio (Dolars) = "))
        self.precio.setText(_translate("Aceptar_Reserva", "42000"))
        self.aceptar.setText(_translate("Aceptar_Reserva", "Aceptar"))
        self.cancelar.setText(_translate("Aceptar_Reserva", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Aceptar_Reserva = QtWidgets.QDialog()
    ui = Ui_Aceptar_Reserva()
    ui.setupUi(Aceptar_Reserva)
    Aceptar_Reserva.show()
    sys.exit(app.exec_())
