# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obsCab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_obsCab(object):
    def setupUi(self, obsCab):
        obsCab.setObjectName("obsCab")
        obsCab.resize(749, 620)
        obsCab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.obs = QtWidgets.QTableWidget(obsCab)
        self.obs.setGeometry(QtCore.QRect(30, 110, 691, 321))
        self.obs.setObjectName("obs")
        self.obs.setColumnCount(0)
        self.obs.setRowCount(0)
        self.deshabilitar = QtWidgets.QPushButton(obsCab)
        self.deshabilitar.setGeometry(QtCore.QRect(510, 450, 191, 51))
        self.deshabilitar.setStyleSheet("background-color: #FF0000;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.deshabilitar.setObjectName("deshabilitar")
        self.add_obs = QtWidgets.QPushButton(obsCab)
        self.add_obs.setGeometry(QtCore.QRect(300, 450, 201, 51))
        self.add_obs.setStyleSheet("background-color: #3B83BD;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.add_obs.setObjectName("add_obs")
        self.label_3 = QtWidgets.QLabel(obsCab)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 57 18pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(obsCab)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 139, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(obsCab)
        QtCore.QMetaObject.connectSlotsByName(obsCab)

    def retranslateUi(self, obsCab):
        _translate = QtCore.QCoreApplication.translate
        obsCab.setWindowTitle(_translate("obsCab", "Observaciones cabaña"))
        self.deshabilitar.setText(_translate("obsCab", "Deshabilitar cabaña"))
        self.add_obs.setText(_translate("obsCab", "Agregar observación"))
        self.label_3.setText(_translate("obsCab", "Cabaña"))
        self.label_5.setText(_translate("obsCab", "Observaciones:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obsCab = QtWidgets.QWidget()
    ui = Ui_obsCab()
    ui.setupUi(obsCab)
    obsCab.show()
    sys.exit(app.exec_())
