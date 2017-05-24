import urllib2
import obo
from bs4 import BeautifulSoup
import re

'''for s in sorteddict: 
	mys = (str(s[1:]))
	mys2 = mys.strip("(,)")
	mys3 = mys2[1:]
	#print mys3.strip("''")
'''	

retStr=''

def hitString(limit, url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,"lxml")
	
	# kill all script and style elements
	for script in soup(["script", "style"]):
	    script.extract()    # rip it out
	
	# get text
	text = soup.get_text()
	text = text.lower()
	
	'''# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)'''
	
	
	#text = text.lower()
	fullwordlist = obo.stripNonAlphaNum(text)
	wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
	dictionary = obo.wordListToFreqDict(wordlist)
	sorteddict = obo.sortFreqDict(dictionary)	
	count = 0
	global retStr
	for s in sorteddict: 
		mys = (str(s[1:]))
		mys2 = mys.strip("(,)")
		mys3 = mys2[1:]
		mys4 = str(mys3.strip("''"))
		mys4 = str(mys4)
		if re.match("^-?[0-9]+$", mys4):
			continue
		count += 1
		#print mys4
		retStr += str(mys4) + ' '
 		if count == limit:
			break
	return retStr;

#print(text)
