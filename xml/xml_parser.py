import xml.etree.ElementTree as ElementTree

tree = ElementTree.parse('country.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
