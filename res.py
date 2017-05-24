import urllib2
import BeautifulSoup
import re
from google import search
from tld import get_tld
from Tkinter import *


def checkPhish():
	web_url = entryURL.get()
	print web_url
	flag_no_title = True
	flag_found_in_list = False
	
	#Tries to find the title
	try:
		response = urllib2.urlopen(web_url)
		soup = BeautifulSoup.BeautifulSoup(response)
		title = soup.html.head.title.string
		print (title)
	except:
		print ("Title not found!")
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
		domain_name = domain_name[:-3]'''
	
	print domain_name
	
	if flag_no_title:
		title = title + ' ' + domain_name
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
			v.set("Not a phishing site ! You may proceed !")
		else :
			v.set("No match found. Phishing Site ! Do not proceed !")
	
	
	else:
		v.set("Title not found ! Phishing site ! Do not proceed !")		
	
'''	return;


#creating root canvas
root = Tk()

#creating two sub-frames
leftFrame = Frame(root, bg = "red")
leftFrame.pack(side = LEFT) #pack the left frame to left
rightFrame = Frame(root)
rightFrame.pack(side = RIGHT) #pack the right frame to left

#create a label and pack it in left of leftframe
labelEnter = Label(leftFrame, text = "Enter Website : ", )
labelEnter.pack(side = LEFT)

#create an entry and pack it in right of leftframe
entryURL = Entry(leftFrame, bd = 5)
entryURL.pack(side = RIGHT)

#created a button to give value
button = Button(rightFrame, text = "Check",fg = "Green", bd = 4, activebackground = "Blue", activeforeground = "White", command = checkPhish, relief = RAISED)
button.pack()

#created a label to display phishing site or not !
v = StringVar()
labelDisplay = Label(root, textvariable = v)
labelDisplay.pack(side = BOTTOM)

root.mainloop()'''