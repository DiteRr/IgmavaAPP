# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editBooking.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editBooking(object):
    def setupUi(self, editBooking):
        editBooking.setObjectName("editBooking")
        editBooking.setWindowModality(QtCore.Qt.ApplicationModal)
        editBooking.resize(553, 552)
        editBooking.setStyleSheet("background-color: rgb(255, 255, 255);")
        editBooking.setModal(True)
        self.groupBox = QtWidgets.QGroupBox(editBooking)
        self.groupBox.setGeometry(QtCore.QRect(40, 100, 471, 101))
        self.groupBox.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.rut_user = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rut_user.sizePolicy().hasHeightForWidth())
        self.rut_user.setSizePolicy(sizePolicy)
        self.rut_user.setObjectName("rut_user")
        self.horizontalLayout_5.addWidget(self.rut_user)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(editBooking)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 220, 461, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.checkout = QtWidgets.QDateEdit(self.horizontalLayoutWidget_2)
        self.checkout.setStyleSheet("background-color : #CDCDCD;\n"
"color: rgb(0,0,0);")
        self.checkout.setCalendarPopup(True)
        self.checkout.setDate(QtCore.QDate(2020, 12, 28))
        self.checkout.setObjectName("checkout")
        self.horizontalLayout_2.addWidget(self.checkout)
        self.precio = QtWidgets.QPushButton(editBooking)
        self.precio.setGeometry(QtCore.QRect(400, 440, 121, 51))
        self.precio.setObjectName("precio")
        self.label_6 = QtWidgets.QLabel(editBooking)
        self.label_6.setGeometry(QtCore.QRect(200, 50, 171, 31))
        self.label_6.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.cancelar = QtWidgets.QPushButton(editBooking)
        self.cancelar.setGeometry(QtCore.QRect(270, 440, 111, 51))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(editBooking)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 330, 188, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setStyleSheet("font: 57 11pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.desc = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.desc.setObjectName("desc")
        self.horizontalLayout_3.addWidget(self.desc)

        self.retranslateUi(editBooking)
        QtCore.QMetaObject.connectSlotsByName(editBooking)
        editBooking.setTabOrder(self.checkin, self.checkout)
        editBooking.setTabOrder(self.checkout, self.desc)
        editBooking.setTabOrder(self.desc, self.precio)
        editBooking.setTabOrder(self.precio, self.cancelar)

    def retranslateUi(self, editBooking):
        _translate = QtCore.QCoreApplication.translate
        editBooking.setWindowTitle(_translate("editBooking", "Editar reserva"))
        self.groupBox.setTitle(_translate("editBooking", "Cliente "))
        self.label_3.setText(_translate("editBooking", "Rut :"))
        self.rut_user.setText(_translate("editBooking", "Rut user"))
        self.label_4.setText(_translate("editBooking", "Check-In"))
        self.label.setText(_translate("editBooking", "Check-Out"))
        self.precio.setText(_translate("editBooking", "Disponibilidad"))
        self.label_6.setText(_translate("editBooking", "Editar Reserva "))
        self.cancelar.setText(_translate("editBooking", "Cancelar"))
        self.label_5.setText(_translate("editBooking", "Descuento %"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editBooking = QtWidgets.QDialog()
    ui = Ui_editBooking()
    ui.setupUi(editBooking)
    editBooking.show()
    sys.exit(app.exec_())
