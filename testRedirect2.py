import urllib.request


res = urllib.request.urlopen(h"ttp://bit.ly/2l3WwuP")
finalurl = res.geturl()
print(finalurl)