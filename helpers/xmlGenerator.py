import xml.etree.cElementTree as ET
import db.Connection as db
conn =  db.Connection();
class xmlGenerator():
    def __init__(self):
        self.cursor = db.Connection().getCursor()

    def getXmlData(self):
        result = self.cursor.execute("EXEC sp_xml_guiaRemision 192,'SAROCIBE'")
        tables = self.cursor.fetchall()
        print(tables)

root = ET.Element("guiaRemision",version="1.1.0",id="comprobante")
infotributaria = ET.SubElement(root,"infoTributaria")
ET.SubElement(infotributaria, "ambiente").text = "1"
ET.SubElement(infotributaria, "tipoEmision").text = "1"
ET.SubElement(infotributaria, "nombreComercial").text = "1"
ET.SubElement(infotributaria, "ruc").text = "1"
ET.SubElement(infotributaria, "claveAcceso").text = "1"
ET.SubElement(infotributaria, "codDoc").text = "1"
ET.SubElement(infotributaria, "estab").text = "1"
ET.SubElement(infotributaria, "ptoEmi").text = "1"
ET.SubElement(infotributaria, "secuencial").text = "1"
ET.SubElement(infotributaria, "dirMatriz").text = "1"

infoGuiaRemision = ET.SubElement(root,"infoGuiaRemision")
                                        
ET.SubElement(infoGuiaRemision, "dirEstablecimiento").text = "2"
ET.SubElement(infoGuiaRemision, "dirPartida").text = "2"
ET.SubElement(infoGuiaRemision, "razonSocialTransportista").text = "2"
ET.SubElement(infoGuiaRemision, "tipoIdentificacionTransportista").text = "2"
ET.SubElement(infoGuiaRemision, "rucTransportista").text = "2"
ET.SubElement(infoGuiaRemision, "obligadoContabilidad").text = "2"
ET.SubElement(infoGuiaRemision, "fechaIniTransporte").text = "2"
ET.SubElement(infoGuiaRemision, "fechaFinTransporte").text = "2"
ET.SubElement(infoGuiaRemision, "placa").text = "2"

destinatarios = ET.SubElement(root,"destinatarios")
destinatario = ET.SubElement(destinatarios,"destinatario")
ET.SubElement(destinatario, "identificacionDestinatario").text = "3"
ET.SubElement(destinatario, "razonSocialDestinatario").text = "3"
ET.SubElement(destinatario, "dirDestinatario").text = "3"
ET.SubElement(destinatario, "motivoTraslado").text = "3"
detalles = ET.SubElement(destinatario,"detalles")
detalle = ET.SubElement(detalles,"detalle")
ET.SubElement(detalle, "codigoInterno").text = "3"
ET.SubElement(detalle, "codigoAdicional").text = "3"
ET.SubElement(detalle, "descripcion").text = "3"
ET.SubElement(detalle, "cantidad").text = "3"
infoadicional = ET.SubElement(root,"infoAdicional")
ET.SubElement(infoadicional, "campoAdicional", nombre="Agente de Retencion").text = "No.Resolucion:"


arbol = ET.ElementTree(root)



arbol.write("C:\Guia Electronica\GuiaElectronica Procesados\prueba.xml", encoding = "UTF-8", xml_declaration = True)