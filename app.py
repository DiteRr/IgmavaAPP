import requests
import json
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets#works for pyqt5
import qdarkstyle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Reservas(QtWidgets.QWidget):
    def __init__(self):
         #super().__init__()
         super().__init__()
         self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
         self.setFixedSize(700, 500)

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

         self.cliente = QtWidgets.QLineEdit("hola")

        
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
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(700, 500)
        #self.resize(800, 600)
        self.setWindowTitle("IGMAVA")
        self.setWindowIcon(QIcon("myicon.png"))

        #self.showMaximized()
        self.setMinimumSize(500, 500)
        #Fijar el tamaño máximo
        self.setMaximumSize(800, 600)

        self.tabwidget = QtWidgets.QTabWidget()
        self.tabwidget.addTab(FirstTab(), "Calendario")
        self.tabwidget.addTab(SecondTab(), "Clientes")
        self.tabwidget.addTab(ThirdTab(), "Cabañas")

        #buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        #buttonbox.accepted.connect(self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.tabwidget)
        #vbox.addWidget(buttonbox)

        self.setLayout(self.vbox)


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
        self.setLayout(self.layout)
    
    def Reserva(self):
         self.tabs = TabWidget()
         self.tabs.hide()
         self.main = Reservas()
         self.main.show()


class SecondTab(QWidget):
    def __init__(self):
        super().__init__()


        self.search = QLineEdit()
        self.search.setObjectName("buscador")
        self.botom = QtWidgets.QPushButton()
        self.botom.setObjectName("botom")
        self.botom.setText("Search")

        self.tableWidget = QTableWidget()
        # Establecer el número de columnas
        self.tableWidget.setColumnCount(6)
        # Establecer el número de filas
        self.tableWidget.setRowCount(0)       
        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tableWidget.setHorizontalHeaderLabels("Contacto;Correo;Nombre;Procedencia;RUT;Telefono".split(";"))        
        # Deshabilitar edición
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Seleccionar toda la fila
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Seleccionar una fila a la vez
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tableWidget.setTextElideMode(Qt.ElideRight)# Qt.ElideNone
        # Establecer el ajuste de palabrasineEdit del texto 
        self.tableWidget.setWordWrap(False)
        # Deshabilitar clasificación
        self.tableWidget.setSortingEnabled(False)
        # Establecer el número de columnas
        self.tableWidget.setColumnCount(6)
        # Alineación del texto del encabezado
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # Ocultar encabezado vertical
        #self.tableWidget.vertself.tabla.verticalHeader().setVisible(False)icalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.tableWidget.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        

        # Layouts #
        self.layout = QVBoxLayout()
        
        self.layoutH = QHBoxLayout()
        self.layoutH.addWidget(self.search)
        self.layoutH.addWidget(self.botom)

        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.tableWidget)

        self.layout.addLayout(self.layoutH)
        self.layout.addLayout(self.layoutV)
        self.setLayout(self.layout)

        # == EVENTOS == #

        self.despliegue()
        self.tableWidget.itemDoubleClicked.connect(self.clienteParticular)
        self.botom.clicked.connect(self.searchRut)

        # Menú contextual
        #self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.tableWidget.customContextMenuRequested.connect(self.menuContextual)
    
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
    
    def searchRut(self):
        rut = self.search.text()
        try:
            r = requests.get('http://127.0.0.1:8007//clientes/{}'.format(rut))
            customer = r.json()['data'][0]
            #print(customer)
            self.tableWidget.setRowCount(1) 
            self.tableWidget.setItem(0, 0, QTableWidgetItem(customer['Contacto']))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(customer['Correo']))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(customer['Nombre']))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(customer['Procedencia']))
            self.tableWidget.setItem(0, 4, QTableWidgetItem(customer['RUT']))
            self.tableWidget.setItem(0, 5, QTableWidgetItem(str(customer['Telefono'])))
        except:
             print("Rut inexistente")

    
    def clienteParticular(self, celda):
        self.tab = TabWidget()
        self.tab.hide()
        self.hide()
        
        customer = [dato.text() for dato in self.tableWidget.selectedItems()]
        print(customer[3])
        self.viewCustomer = ViewCustomer(customer)       
        self.viewCustomer.show()

        #filaSeleccionada = [dato.text() for dato in self.tableWidget.selectedItems()]
        #print(filaSeleccionada)
        #QMessageBox.warning(self, "Probando", filaSeleccionada + ", celda seleccionada {}.   ".format(celda.text()), QMessageBox.Ok)

class ViewCustomer(QWidget):
    def __init__(self, customer):
        super().__init__()
        self.setFixedSize(700, 500)
        self.customer = customer
        #print(self.customer)
        self.setWindowTitle("Customer")
        
        #--#
        self.mainLayout = QVBoxLayout()

        self.tableCustomer = QTableWidget()

        self.tableCustomer.setColumnCount(6)
        self.tableCustomer.setRowCount(1)
        
        self.tableCustomer.setHorizontalHeaderLabels("Contacto;Correo;Nombre;Procedencia;RUT;Telefono".split(";"))
        self.tableCustomer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCustomer.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableCustomer.setTextElideMode(Qt.ElideRight)
        self.tableCustomer.setWordWrap(False)
        self.tableCustomer.setSortingEnabled(False)
        self.tableCustomer.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)
        self.tableCustomer.horizontalHeader().setHighlightSections(False)
        self.tableCustomer.setAlternatingRowColors(True)
        self.tableCustomer.verticalHeader().setVisible(False)
        self.tableCustomer.verticalHeader().setDefaultSectionSize(180)


        #--# Table customer
        self.tableCustomer.setItem(0, 0, QTableWidgetItem(self.customer[0]))
        self.tableCustomer.setItem(0, 1, QTableWidgetItem(self.customer[1]))
        self.tableCustomer.setItem(0, 2, QTableWidgetItem(self.customer[2]))
        self.tableCustomer.setItem(0, 3, QTableWidgetItem(self.customer[3]))
        self.tableCustomer.setItem(0, 4, QTableWidgetItem(self.customer[4]))
        self.tableCustomer.setItem(0, 5, QTableWidgetItem(self.customer[5]))

        #--#Loading
        
        self.label_animation =  QLabel(self)
        self.movie = QMovie('Loading_2.gif')
        self.label_animation.setMovie(self.movie)


        #--# Buttons
        self.edit = QtWidgets.QPushButton("Editar")
        self.sendEmail = QtWidgets.QPushButton("Enviar Correo")
        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.addWidget(self.edit)
        self.layoutButtons.addWidget(self.sendEmail)

        #--# Layout TableWidget and buttons

        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.tableCustomer)
        self.layoutV.addLayout(self.layoutButtons)
        #self.layoutV.addWidget(self.label_animation)
        
        #--# GroupBoxFecha
        self.checkinC = QtWidgets.QCalendarWidget()
        self.checkoutC = QtWidgets.QCalendarWidget()
        self.añadir = QtWidgets.QPushButton("Añadir reserva")
         
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.checkinC)
        self.layout1.addWidget(self.checkoutC)

        self.layout2 = QVBoxLayout()
        self.layout2.addLayout(self.layout1)
        self.layout2.addWidget(self.añadir) 
        
        self.groupBoxFechaC= QtWidgets.QGroupBox("Añadir reserva") 
        self.groupBoxFechaC.setLayout(self.layout2)

        #--# Unite all

        self.mainLayout.addLayout(self.layoutV)
        self.mainLayout.addWidget(self.groupBoxFechaC)
        self.setLayout(self.mainLayout)


        #==EVENTOS==#

        self.edit.clicked.connect(self.editCustomer)
        self.sendEmail.clicked.connect(self.emailSend)

    def editCustomer(self):
        self.hide()
        self.editC = EditCustomer(self.customer)   
        self.editC.show()
    
    def emailSend(self):
        
        def simpleSend(recver,subject,messag):
            defaultSend="igmavamailtest@gmail.com"
            defaultPass="ismabaya"
            sendMail(defaultSend,defaultPass,recver,subject,messag)

        def sendMail(sender,sendpass,recver,subject,messag):
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = recver
            message['Subject'] = subject
            message.attach(MIMEText(messag, 'plain'))
            text = message.as_string()
            try:
                session = smtplib.SMTP('smtp.gmail.com', 587)
                session.starttls()
                session.login(sender, sendpass)
                session.sendmail(sender, recver, text)
                session.quit()
                self.movie.stop()
                QMessageBox.warning(self, "", "¡ Correo enviado !", QMessageBox.Ok)
            except:
                self.movie.stop()
                QMessageBox.warning(self, "", "¡ Ocurrio un error !",QMessageBox.Ok)
           
        def moroseMail(name,debt,mail):
            asunto="Importante: Comunicado sobre deuda Cabañas Igmava."
            cuerpo="""Estimado/a Sr./Sra. {},
    
            Le escribimos para comunircarle que actualmente debe el pago de ${} por su estadía.
            Le rogamos realize el deposito a la cuenta bancaria indicada lo antes posible.
            Si tiene alguna consulta puede contactarnos al telefono indicado.
    
            Cuenta: XXXX-XXXX-XXXX
            Fono: XXXX-XXXX-XXXX""".format(name,debt)
            simpleSend(mail,asunto,cuerpo)
    
        self.movie.start()
        moroseMail("Abada Kadabra",50000,"igmavamailtest@gmail.com")
    

class EditCustomer(QWidget):
    def __init__(self, customer):
        super().__init__()
        self.setFixedSize(700, 500)
        self.setWindowTitle("Editar cliente")
        self.customer = customer
        self.rut = customer[4]
        #print(self.rut)
        #print(customer)
        #--#
        self.nombreC= QtWidgets.QGroupBox("Nombre")
        self.nombre= QtWidgets.QLineEdit(customer[2])
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.nombre)
        self.nombreC.setLayout(self.layout1)


        self.proceC= QtWidgets.QGroupBox("Procedencia")
        self.proce = QtWidgets.QLineEdit(customer[3]) 
        self.layout3 = QHBoxLayout()
        self.layout3.addWidget(self.proce)
        self.proceC.setLayout(self.layout3)

        self.telefonoC= QtWidgets.QGroupBox("Telefono") 
        self.telefono = QtWidgets.QLineEdit(customer[5])
        self.layout4 = QHBoxLayout()
        self.layout4.addWidget(self.telefono)
        self.telefonoC.setLayout(self.layout4)

        self.correoC= QtWidgets.QGroupBox("Correo")
        self.correo = QtWidgets.QLineEdit(customer[1])
        self.layout5 = QHBoxLayout()
        self.layout5.addWidget(self.correo)
        self.correoC.setLayout(self.layout5)
        
        self.contactoC= QtWidgets.QGroupBox("Contacto")
        self.contacto = QtWidgets.QLineEdit(customer[0])
        self.layout6 = QHBoxLayout()
        self.layout6.addWidget(self.contacto)
        self.contactoC.setLayout(self.layout6)
        
        #--# buttons

        self.save = QtWidgets.QPushButton("Guardar")
        self.cancel = QtWidgets.QPushButton("Cancelar")
        self.layoutButtons = QHBoxLayout()
        self.layoutButtons.addWidget(self.save)
        self.layoutButtons.addWidget(self.cancel)



        self.mainlayout = QVBoxLayout()
        
        self.mainlayout.addWidget(self.nombreC)
        self.mainlayout.addWidget(self.proceC)
        self.mainlayout.addWidget(self.telefonoC)
        self.mainlayout.addWidget(self.correoC)
        self.mainlayout.addWidget(self.contactoC)
        self.mainlayout.addLayout(self.layoutButtons)

        self.setLayout(self.mainlayout)

         # == EVENTOS == #
        
        self.save.clicked.connect(self.saveChanges)
        self.cancel.clicked.connect(self.canceled)

    def canceled(self):
        
        self.hide()
        self.viewCustomer = ViewCustomer(self.customer)
        self.viewCustomer.show()
    
    def saveChanges(self):
        rut = self.rut
        nombre = self.nombre.text()
        procedencia = self.proce.text()
        telefono = self.telefono.text()
        correo = self.correo.text()
        contacto = self.contacto.text()
        customer = {'nombre': nombre, 'procedencia': procedencia, 'telefono': telefono, 'correo': correo, 'contacto': contacto}
        r = requests.put('http://127.0.0.1:8007/clientes/{}'.format(rut), json = customer)
        #print(r)
        #if(r == "<Response [200]>"):
        self.customer[0] = contacto 
        self.customer[1] = correo
        self.customer[2] = nombre
        self.customer[3] = procedencia
        self.customer[5] = telefono
            
        self.hide()
        self.viewCustomer = ViewCustomer(self.customer)
        self.viewCustomer.show()
         
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
