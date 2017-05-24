import urllib2
import BeautifulSoup
import re
from google import search
from tld import get_tld
from Tkinter import *

web_url = raw_input("Enter : ")
flag_no_title = True
flag_found_in_list = False


#Tries to find the title
try:
	response = urllib2.urlopen(web_url)
	soup = BeautifulSoup(response)
	title = soup.html.head.title.string
	print (title)
except:
	#print ("Title not found!")
	flag_no_title = False

#P.S. : well defined websites have properly formatted HTML codes and so is the title.
#hence the title must easy to extract and must be present 
#If title extraction fails then this confirms that some tampering 
#has been done with the code 

#extract url's main keyword
domain_name = get_tld(web_url)
#print (domain_name)

# remove .com/.org/.co.in from domain
'''if domain_name.endswith('.com'):
	domain_name = domain_name[:-4]
if domain_name.endswith('.co.in'):
	domain_name = domain_name[:-6]
if domain_name.endswith('.org'):
	domain_name = domain_name[:-4]
if domain_name.endswith('.in'):
	domain_name = domain_name[:-3]
'''

print ("Domain name is : ")
print domain_name


if flag_no_title:
	title = domain_name + ' ' + title
else:
	title = domain_name
	
print (title)

# Performs a search on google based on title + domain name
print ("URLs are : ")
for url in search(title, stop=20):
	print (url)
	if (url == web_url):
		print ("========================================Match found=====================================")
		flag_found_in_list = True
	#Top URL's fetched on google search of title + web_url
if flag_found_in_list:
	print("Not a phishing site ! You may proceed !")
else :
	print("No match found. Phishing Site ! Do not proceed !")
