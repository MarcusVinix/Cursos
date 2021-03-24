from xml.etree.ElementTree import ElementTree
tree = ElementTree(file="sanfonas.xml")
root = tree.getroot()
print(root.getchildren())
scandalli = root.find("Scandalli")
print(scandalli.tag)
print(scandalli.attrib)
root.remove(root.find("Todeschini"))
print(root.getchildren())
