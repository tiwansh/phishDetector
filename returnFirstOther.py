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
from otherCrawl import crawlMatch

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
		print "Khula"
	except urllib2.HTTPError as err:
		if err.code == 404:
			print "404"
			return -1
		elif err.code == 403:
			print "403"
			return -1
		else:
			print err.code
			return -1
	except urllib2.URLError as err:
		print "Unable1"
		return -1
	except:
		print "Unable"
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
				if(crawlMatch(query, web_url) == True):
					flag_legitimate = True
				#if match Legitimate
				#else IP Match
				#apply IP Lookup
				'''if flag_legitimate == False:
					if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
						print "Match found !!"
						flag_legitimate = True
				#if IP Matches Legitimate
				
				#else hitString REMOVED'''
			else:
				query = domain_name
				#Crawl q = tld
				if(crawlMatch(query, web_url) == True):
					flag_legitimate = True
				#matches => Legitimate else IP Match
				'''query = domain_name
				if flag_legitimate == False:
					if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
						print "Match finally !"
						flag_legitimate = True
				'''

		else:
			#Crawl q = tld
			query = domain_name
			if(crawlMatch(query, web_url) == True):
				flag_legitimate = True
			#matches => Legitimate else IP Lookup
			'''if flag_legitimate == False:
				if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
					flag_legitimate = True
			'''


	if flag_blogSite:
		return 2
	else:
		if flag_legitimate:
			return 1
		else:
			return 0

	#print "Time taken : " + str(time.time() - start_time) 

