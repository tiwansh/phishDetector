import srcIPMatch
import urllib2
import BeautifulSoup
import re
from google import search
from tld import get_tld
#import lolmax
from langdetect import detect
import sourceUrlsList
#import catchRedirect
import titleSearch


ipMatchLimit = 3

title=''
web_url = raw_input("Enter URL : ")

flag_titleFound = False
flag_legitimate = False

#urlsList = []

'''
#checking for redirection
if catchRedirect.get_redirect_url(web_url) != "@":
	web_url = catchRedirect.get_redirect_url(web_url)
	print "Redirection !! New URL : " + web_url

#print web_url
'''

domain_name = get_tld(web_url)
print ("Domain name is : ") + domain_name

query = ''


if(titleSearch.returnTitle(web_url) != ''):
	title = titleSearch.returnTitle(web_url)
	print "Title is : " + (title)
	flag_titleFound = True
else:
	print ("Title not found!")


if flag_titleFound:
	try:
		language = detect(title)
	except:
		language = ''
	
	if(str(language) == "en"):
		query = domain_name + ' ' + title
		#Crawl tld + title
		for url in search(query, stop=7):
			print (url)
			#print type(str(url))
			domain_found = get_tld(str(url))
			if (domain_name == domain_found):
				print ("========================================Match found in crawling title + tld =====================================")
				flag_legitimate = True
				break
		#if match Legitimate
		#else IP Match
		#apply IP Lookup
		if flag_legitimate == False:
			if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
				print "Match found !!"
				flag_legitimate = True
		#if IP Matches Legitimate
		'''if flag_legitimate == False:
			newQuery = lolmax.hitString(7, web_url)
			for newUrl in search(newQuery, stop = 7):
				print (newUrl)
				new_domain_found = get_tld(str(newUrl))
				if(domain_name == new_domain_found):
					print "Match found in lolol"
					flag_legitimate = True
		#else hitString'''
	else:
		query = domain_name
		#Crawl q = tld
		for url in search(query, stop=7):
			print (url)
			#print type(str(url))
			domain_found = get_tld(str(url))
			if (domain_name == domain_found):
				print ("========================================Match found in crawling domain / No langugage =====================================")
				flag_legitimate = True
				break
		#matches => Legitimate else IP Match
		query = domain_name
		if flag_legitimate == False:
			if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
				print "Match finally !"
				flag_legitimate = True
else:
	#Crawl q = tld
	query = domain_name
	for url in search(query, stop=7):
		print (url)
		#print type(str(url))
		domain_found = get_tld(str(url))
		if (domain_name == domain_found):
			print ("========================================Match found in crawling title + tld =====================================")
			flag_legitimate = True
			break
	#matches => Legitimate else IP Lookup
	if flag_legitimate == False:
		if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
			flag_legitimate = True





if flag_legitimate:
	print "Legitimate !!"
else:
	print "Phishing !!"

