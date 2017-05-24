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
import requests

def isLegit(web_url):
	start_time = time.time()
	ipMatchLimit = 3

	title= " "
	#web_url = raw_input("Enter URL : ")

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

	'''
	Testing for status code
	'''

	try:
		page = urllib2.urlopen(web_url)
	except urllib2.HTTPError as err:
		if err.code == 404:
			return -1
		elif err.code == 403:
			return -1
		else:
			print err.code
			return -1
	except urllib2.URLError as err:
		return -1
	except:
		return -1
	

	'''req = requests.get(web_url)
	print "Status code : " + str(req.status_code)
	'''
	if blog.isBlogSite(web_url):
		flag_blogSite = True

	title = titleSearch.returnTitle(web_url)
	if(title is not ""):
		print "Title is : " + str(title)
		flag_titleFound = True
	else:
		print ("Title not found!")

	if(title is "Access Denied"):
		return -1

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
		return 2
	else:
		if flag_legitimate:
			return 1
		else:
			return 0

	#print "Time taken : " + str(time.time() - start_time) 

