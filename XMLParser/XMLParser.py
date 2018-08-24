
from xml.etree import ElementTree

def xmlToString(parser_object):
    try:
        file_path = parser_object.file_path
        with open(file_path, 'rb') as file_name:
            xmlString = (file_name.read().strip())
    except:
        xmlString = None
    return xmlString

def generateXmlObject(parser_object):
    try:
        xmlString = xmlToString(parser_object = parser_object)
        parser_object.xmlObject = ElementTree.fromstring(xmlString)
    except:
        parser_object = None
    return parser_object

def findElementsByTagName(parser_object, tag_name = None):
    try:
        tag_object = parser_object.xmlObject.findall('.//'+tag_name)
    except:
        tag_object = None
    return tag_object

def innerHTML(element):
    return element.text