from Tkinter import *
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

def isLegit():
	web_url = entryURL.get()
	start_time = time.time()
	ipMatchLimit = 5

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
	start_time = time.time()
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
				if(crawlMatch(query, web_url) == True):
					flag_legitimate = True
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
				if(crawlMatch(query, web_url) == True):
					flag_legitimate = True
				#matches => Legitimate else IP Match
				query = domain_name
				if flag_legitimate == False:
					if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
						print "Match finally !"
						flag_legitimate = True


		else:
			#Crawl q = tld
			query = domain_name
			if(crawlMatch(query, web_url) == True):
				flag_legitimate = True
			#matches => Legitimate else IP Lookup
			if flag_legitimate == False:
				if srcIPMatch.ipMatches(web_url, ipMatchLimit) == 1:
					flag_legitimate = True


	diff = time.time() - start_time
	#Add following to each v.set() to display response time  
	'''+ str(diff)'''
	if flag_blogSite:
		v.set("Blogging Site !! Procees with caution ! " )
	else:
		if flag_legitimate:
			v.set("Legitimate Site !! You may proceed ! " )
		else:
			v.set("Phishing Site !! DO NOT PROCEED ! " )

	#print "Time taken : " + str(time.time() - start_time) 


def printme(url):
	print url
	print "lol"


root = Tk()
root.title("Phish Detector")
root.geometry('500x500')
root.configure(background = "#a1dbcd")


#creating three sub-frames
topFrame = Frame(root)
topFrame.pack()
leftFrame = Frame(root, pady = 20, bg = "#a1dbcd")
leftFrame.pack() #pack the left frame to left
rightFrame = Frame(root)
rightFrame.pack() #pack the right frame to left
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

#created a label to display creds
labelTop = Label(topFrame, font = ("Helvetica",24), text = "Check a phishing website !", bg= "#a1dbcd", pady = 50)
labelTop.pack()

#create a label and pack it in left of leftframe
labelEnter = Label(leftFrame, text = "Enter Website : ", padx = 10, bg  = "#a1dbcd")
labelEnter.pack(side = LEFT)

#create an entry and pack it in right of leftframe
entryURL = Entry(leftFrame, bd = 5)
entryURL.pack(side = RIGHT)

#created a button to give value
button = Button(rightFrame, text = "Check",fg = "Green", bd = 0, activebackground = "Blue", activeforeground = "White", command = isLegit, relief = FLAT)
button.pack()

v = StringVar()
labelDisplay = Label(bottomFrame, textvariable = v, pady = 30, bg  = "#a1dbcd")
labelDisplay.pack()

root.mainloop()