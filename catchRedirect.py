import urllib2

#url = raw_input("Enter URL : ")

def get_redirect_url(url):
	try:
		opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
		request = opener.open(url)
		lol = request.url
		print lol
		return request.url
		'''a = requests.get(url)
		print r.url
		return r.url'''
	except:
		return "@"