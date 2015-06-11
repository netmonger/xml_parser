#!/usr/bin/env python

from lxml import etree

tree = etree.parse('config.xml')

ip = raw_input('Enter IP: ')
found_ip = False


# Iterate through XML tree looking for IP.
for elem in tree.iter('ip'):
	if elem.text != ip:
		continue
	else:
		found_ip=True
		#print("Found IP")
		#print((elem.iterancestors()).tag)
		parent = elem.getparent()
		port = parent.find('port').text
		host_ip = parent.find('host-ip').text
		feed = parent.find('feed').text
		print "IP: %s" % ip
		print "Port: %s" % port
		print "Source IP: %s" % host_ip
		print "Feed side: %s" % feed
		break

# Inform user if IP was not found.
if found_ip is False:
	print("IP not found")


