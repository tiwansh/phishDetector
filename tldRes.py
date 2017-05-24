import re
import socket
url = raw_input("")

pattern = re.compile("\/\/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/")
test = pattern.match(url)
if test:
	print "Match"
else:
	print "No"
