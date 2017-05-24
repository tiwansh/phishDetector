import urllib2
import BeautifulSoup
import re
from tld import get_tld
from google import search

title=''
web_url = raw_input("Enter : ")
#print type(web_url)
flag_no_title = True
flag_found_in_list = False


#Tries to find the title
try:
	response = urllib2.urlopen(web_url)
	soup = BeautifulSoup(response)
	#title = soup.html.head.title.string
	#title = soup.html.head.title.string
	html_obj = soup.html
	head_obj = html_obj.head
	title_obj = head_obj.title
	title = title_obj.string
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
print ("Domain name is : ")
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
	
#print domain_name


if flag_no_title:
	query = domain_name + ' ' + title
else:
	query = domain_name

print (query)
# Performs a search on google based on title + domain name
print ("URLs are : ")
for url in search(query, stop=10):
	print (url)
	#print type(str(url))
	domain_found = get_tld(str(url))
	if (domain_name == domain_found):
		print ("========================================Match found=====================================")
		flag_found_in_list = True
	#Top URL's fetched on google search of title + web_url
	
	
if flag_found_in_list:
	print("Not a phishing site ! You may proceed !")
else :
	print("No match found. Phishing Site ! Do not proceed !")
