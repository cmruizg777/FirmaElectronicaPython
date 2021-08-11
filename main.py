from helpers.barCodeGenerator import barCodeGenerator
from helpers.xades.xades import Xades
from helpers.xmlGenerator import xmlGenerator
from helpers.pdfGenerator import pdfGenerator
from helpers.guideRemission import guideRemission
from helpers.webServiceSri import webServiceSri
import  pyodbc as pyodbc
print(pyodbc.dataSources())
exit(0)
p12File = 'cs.p12'
password = '1091725041001'

guide = guideRemission()
data = guide.getgGuideRemissionData()
print(data)
xmlObject = xmlGenerator()
xmlDocument, accessKey = xmlObject.generateRemissionGuideXml(data)
#exit(0)

#accessKey = '0308202106109172504100110010010000009321575110617'
#xsdSchema = 'helpers/docs/guiaRemision_v1.1.0.xsd'
#xmlSignedDocument = 'files/firmado.xml'
#xades = Xades()
#xades.sign(xmlDocument, xmlSignedDocument, p12File, password)

#resp = xmlObject.validate(xmlSignedDocument, xsdSchema)
#print('Is valid: ', resp)
#in_file = open(xmlSignedDocument, 'r') # opening for [r]eading as [b]inary
#dataFile = in_file.read()
#sri = webServiceSri()
#success, errors = sri.send_receipt(dataFile)
#print(success, errors)

#if(success):
#    auth, messages = sri.request_authorization(accessKey)
#    print(auth)
#    print(messages)

barcode = barCodeGenerator()
barcode.generate('12345')
#barcode.generate(accessKey)

logo = 'files/img/logo.jpg'
#pdf = pdfGenerator()
#pdf.generateRemissionGuidePdf(data=data, logo_file=logo)



