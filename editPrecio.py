# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editPrecio.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editPrecio(object):
    def setupUi(self, editPrecio):
        editPrecio.setObjectName("editPrecio")
        editPrecio.resize(576, 247)
        editPrecio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.confirmar = QtWidgets.QPushButton(editPrecio)
        self.confirmar.setGeometry(QtCore.QRect(430, 180, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmar.sizePolicy().hasHeightForWidth())
        self.confirmar.setSizePolicy(sizePolicy)
        self.confirmar.setStyleSheet("background-color: #3B83BD;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.confirmar.setObjectName("confirmar")
        self.cancelar = QtWidgets.QPushButton(editPrecio)
        self.cancelar.setGeometry(QtCore.QRect(270, 180, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelar.sizePolicy().hasHeightForWidth())
        self.cancelar.setSizePolicy(sizePolicy)
        self.cancelar.setStyleSheet("background-color: #FF0000;\n"
"font-size: 18px;\n"
"/*border-radius: 8px;*/\n"
"color: #FFFFFF;")
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(editPrecio)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 10, 201, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.precio_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.precio_label.sizePolicy().hasHeightForWidth())
        self.precio_label.setSizePolicy(sizePolicy)
        self.precio_label.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.precio_label.setObjectName("precio_label")
        self.horizontalLayout.addWidget(self.precio_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(editPrecio)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 80, 331, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 57 14pt \"Ubuntu\";\n"
"font-weight:bold;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.precio = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.precio.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.precio.setMaximum(1000)
        self.precio.setProperty("value", 50)
        self.precio.setObjectName("precio")
        self.horizontalLayout_2.addWidget(self.precio)

        self.retranslateUi(editPrecio)
        QtCore.QMetaObject.connectSlotsByName(editPrecio)

    def retranslateUi(self, editPrecio):
        _translate = QtCore.QCoreApplication.translate
        editPrecio.setWindowTitle(_translate("editPrecio", "Editar precio"))
        self.confirmar.setText(_translate("editPrecio", "Confirmar"))
        self.cancelar.setText(_translate("editPrecio", "Cancelar"))
        self.label_4.setText(_translate("editPrecio", "Precio actual:"))
        self.precio_label.setText(_translate("editPrecio", "50"))
        self.label_5.setText(_translate("editPrecio", "Nuevo precio: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editPrecio = QtWidgets.QDialog()
    ui = Ui_editPrecio()
    ui.setupUi(editPrecio)
    editPrecio.show()
    sys.exit(app.exec_())
