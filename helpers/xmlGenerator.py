import xml.etree.cElementTree as ET
import datetime
from helpers.Module11 import Module11


class xmlGenerator():

    def __init__(self):
        print('xml generator')



    def generateRemissionGuideXml(self, data):
        infoTributariaEmpresa = data[0][0]
        infoTributariaSecuenciales = data[1][0]
        infoTransportista = data[2][0]
        infoDestinatario = data[3][0]
        infoDetalles = data[4]
        secuencialLength = len(str(infoTributariaSecuenciales[6]))
        zeros = ""

        for i in range(9-secuencialLength):
            zeros += "0"

        secuencial = zeros + str(infoTributariaSecuenciales[6])
        ptoEmision = infoTributariaSecuenciales[4]
        sucursal = infoTributariaSecuenciales[5]  # sucursal
        print(secuencial)
        fecha = datetime.datetime.strptime(infoTributariaSecuenciales[7], '%d/%m/%Y').date()

        mod11 = Module11(
            fecha,                      #fecha
            "06",                       #tipoComprobante
            infoTributariaEmpresa[-3],  #ruc
            "1",                        #ambiente
            ptoEmision,                 #ptoEmision
            sucursal,                   #sucursal
            secuencial,                 #secuencial
            "12345678"                  #random8Digitos
        )
        claveAcceso = mod11.getModule11()

        print(infoTributariaEmpresa)
        print(infoTributariaSecuenciales)
        print(infoTransportista)
        print(infoDestinatario)
        for deta in infoDetalles:
            print(deta)

        root = ET.Element("guiaRemision", version="1.1.0", id="comprobante")
        infotributaria = ET.SubElement(root, "infoTributaria")
        ET.SubElement(infotributaria, "ambiente").text = "1" # 1 -> PRUEBAS
        ET.SubElement(infotributaria, "tipoEmision").text = "1"
        ET.SubElement(infotributaria, "nombreComercial").text = infoTributariaEmpresa[1]
        ET.SubElement(infotributaria, "ruc").text = infoTributariaEmpresa[-3]
        ET.SubElement(infotributaria, "claveAcceso").text = claveAcceso
        ET.SubElement(infotributaria, "codDoc").text = "06"
        ET.SubElement(infotributaria, "estab").text = sucursal
        ET.SubElement(infotributaria, "ptoEmi").text = ptoEmision
        ET.SubElement(infotributaria, "secuencial").text = secuencial
        ET.SubElement(infotributaria, "dirMatriz").text = infoTributariaEmpresa[3]

        infoGuiaRemision = ET.SubElement(root, "infoGuiaRemision")
        ET.SubElement(infoGuiaRemision, "dirEstablecimiento").text = infoTributariaEmpresa[3]
        ET.SubElement(infoGuiaRemision, "dirPartida").text = infoTributariaEmpresa[3]
        ET.SubElement(infoGuiaRemision, "razonSocialTransportista").text = infoTransportista[4]
        ET.SubElement(infoGuiaRemision, "tipoIdentificacionTransportista").text = "04"
        ET.SubElement(infoGuiaRemision, "rucTransportista").text = infoTransportista[2]
        ET.SubElement(infoGuiaRemision, "obligadoContabilidad").text = "NO"
        ET.SubElement(infoGuiaRemision, "fechaIniTransporte").text = infoTributariaSecuenciales[7]
        ET.SubElement(infoGuiaRemision, "fechaFinTransporte").text =  infoTributariaSecuenciales[7]
        ET.SubElement(infoGuiaRemision, "placa").text = infoTransportista[-2].strip()

        destinatarios = ET.SubElement(root, "destinatarios")

        destinatario = ET.SubElement(destinatarios, "destinatario")
        ET.SubElement(destinatario, "identificacionDestinatario").text = infoDestinatario[3]
        ET.SubElement(destinatario, "razonSocialDestinatario").text = infoDestinatario[4]
        ET.SubElement(destinatario, "dirDestinatario").text = infoDestinatario[5]
        ET.SubElement(destinatario, "motivoTraslado").text = "MOVILIZACION DE MERCADERIA"

        detalles = ET.SubElement(destinatario, "detalles")
        for infoDetalle in infoDetalles:
            detalle = ET.SubElement(detalles, "detalle")
            ET.SubElement(detalle, "codigoInterno").text = str(infoDetalle[0])
            ET.SubElement(detalle, "codigoAdicional").text = str(infoDetalle[0])
            ET.SubElement(detalle, "descripcion").text = str(infoDetalle[5])
            ET.SubElement(detalle, "cantidad").text = str(infoDetalle[-3])

        infoadicional = ET.SubElement(root, "infoAdicional")
        ET.SubElement(infoadicional, "campoAdicional", nombre="Agente de Retencion").text = "No.Resolucion:123"
        arbol = ET.ElementTree(root)
        fileName = "files\prueba3.xml"
        arbol.write(fileName, encoding="UTF-8", xml_declaration=True)
        return fileName
