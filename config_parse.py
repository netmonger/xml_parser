#!/usr/bin/env python

from lxml import etree

tree = etree.parse('config.xml')
root = tree.getroot()

for child in root:
	print child.tag, child.attrib



# iterate through file looking for specific elements and their text
for element in root.iter("ip"):
	print element.text


for element in root.xpath('//ip'):
	print element.text


for x in tree.iter('ip'):
	print x.text
	print(tree.getpath(x))


224.0.28.1
/configuration/channel[1]/connections/connection[2]/ip
224.0.28.128
/configuration/channel[1]/connections/connection[3]/ip
