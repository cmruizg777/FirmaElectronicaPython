# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from helpers.xades.xades import Xades
from model import Modulo11
from db.Connection import Connection
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import os
import sys
def Modulo11(modulo11: Modulo11):

    suma = 0
    factor = 7

    claveAcceso = (
                    modulo11.Fecha.ToString("ddMMyyyy") +
                    modulo11.TipoComprobante +
                    modulo11.RucEmpresa +
                    modulo11.Ambiente +
                    modulo11.PtoEmision +
                    modulo11.Sucursal +
                    modulo11.Secuencial +
                    modulo11.Digito8 +
                    "1"
                    )

    for item in claveAcceso:
        suma = suma + int(item.ToString()) * factor
        factor = factor - 1
        if (factor == 1):
            factor = 7

    digitoVerificador = (suma % 11)
    digitoVerificador = 11 - digitoVerificador

    if (digitoVerificador == 11):
        digitoVerificador = 0

    if (digitoVerificador == 10):
        digitoVerificador = 1

    return claveAcceso + digitoVerificador



#file_p12 = open('diegop.P12',encoding="utf8", errors='ignore')
file_p12 = 'cs.p12'
#p12Content = file_p12.read()
password = '1091725041001'
#file_xml = open('documento.xml', encoding="utf8")
xml_document = 'documento.xml'
#xmlContent = file_xml.read()
xml_signed = 'firmado.xml'
xades = Xades()
xades.sign(xml_document,xml_signed,file_p12, password)

#connection = Connection()
#cursor.execute("SELECT LastName FROM myContacts")
#while 1:
#    row = cursor.fetchone()
#    if not row:
#        break
#    print(row.LastName)