import urllib2
import obo
from bs4 import BeautifulSoup



url = raw_input("Enter : ")
#url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
response = urllib2.urlopen(url)
html = response.read()
#soup = BeautifulSoup(html)

# kill all script and style elements
#for script in soup(["script", "style"]):
#    script.extract()    # rip it out

# get text
text = obo.stripTags(html).lower()

'''# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
'''

text = text.lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))


print(text)
