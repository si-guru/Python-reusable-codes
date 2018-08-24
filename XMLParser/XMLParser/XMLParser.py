from xml.etree import ElementTree

def xmlToString(parser_object):
    
    file_path = parser_object.file_path
    with open(file_path, 'rb') as file_name:
        xmlString = (file_name.read().strip())
    return xmlString

def generateXmlObject(parser_object):
    parser_object.xmlObject = ElementTree.fromstring(xmlToString(parser_object = parser_object))
    return parser_object

def findElementsByTagName(parser_object, tag_name = None):
    tag_object = parser_object.xmlObject.findall('.//p')
    return tag_object