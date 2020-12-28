#import requests
import json
import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
#import qdarkstyle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import uic
from PyQt5 import QtCore as qtc

#load both ui file
uifile_1 = 'UIfiles/Tab.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'UIfiles/Rutmodal.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

uifile_3 = 'UIfiles/EditUser.ui'
form_editUser, base_editUser = uic.loadUiType(uifile_3)

uifile_4 = 'UIfiles/agregarReservas.ui'
form_addR, base_addR = uic.loadUiType(uifile_4)

uifile_5 = 'UIfiles/newUser.ui'
form_newUser, base_newUser = uic.loadUiType(uifile_5)

uifile_6 = 'UIfiles/cabinsAvailables.ui'
form_available, base_available = uic.loadUiType(uifile_6)

uifile_7 = 'UIfiles/AceptarReserva.ui'
form_reserva, base_reserva = uic.loadUiType(uifile_7)


session = smtplib.SMTP('smtp.gmail.com', 587) #Me funciona declarandolo acá!


class Tabs(base_1, form_1):
    def __init__(self,*args, **kwargs):
        super(base_1, self).__init__(*args, **kwargs)
        self.setupUi(self)
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
        #self.tableWidget.vertself.tabla.veronfticalHeader().setVisible(False)icalHeader().setVisible(False)
        # Dibujar el fondo usando colores alternados
        self.tableWidget.setAlternatingRowColors(True)
        # Establecer altura de las filas
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        
        #== EVENTOS == #
        
        #--Tab calendar--#
        self.reservas_tab.clicked.connect(self.reservas)

        #--Tab customer--#
        self.deployCustomers()
        self.tableWidget.itemDoubleClicked.connect(self.doubleClickCustomer)
        self.update.clicked.connect(self.updateUser)
        self.eliminar.clicked.connect(self.remove)
        self.sendEmail.clicked.connect(self.emailSend)
        self.buscar.clicked.connect(self.searchRut)


    def reservas(self):
        self.reservas_rut = Reservas_rut()
        
        self.reservas_rut.submitted.connect(self.update_deployCustomers)
        self.reservas_rut.show()

        #self.newUser = Nuevo_usuario()
        #self.newUser.submitted2.connect(self.update_deployCustomers)
        #self.reservas_rut.show()

    
    def deployCustomers(self):
        result = requests.get('http://127.0.0.1:8007//clientes')  
        customers = result.json()['data']
        #print(customers)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(customers):
            #print(row_number)
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data.values()):
                #print(data)
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        firstUser = customers[0]
        self.rut.setText(firstUser['RUT'])
        self.nombre.setText(firstUser['Nombre'])
        self.telefono.setText(str(firstUser['Telefono']))
        self.correo.setText(firstUser['Correo'])
        self.procedencia.setText(firstUser['Procedencia'])
        self.contacto.setText(firstUser['Contacto'])

    
    @qtc.pyqtSlot(str,str,str,str,str,str)
    def update_deployCustomers(self, rut, nombre, telefono, correo, procedencia, contacto):
        self.rut.setText(rut)
        self.nombre.setText(nombre)
        self.telefono.setText(telefono)
        self.correo.setText(correo)
        self.procedencia.setText(procedencia)
        self.contacto.setText(contacto)
        
        result = requests.get('http://127.0.0.1:8007//clientes')  
        customers = result.json()['data']

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(customers):
            #print(row_number)
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data.values()):
                #print(data)
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    

    def doubleClickCustomer(self):
        
        customer = [dato.text() for dato in self.tableWidget.selectedItems()]
        
        self.rut.setText(customer[4])
        self.nombre.setText(customer[2])
        self.telefono.setText(customer[5])
        self.correo.setText(customer[1])
        self.procedencia.setText(customer[3])
        self.contacto.setText(customer[0])
    
    def updateUser(self):
        #customer = [dato.text() for dato in self.tableWidget.selectedItems()]

        rut = self.rut.text()
        nombre = self.nombre.text()
        procedencia = self.procedencia.text()
        telefono = self.telefono.text()
        correo = self.correo.text()
        contacto = self.contacto.text()

        customer = [contacto, correo, nombre, procedencia, rut, telefono]
        self.editUser = EditUser(customer)
        self.editUser.submitted.connect(self.update_deployCustomers)

        #self.newUser = Nuevo_usuario()
        #self.newUser.submitted2.connect(self.update_deployCustomers)


        self.editUser.show()
    
    def remove(self):
        rut = self.rut.text()
        print(rut)
        r = requests.delete('http://127.0.0.1:8007/clientes/{}'.format(rut))
        print(r)
        self.deployCustomers()
    
    def emailSend(self):
        def simpleSend(recver,subject,messag):
            defaultSend="igmavamailtest@gmail.com"
            defaultPass="ismabaya"
            return sendMail(defaultSend,defaultPass,recver,subject,messag)

        def sendMail(sender,sendpass,recver,subject,messag):
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = recver
            message['Subject'] = subject
            message.attach(MIMEText(messag, 'plain'))
            text = message.as_string()
            try:
                print("1")
                session = smtplib.SMTP('smtp.gmail.com', 587)
                print("2")
                session.starttls()
                print("3")
                session.login(sender, sendpass)
                session.sendmail(sender, recver, text)
                session.quit()
                QMessageBox.information(self,"", "Mensaje enviado!", QMessageBox.Ok)
                return "Correo Enviado"
            except:
                QMessageBox.warning(self,"", "Ocurrió un error!", QMessageBox.Ok)
                return "Ocurrio Error"
    
        def moroseMail(name,debt,mail):
            asunto="Importante: Comunicado sobre deuda Cabañas Igmava."
            cuerpo="""Estimado/a Sr./Sra. {},
    
            Le escribimos para comunircarle que actualmente debe el pago de ${} por su estadía.
            Le rogamos realize el deposito a la cuenta bancaria indicada lo antes posible.
            Si tiene alguna consulta puede contactarnos al telefono indicado.
    
            Cuenta: XXXX-XXXX-XXXX
            Fono: XXXX-XXXX-XXXX""".format(name,debt)
            return simpleSend(mail,asunto,cuerpo)
    
    
        result = moroseMail("Abada Kadabra",50000,"igmavamailtest@gmail.com")
        print(result)
    
    def searchRut(self):
        rut = self.search.text()
        if(rut == ''):
            self.deployCustomers()
        else:
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

        
    
class EditUser(base_editUser, form_editUser):

    submitted = qtc.pyqtSignal(str,str,str,str,str,str)

    def __init__(self, customer):
        super(base_editUser, self).__init__()
        self.setupUi(self)

        self.rut = customer[4]
        self.nombre.setText(customer[2])
        self.telefono.setText(customer[5])
        self.correo.setText(customer[1])
        self.procedencia.setText(customer[3])
        self.contacto.setText(customer[0])

        #== EVENTOS ==#

        self.aceptar.clicked.connect(self.confirmed)
    
    def confirmed(self):
        rut = self.rut
        nombre = self.nombre.text()
        procedencia = self.procedencia.text()
        telefono = self.telefono.text()
        correo = self.correo.text()
        contacto = self.contacto.text()
        customer = {'nombre': nombre, 'procedencia': procedencia, 'telefono': telefono, 'correo': correo, 'contacto': contacto}
        r = requests.put('http://127.0.0.1:8007/clientes/{}'.format(rut), json = customer)
        #FALTA VERIFICAR EL 'r' ( 200 = OK, 404 = ERROR)
        
        #print(r)
        #if(r == "<Response [200]>"):
        customer = {'RUT': rut, 'nombre': nombre, 'procedencia': procedencia, 'telefono': telefono, 'correo': correo, 'contacto': contacto}
        self.submitted.emit(rut, nombre, telefono, correo, procedencia, contacto)
        self.close()
    


class Reservas_rut(base_2, form_2):

    submitted = qtc.pyqtSignal(str,str,str,str,str,str)
    
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)


        #== EVENTOS == #
        self.reservar_rut.clicked.connect(self.reservar)
        self.nuevo_usuario.clicked.connect(self.newUser)
    
    def reservar(self):
        rut = self.rut_edit.text()
        #print(rut)
        try:
            r = requests.get('http://127.0.0.1:8007//clientes/{}'.format(rut))
            #print(r.json())
            if(r.json()['data'] == []):
                QMessageBox.information(self,"", "Usuario no existe", QMessageBox.Ok)
            else:
                customer = r.json()['data'][0]
                self.addReserve = Agregar_reserva(customer)
                self.close()
                self.addReserve.show()
        except:
            QMessageBox.information(self,"", "Ingrese rut(NO VACÍO)", QMessageBox.Ok)
    
    def newUser(self):
        self.newUsuario = Nuevo_usuario()
        self.newUsuario.submitted2.connect(self.moveData)

        self.close()
        self.newUsuario.show()
    
    @qtc.pyqtSlot(str,str,str,str,str,str)
    def moveData(self, rut, nombre, telefono, correo, procedencia, contacto):
        self.submitted.emit(rut, nombre, telefono, correo, procedencia, contacto)

        
    
class Agregar_reserva(base_addR, form_addR):
    def __init__(self, customer):
        super(base_addR, self).__init__()
        self.setupUi(self)
        self.rut = customer['RUT']
        #print(customer['Nombre'])
        self.username.setText(customer['Nombre'])
        self.rut_user.setText(customer['RUT'])

        #== EVENTOS ==#

        self.precio.clicked.connect(self.disponibilidad)
        
    
    def disponibilidad(self):
     
        #Verificar si hay reserva 

        desc = self.desc.value()
        dateCheckin = self.checkin.date().toString(Qt.ISODate)
        dateCheckout = self.checkout.date().toString(Qt.ISODate)
        r = requests.get("http://127.0.0.1:8007/disponible/{}/{}".format(dateCheckin,dateCheckout))
        result = r.json()['data'][0]['Cabins']

        self.cabinsAvailable = Cabañas_disponibles(self.rut, result, desc, dateCheckin, dateCheckout)
        self.cabinsAvailable.show()



class Cabañas_disponibles(base_available, form_available):
    def __init__(self, rut, cabins, desc, dateCheckin, dateCheckout):
        super(base_available, self).__init__()
        self.setupUi(self)
        
        self.rut = rut
        self.desc = desc
        self.cabins = cabins
        self.dateCheckin = dateCheckin
        self.dateCheckout = dateCheckout
        
        if 1 not in self.cabins:
            self.cab1.hide()
        
        if 2 not in self.cabins:
            self.cab2.hide()

        if 3 not in self.cabins:
            self.cab3.hide()
        
        if(cabins == []):
            self.label.setText("NO HAY DISPONIBILIDAD")
            self.precio.hide()


    
        # == EVENTOS == #

        self.precio.clicked.connect(self.aceptarR)
        self.cancelar.clicked.connect(self.cancel)


    def aceptarR(self):

        #--#
        self.cabs = []
        if self.cab1.isChecked() == True:
            self.cabs.append(1)
            
        if self.cab2.isChecked() == True:
            self.cabs.append(2)
            
        if self.cab3.isChecked() == True:
            self.cabs.append(3)              
        
        self.aceptarReserva = Aceptar_reserva(self.rut, self.cabs, self.desc, self.dateCheckin, self.dateCheckout)
        self.close()
        self.aceptarReserva.show()
    
    def cancel(self):
        self.close()

        

class Aceptar_reserva(base_reserva, form_reserva):
    def __init__(self, rut, cabs, desc, dateCheckin, dateCheckout):
        super(base_reserva, self).__init__()
        self.setupUi(self)

        self.rut = rut
        self.desc = desc
        self.cabs = cabs
        self.desc = desc
        self.dateCheckin = dateCheckin
        self.dateCheckout = dateCheckout


        self.totalCosto = 0
        for cab in cabs:
            #Me falta considerar los dias
            r = requests.get('http://127.0.0.1:8007//cabanas/{}'.format(cab))
            cabana = r.json()['data'][0]
            costo = cabana['Precio'] - cabana['Precio']*(desc/100)
            print(costo)
            self.totalCosto = self.totalCosto + costo

        print(self.totalCosto)
        self.precio.setText(str(self.totalCosto))

        
        # == EVENTOS == #

        self.aceptar.clicked.connect(self.aceptarReserva)
        self.cancelar.clicked.connect(self.cancel)


    def aceptarReserva(self):
        data = {'RUT': self.rut, 'in': self.dateCheckin, 'out': self.dateCheckout, 'costo': str(self.totalCosto) , 'pagado': '0', 'cabins': self.cabs}

        print(data)

        r = requests.post('http://127.0.0.1:8007//reservas', json = data)
        QMessageBox.information(self,"", "Reserva ingresada", QMessageBox.Ok)
        self.close()
    
    def cancel(self):
        self.close()

        
     

class Nuevo_usuario(base_newUser,form_newUser):

    submitted2 = qtc.pyqtSignal(str,str,str,str,str,str)

    def __init__(self):
        super(base_newUser, self).__init__()
        self.setupUi(self)

        self.aceptar.clicked.connect(self.confirmed)
    
    def confirmed(self):
        rut = self.rut.text()
        nombre = self.nombre.text()
        procedencia = self.procedencia.text()
        telefono = self.telefono.text()
        correo = self.correo.text()
        contacto = self.contacto.text()
        customer = {'RUT': rut, 'nombre': nombre, 'procedencia': procedencia, 'telefono': telefono, 'correo': correo, 'contacto': contacto}
        r = requests.post('http://127.0.0.1:8007/clientes', json = customer)
        
        customer = {'RUT': rut, 'Nombre': nombre, 'Procedencia': procedencia, 'Telefono': telefono, 'Correo': correo, 'Contacto': contacto}
        #FALTA VERIFICAR EL 'r' ( 200 = OK, 404 = ERROR)
        print(r)
        self.submitted2.emit(rut, nombre, telefono, correo, procedencia, contacto)
        self.addReserve = Agregar_reserva(customer)
        self.close()
        self.addReserve.show()
        #print(r)
        #if(r == "<Response [200]>"):

        #customer = [rut, nombre, procedencia, telefono, correo, contacto]

        #self.submitted.emit(rut, nombre, telefono, correo, procedencia, contacto)
        #self.close()
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tabs()
    ex.show()
    sys.exit(app.exec_())