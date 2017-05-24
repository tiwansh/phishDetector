#Function returning whether a website hits IP Matching or not
#Generates the list of most frequent links in the source

import re
import requests
from tld import get_tld
import socket




def ipMatches(url, limit):
	dictionary = {}
	dictionarylist = []

	dictionary.clear()
	del dictionarylist[:]
	print "Inside Second Module"
	flagLegitimate = False
	try:
		urlIP = socket.gethostbyname(get_tld(url))
	except:
		print "Unable host urlIP"
		return False
	counter = 0
	r = requests.get(url)

	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.content)

	for link in urls:
		#for arbitrary links with only words ?
		if "." not in link:
			continue
		pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
		if pattern.match(link):
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

	for urls in dictionarylist:
		if(counter == limit):
			break
		else:
			counter = counter + 1
		try:
			urlsIP = socket.gethostbyname(urls)
			print urls + " " + socket.gethostbyname(urls)
			if urlIP == urlsIP:
				#print "---------------IP's Matched-------------"
				flagLegitimate = True
				break
		except:
			print urls + " " + "Exception !"


	

	if flagLegitimate == True:
		print "----------- Domain Name Match found !!-----------"
		return 1
	else:
		print "!!! NO MATCH ~~~"
		return 0


#Positive for:
#https://www.facebook.com/
#http://timesofindia.indiatimes.com/
#https://www.office.com/
#https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1486413370&rver=6.4.6456.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fmail.live.com%2Fdefault.aspx&lc=1033&id=64855&mkt=en-us&cbcxt=mai


#http://engidex.info/
#http://www.stylogems.com/wp-admin/id/manage/customer/check/4e201b8bdc660d9a377d7f651dcbacf4/index/web/8243ae21633a8035b637d0a74ee0ea4a/login.php
#http://sich-er-heit.website/index.php?sessionid&signin&country.x=DE&cache=8AFLgs5OU3MYrpC9BEbe&locale.x=de_D
#http://aerokits.net/cart/bbggi/index.php


#Negative for:
#http://logistik.gr/cb/1/login.htm - Website doesnt allow to open the source