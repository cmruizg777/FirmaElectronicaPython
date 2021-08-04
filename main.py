
from helpers.xades.xades import Xades
from helpers.xmlGenerator import xmlGenerator
from helpers.pdfGenerator import pdfGenerator
from helpers.guideRemission import guideRemission

#p12File = 'cs.p12'
#password = '1091725041001'

guide = guideRemission()
data = guide.getgGuideRemissionData()

xmlObject = xmlGenerator()
xmlDocument = xmlObject.generateRemissionGuideXml(data)

#pdf = pdfGenerator()
#pdf.generateRemissionGuidePdf(guide)

#xmlSignedDocument = 'files/firmado.xml'

#xades = Xades()
#xades.sign(xmlDocument, xmlSignedDocument, p12File, password)
