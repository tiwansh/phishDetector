import srcIPMatch
import urllib2
import BeautifulSoup
import re
from google import search
from tld import get_tld
import lolmax
from langdetect import detect
import sourceUrlsList
import catchRedirect
import titleSearch
import blog
import time

start_time = time.time()

ipMatchLimit = 3

title= " "
web_url = raw_input("Enter URL : ")

flag_titleFound = False
flag_legitimate = False
flag_blogSite = False
urlsList = []
'''
redirectChecker = catchRedirect.get_redirect_url(web_url)
#checking for redirection
if redirectChecker != "@":
	web_url = redirectChecker
	print "Redirection !! New URL : " + web_url

#print web_url
'''

if blog.isBlogSite(web_url):
	flag_blogSite = True

title = titleSearch.returnTitle(web_url)
if(title is not ""):
	print "Title is : " + str(title)
	flag_titleFound = True
else:
	print ("Title not found!")

domain_name = get_tld(web_url)
print ("Domain name is : ") + domain_name

query = ''

if flag_blogSite == False:
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
				#print url
				try:
					domain_found = get_tld(str(url))
				except:
					continue
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
			
			#else hitString REMOVED
		else:
			query = domain_name
			#Crawl q = tld
			for url in search(query, stop=7):
				print (url)
				#print type(str(url))
				try:
					domain_found = get_tld(str(url))
				except:
					continue
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
			#print (url)
			#print type(str(url))
			try:
				domain_found = get_tld(str(url))
			except:
				continue
			if (domain_name == domain_found):
				print ("========================================Match found in crawling title + tld =====================================")
				flag_legitimate = True
				break
		#matches => Legitimate else IP Lookup
		if flag_legitimate == False:
			if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
				flag_legitimate = True



if flag_blogSite:
	print "Warning ! This is a blogging website and may be a phish!"
else:
	if flag_legitimate:
		print "Legitimate !!"
	else:
		print "Phishing !!"

print "Time taken : " + str(time.time() - start_time) 

