#!/usr/bin/env python

from lxml import etree
import pprint

tree = etree.parse('config.xml')

ip = raw_input('Enter IP: ')
found_ip = False


# Iterate through XML tree looking for IP.
for elem in tree.iter('ip'):
	if elem.text != ip:
		continue
	else:
		# IP was found
		found_ip=True

		# Get parents element of section where IP was found
		connection = elem.getparent()
		channel = (connection.getparent()).getparent()

		# Get text of all elements of a connection as well as channel information
		connection_id = connection.attrib["id"]
		port = connection.find('port').text
		host_ip = connection.find('host-ip').text
		feed = connection.find('feed').text
		channel_id = channel.attrib["id"]
		channel_label = channel.attrib["label"]

		# Print all elements of a connection including channel information
		print "\n"
		print "Connection ID: %s" % connection_id
		print "IP: %s" % ip
		print "Port: %s" % port
		print "Source IP: %s" % host_ip
		print "Feed side: %s" % feed
		print "Channel ID: %s" % channel_id
		print "Channel label: %s" % channel_label
		break

# Inform user if IP was not found.
if found_ip is False:
	print("IP not found")


