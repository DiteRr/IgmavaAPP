# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rutmodal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rutmodal(object):
    def setupUi(self, Rutmodal):
        Rutmodal.setObjectName("Rutmodal")
        Rutmodal.setWindowModality(QtCore.Qt.ApplicationModal)
        Rutmodal.resize(535, 365)
        Rutmodal.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.nuevo_usuario = QtWidgets.QPushButton(Rutmodal)
        self.nuevo_usuario.setGeometry(QtCore.QRect(60, 250, 401, 41))
        self.nuevo_usuario.setStyleSheet("background-color: #CDCDCD;\n"
"font: 25 11pt \"Ubuntu\";\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/")
        self.nuevo_usuario.setObjectName("nuevo_usuario")
        self.rut_edit = QtWidgets.QLineEdit(Rutmodal)
        self.rut_edit.setGeometry(QtCore.QRect(110, 100, 351, 31))
        self.rut_edit.setObjectName("rut_edit")
        self.label_3 = QtWidgets.QLabel(Rutmodal)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.reservar_rut = QtWidgets.QPushButton(Rutmodal)
        self.reservar_rut.setGeometry(QtCore.QRect(60, 190, 401, 41))
        self.reservar_rut.setStyleSheet("background-color: #3B83BD;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.reservar_rut.setObjectName("reservar_rut")

        self.retranslateUi(Rutmodal)
        QtCore.QMetaObject.connectSlotsByName(Rutmodal)
        Rutmodal.setTabOrder(self.rut_edit, self.reservar_rut)
        Rutmodal.setTabOrder(self.reservar_rut, self.nuevo_usuario)

    def retranslateUi(self, Rutmodal):
        _translate = QtCore.QCoreApplication.translate
        Rutmodal.setWindowTitle(_translate("Rutmodal", "Rut usuario"))
        self.nuevo_usuario.setText(_translate("Rutmodal", "Nuevo usuario"))
        self.label_3.setText(_translate("Rutmodal", "RUT : "))
        self.reservar_rut.setText(_translate("Rutmodal", "Reservar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rutmodal = QtWidgets.QDialog()
    ui = Ui_Rutmodal()
    ui.setupUi(Rutmodal)
    Rutmodal.show()
    sys.exit(app.exec_())
