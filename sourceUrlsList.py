#Generates the list of most frequent links in the source

import re
import requests
from tld import get_tld

dictionary = {}


def urlsList(url):
	r = requests.get(url)
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.content)

	for link in urls:
		#for arbitrary links with only words ?
		if "." not in link:
			continue
		#Testing whether the link is an IP ?
		#Trying in case of IP address hosted link example -- http://128.199.202.96/thehindu/public/img/article/theHinduCenter.png
		#print link
		try:
			newurl = get_tld(link)
			#print newurl
			if not newurl in dictionary:
				dictionary[newurl] = 1
			else:
				dictionary[newurl] += 1
		except:
			continue


	#Created a new sorted list from dictionary
	dictionarylist = sorted(dictionary, key=dictionary.get, reverse = True)

	return dictionaryList
		
#Positive for:
#https://www.facebook.com/
#http://timesofindia.indiatimes.com/
#http://engidex.info/
#http://www.stylogems.com/wp-admin/id/manage/customer/check/4e201b8bdc660d9a377d7f651dcbacf4/index/web/8243ae21633a8035b637d0a74ee0ea4a/login.php
#http://sich-er-heit.website/index.php?sessionid&signin&country.x=DE&cache=8AFLgs5OU3MYrpC9BEbe&locale.x=de_D



#Negative for:
#http://logistik.gr/cb/1/login.htm - Website doesnt allow to open the source