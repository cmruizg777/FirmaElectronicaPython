
from helpers.xades.xades import Xades
from helpers.xmlGenerator import xmlGenerator

#p12File = 'cs.p12'
#password = '1091725041001'

xmlObject = xmlGenerator()
xmlDocument = xmlObject.generateRemissionGuideXml()
#xmlSignedDocument = 'files/firmado.xml'

#xades = Xades()
#xades.sign(xmlDocument, xmlSignedDocument, p12File, password)
