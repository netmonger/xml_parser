#!/usr/bin/env python

from lxml import etree
import sys
import urllib
import pprint

# Downloading various config.xml files from CME FTP site ftp://www.cmegroup.com/

# Check if currently stored file is from yesterday or older.  If it is download a new copy.
# <need code here>

# Initialize XML file dictionary for iterating through when searching for IP.
xml_file_list = {}

# Download SBEFix NRCert
# Temporarily disabled
# url = 'ftp://ftp.cmegroup.com/SBEFix/NRCert/Configuration/config.xml'
# urllib.urlretrieve(url, 'sbefix_nrcert.xml')
xml_file_list['SBEFix NRCert'] = 'sbefix_nrcert.xml'

# Download SBEFix NRAutoCertPlus
# Temporarily disabled
# url = 'ftp://ftp.cmegroup.com/SBEFix/NRAutoCertPlus/Configuration/config.xml'
# urllib.urlretrieve(url, 'sbefix_nrautocertplus.xml')
xml_file_list['SBEFix NRAutoCertPlus'] = 'sbefix_nrautocertplus.xml'

# Get IP from user
# ip = raw_input('Enter multicast group IP: ')
ip = sys.argv[1]
found_ip = False


# Search all XML files for IP by iterating through list of XML files.  Once IP is found then enter parsing function.
for name,file in xml_file_list.iteritems():

	# Parsing XML file
	tree = etree.parse(file)
	
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
			print name
			print "-----------------------------"
			print "Channel label: %s" % channel_label
			print "Channel ID: %s" % channel_id
			print "Connection ID: %s" % connection_id
			print "Feed side: %s" % feed
			print "Source IP: %s" % host_ip
			print "IP: %s" % ip
			print "Port: %s" % port
			print "\n"
			break

# Inform user if IP was not found.
if found_ip is False:
	print("\nIP not found\n")

