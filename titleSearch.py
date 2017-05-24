import urllib2
import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
import lxml.html
from mechanize import Browser

#url = raw_input("Enter url : ")

def returnTitle(url):
	title = ""
	a = 0
	try:
		t = lxml.html.parse(url)
		title = t.find(".//title").text
	except:
		a = 1


	try:
		response = urllib2.urlopen(url)
		soup = BeautifulSoup.BeautifulSoup(response)
		title = soup.html.head.title.string
		#print (title)
	except:
		a = 2

	try:
		soup1 = BeautifulSoup(urllib2.urlopen(url))
		title = soup1.title.string
	except:
		a = 3

	try:
		br = Browser()
		br.open(url)
		title = br.title()
	except:
		a = 4

	try:
		resp = urlopen(url)
		p = parse(page)
		title = p.getroot()
	except:
		a = 5

	#print title
	return title