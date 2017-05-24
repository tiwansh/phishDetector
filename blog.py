from tld import get_tld

def isBlogSite(url):
	#print "Yaha"
	try:
		url_tld = get_tld(url)
	except:
		return False
	print "Top level domain is " + url_tld
	with open("finalList") as f:
		for line in f:
			#print type(line)
			#print (line.lower()) 
			#print (str(url_tld.lower()))
			line = line.strip()
			line = line.lower()
			url_tld = str(url_tld)
			url_tld = url_tld.lower()
			#print (line)
			#print (url_tld)
			if line == url_tld:
				print "Blogging match found !"
				return True
	return False