# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_obsCab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_ObsCab(object):
    def setupUi(self, Add_ObsCab):
        Add_ObsCab.setObjectName("Add_ObsCab")
        Add_ObsCab.setWindowModality(QtCore.Qt.ApplicationModal)
        Add_ObsCab.resize(512, 404)
        Add_ObsCab.setStyleSheet("background-color: rgb(255, 255, 255);")
        Add_ObsCab.setModal(True)
        self.label_6 = QtWidgets.QLabel(Add_ObsCab)
        self.label_6.setGeometry(QtCore.QRect(170, 30, 291, 51))
        self.label_6.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.aceptar = QtWidgets.QPushButton(Add_ObsCab)
        self.aceptar.setGeometry(QtCore.QRect(290, 270, 131, 41))
        self.aceptar.setObjectName("aceptar")
        self.cancelar = QtWidgets.QPushButton(Add_ObsCab)
        self.cancelar.setGeometry(QtCore.QRect(130, 270, 131, 41))
        self.cancelar.setObjectName("cancelar")
        self.gridLayoutWidget = QtWidgets.QWidget(Add_ObsCab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 100, 441, 121))
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

        self.retranslateUi(Add_ObsCab)
        QtCore.QMetaObject.connectSlotsByName(Add_ObsCab)
        Add_ObsCab.setTabOrder(self.tipo, self.descripcion)
        Add_ObsCab.setTabOrder(self.descripcion, self.aceptar)
        Add_ObsCab.setTabOrder(self.aceptar, self.cancelar)

    def retranslateUi(self, Add_ObsCab):
        _translate = QtCore.QCoreApplication.translate
        Add_ObsCab.setWindowTitle(_translate("Add_ObsCab", "Observación Cabaña"))
        self.label_6.setText(_translate("Add_ObsCab", "Observación"))
        self.aceptar.setText(_translate("Add_ObsCab", "Aceptar"))
        self.cancelar.setText(_translate("Add_ObsCab", "Cancelar"))
        self.label_2.setText(_translate("Add_ObsCab", "       Tipo:"))
        self.label_3.setText(_translate("Add_ObsCab", "Descripción:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_ObsCab = QtWidgets.QDialog()
    ui = Ui_Add_ObsCab()
    ui.setupUi(Add_ObsCab)
    Add_ObsCab.show()
    sys.exit(app.exec_())
