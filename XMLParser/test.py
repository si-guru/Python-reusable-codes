from XMLParser import XMLParser as parser
import XMLParser
# import XMLParser

dummy_object = XMLParser.XMLParserObject('D:\Guru\Project\Project Tasks\VBAMacro\ClearEmptyPages\Macro Enabled Word Document - Copy\word\document.xml')
string_object = parser.xmlToString(parser_object = dummy_object)
# print(string_object)
parser.generateXmlObject(parser_object = dummy_object)
tag_elements = parser.findElementsByTagName(parser_object = dummy_object, tag_name='w')
for element in tag_elements:
    print(element) 