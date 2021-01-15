# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Booking_AceptarReserva.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Booking_aceptarReserva(object):
    def setupUi(self, Booking_aceptarReserva):
        Booking_aceptarReserva.setObjectName("Booking_aceptarReserva")
        Booking_aceptarReserva.setWindowModality(QtCore.Qt.ApplicationModal)
        Booking_aceptarReserva.resize(452, 275)
        Booking_aceptarReserva.setStyleSheet("background-color: rgb(255, 255, 255);")
        Booking_aceptarReserva.setModal(True)
        self.aceptar = QtWidgets.QPushButton(Booking_aceptarReserva)
        self.aceptar.setGeometry(QtCore.QRect(330, 220, 89, 25))
        self.aceptar.setObjectName("aceptar")
        self.cancelar = QtWidgets.QPushButton(Booking_aceptarReserva)
        self.cancelar.setGeometry(QtCore.QRect(230, 220, 89, 25))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Booking_aceptarReserva)
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

        self.retranslateUi(Booking_aceptarReserva)
        QtCore.QMetaObject.connectSlotsByName(Booking_aceptarReserva)

    def retranslateUi(self, Booking_aceptarReserva):
        _translate = QtCore.QCoreApplication.translate
        Booking_aceptarReserva.setWindowTitle(_translate("Booking_aceptarReserva", "Reserva"))
        self.aceptar.setText(_translate("Booking_aceptarReserva", "Aceptar"))
        self.cancelar.setText(_translate("Booking_aceptarReserva", "Cancelar"))
        self.label.setText(_translate("Booking_aceptarReserva", "Precio (Dolars) = "))
        self.precio.setText(_translate("Booking_aceptarReserva", "42000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Booking_aceptarReserva = QtWidgets.QDialog()
    ui = Ui_Booking_aceptarReserva()
    ui.setupUi(Booking_aceptarReserva)
    Booking_aceptarReserva.show()
    sys.exit(app.exec_())
