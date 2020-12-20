import requests
import json
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets#works for pyqt5
import qdarkstyle

class Reservas(QtWidgets.QWidget):
    def __init__(self):
         #super().__init__()
         super().__init__()

         self.setWindowTitle("Reservas IGMAVA")

         #buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) Pop-up
         
         self.groupBoxCab = QtWidgets.QGroupBox("Cabaña")
         self.cab1 = QtWidgets.QCheckBox("1")
         self.cab2 = QtWidgets.QCheckBox("2")
         self.cab3 = QtWidgets.QCheckBox("3")
        
         self.hbox = QtWidgets.QHBoxLayout()
         self.hbox.addWidget(self.cab1)
         self.hbox.addWidget(self.cab2)
         self.hbox.addWidget(self.cab3)

         self.groupBoxCab.setLayout(self.hbox)
         
         #---
        
         self.groupBoxCliente= QtWidgets.QGroupBox("Cliente")

         self.cliente = QtWidgets.QLineEdit()

        
         self.hbox2 = QtWidgets.QHBoxLayout()
         self.hbox2.addWidget(self.cliente)

         self.groupBoxCliente.setLayout(self.hbox2)

        
         #-- 

         self.groupBoxRut= QtWidgets.QGroupBox("Rut")

         self.rut = QtWidgets.QLineEdit()
        
         self.hbox3 = QtWidgets.QHBoxLayout()
         self.hbox3.addWidget(self.rut)

         self.groupBoxRut.setLayout(self.hbox3)

         #-- 

         self.groupBoxFecha= QtWidgets.QGroupBox("Fecha")
         #self.groupBoxCheckout= QtWidgets.QGroupBox("Checkout")

         self.checkin = QtWidgets.QCalendarWidget()
         self.checkout = QtWidgets.QCalendarWidget()
         
         self.groupBoxCheInOut = QtWidgets.QHBoxLayout()
         self.groupBoxCheInOut.addWidget(self.checkin)
         self.groupBoxCheInOut.addWidget(self.checkout)

         self.groupBoxFecha.setLayout(self.groupBoxCheInOut)
         
         
         
         self.save = QtWidgets.QPushButton("Guardar")
         self.cancel = QtWidgets.QPushButton("Cancelar")
        
         #GUARDAR 
         self.save.clicked.connect(self.saveReservas)


         self.hbox4 = QtWidgets.QVBoxLayout()
         
         self.hbox41= QtWidgets.QHBoxLayout()
         self.hbox41.addWidget(self.save)
         self.hbox41.addWidget(self.cancel)

         self.hbox4.addWidget(self.groupBoxFecha)

         #-- 

         self.hbox5 = QtWidgets.QHBoxLayout()

         self.precioLabel = QtWidgets.QLabel("Precio")
         self.precio = QtWidgets.QLineEdit()

         self.hbox5.addWidget(self.precioLabel)
         self.hbox5.addWidget(self.precio)

         self.hbox6= QtWidgets.QHBoxLayout()
         self.hbox6.addWidget(self.groupBoxFecha)
         self.hbox6.addLayout(self.hbox5)
         
         #-- 
         self.hbox7 = QtWidgets.QVBoxLayout()
         self.hbox7.addLayout(self.hbox6)
         self.hbox7.addLayout(self.hbox41)


         self.mainLayout = QtWidgets.QVBoxLayout()
         self.mainLayout.addWidget(self.groupBoxCab)
         self.mainLayout.addWidget(self.groupBoxCliente)
         self.mainLayout.addWidget(self.groupBoxRut)
         self.mainLayout.addLayout(self.hbox7)
         #mainLayout.addStretch()
        
         self.setLayout(self.mainLayout)

    def saveReservas(self):
         r = requests.get('http://127.0.0.1:8007//reservas/1')

         
         print(r.json()['data'])


             

class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        #QMainWindow.__init__(self)
        self.resize(800, 600)
        self.setWindowTitle("IGMAVA")
        self.setWindowIcon(QIcon("myicon.png"))

        #self.showMaximized()
        self.setMinimumSize(500, 500)
        #Fijar el tamaño máximo
        self.setMaximumSize(800, 600)

        tabwidget = QtWidgets.QTabWidget()
        tabwidget.addTab(FirstTab(), "Calendario")
        tabwidget.addTab(SecondTab(), "Clientes")
        tabwidget.addTab(ThirdTab(), "Cabañas")

        #buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        #buttonbox.accepted.connect(self)

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)
        #vbox.addWidget(buttonbox)

        self.setLayout(vbox)


class FirstTab(QWidget):
    def __init__(self):
        super().__init__() 
        
        self.calender = QtWidgets.QCalendarWidget() 

        self.button = QtWidgets.QPushButton()
        self.button.setText("Añadir reserva ")
        self.button.clicked.connect(self.Reserva)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.calender)
        self.layout.addWidget(self.button)
        #layout.addWidget(name)
        #layout.addWidget(nameEdit)
        self.setLayout(self.layout)

        '''dob = QLabel("Birth day: ")
        dobEdit = QLineEdit()

        age = QLabel("Birth day: ")
        ageEdit = QLineEdit()

        phone = QLabel("Birth day: ")
        phoneEdit = QLineEdit()


        layout = QVBoxLayout()
        layout.addWidget(name)
        layout.addWidget(nameEdit)
        layout.addWidget(dob)
        layout.addWidget(dobEdit)
        layout.addWidget(age)
        layout.addWidget(ageEdit)
        layout.addWidget(phone)
        layout.addWidget(phoneEdit)
        
        self.setLayout(layout)'''
    def Reserva(self):
         self.tabs = TabWidget()
         self.tabs.hide()
         self.main = Reservas()
         self.main.show()



class SecondTab(QWidget):
    def __init__(self):
        super().__init__()


        search = QLineEdit()
        search.setObjectName("buscador")
        search.setText("Buscar")
        botom = QtWidgets.QPushButton()
        botom.setObjectName("botom")
        botom.setText("Search")

        self.tableWidget = QTableWidget()
        #self.tableWidget.setRowCount(1000)  
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels("Contacto;Correo;Nombre;Procedencia;RUT;Telefono".split(";"))
        #self.tableWidget.horizontalHeaderItem().setTextAlignment(Qt.AlignHCenter)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        


        layout = QVBoxLayout()
        
        layoutH = QHBoxLayout()
        layoutH.addWidget(search)
        layoutH.addWidget(botom)

        layoutV = QVBoxLayout()
        layoutV.addWidget(self.tableWidget)

        layout.addLayout(layoutH)
        layout.addLayout(layoutV)
        self.setLayout(layout)

        self.despliegue()
    
    def despliegue(self):
        result = requests.get('http://127.0.0.1:8007//clientes')       
        customers = result.json()['data']
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(customers):
            #print(row_number)
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data.values()):
                #print(data)
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

        """selectGroup = QGroupBox("Select Operatig Systems")
        combo = QComboBox()
        list =  ["Windows", "Mac", "Linux", "Fedora", "Kali"]
        combo.addItems(list)
        selectLayout = QVBoxLayout()
        selectLayout.addWidget(combo)
        selectGroup.setLayout(selectLayout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(selectGroup)
        self.setLayout(mainLayout)"""






app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
tabwidget = TabWidget()
tabwidget.show()
app.exec()
