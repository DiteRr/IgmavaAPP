# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserBooking.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserBooking(object):
    def setupUi(self, UserBooking):
        UserBooking.setObjectName("UserBooking")
        UserBooking.resize(877, 572)
        UserBooking.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(UserBooking)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reservasRUT = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reservasRUT.sizePolicy().hasHeightForWidth())
        self.reservasRUT.setSizePolicy(sizePolicy)
        self.reservasRUT.setObjectName("reservasRUT")
        self.reservasRUT.setColumnCount(0)
        self.reservasRUT.setRowCount(0)
        self.verticalLayout_2.addWidget(self.reservasRUT)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 2, 1, 1, 1)
        self.check_out = QtWidgets.QLabel(self.centralwidget)
        self.check_out.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.check_out.setObjectName("check_out")
        self.gridLayout_4.addWidget(self.check_out, 3, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 3, 1, 1, 1)
        self.costo = QtWidgets.QLabel(self.centralwidget)
        self.costo.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.costo.setObjectName("costo")
        self.gridLayout_4.addWidget(self.costo, 5, 2, 1, 1)
        self.pagado = QtWidgets.QLabel(self.centralwidget)
        self.pagado.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.pagado.setObjectName("pagado")
        self.gridLayout_4.addWidget(self.pagado, 4, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 3, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 1, 1, 1)
        self.rut = QtWidgets.QLabel(self.centralwidget)
        self.rut.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.rut.setObjectName("rut")
        self.gridLayout_4.addWidget(self.rut, 1, 2, 1, 1)
        self.check_in = QtWidgets.QLabel(self.centralwidget)
        self.check_in.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.check_in.setObjectName("check_in")
        self.gridLayout_4.addWidget(self.check_in, 2, 2, 1, 1)
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.id.setObjectName("id")
        self.gridLayout_4.addWidget(self.id, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 4, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.editarReserva = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editarReserva.sizePolicy().hasHeightForWidth())
        self.editarReserva.setSizePolicy(sizePolicy)
        self.editarReserva.setStyleSheet("background-color: #00BB2D;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.editarReserva.setObjectName("editarReserva")
        self.horizontalLayout_4.addWidget(self.editarReserva)
        self.eliminarReserva = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eliminarReserva.sizePolicy().hasHeightForWidth())
        self.eliminarReserva.setSizePolicy(sizePolicy)
        self.eliminarReserva.setStyleSheet("background-color: #FF0000;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.eliminarReserva.setObjectName("eliminarReserva")
        self.horizontalLayout_4.addWidget(self.eliminarReserva)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        UserBooking.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UserBooking)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 22))
        self.menubar.setObjectName("menubar")
        UserBooking.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UserBooking)
        self.statusbar.setObjectName("statusbar")
        UserBooking.setStatusBar(self.statusbar)

        self.retranslateUi(UserBooking)
        QtCore.QMetaObject.connectSlotsByName(UserBooking)

    def retranslateUi(self, UserBooking):
        _translate = QtCore.QCoreApplication.translate
        UserBooking.setWindowTitle(_translate("UserBooking", "Reservas usuario"))
        self.label_19.setText(_translate("UserBooking", "Check-out"))
        self.check_out.setText(_translate("UserBooking", "21/03/2021"))
        self.label_21.setText(_translate("UserBooking", "Check-in"))
        self.costo.setText(_translate("UserBooking", "30"))
        self.pagado.setText(_translate("UserBooking", "1"))
        self.label_23.setText(_translate("UserBooking", "Costo"))
        self.label.setText(_translate("UserBooking", "ID:"))
        self.label_17.setText(_translate("UserBooking", "Rut:"))
        self.rut.setText(_translate("UserBooking", "19358005-k"))
        self.check_in.setText(_translate("UserBooking", "20/03/2021"))
        self.id.setText(_translate("UserBooking", "1"))
        self.label_25.setText(_translate("UserBooking", "Pagado"))
        self.editarReserva.setText(_translate("UserBooking", "Editar reserva"))
        self.eliminarReserva.setText(_translate("UserBooking", "Eliminar reserva"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserBooking = QtWidgets.QMainWindow()
    ui = Ui_UserBooking()
    ui.setupUi(UserBooking)
    UserBooking.show()
    sys.exit(app.exec_())
