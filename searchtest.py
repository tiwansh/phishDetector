from google import search

query="9gag"
print ("URLs are : ")
for url in search(query, stop=10):
	print (url)
	#print type(str(url))
	#domain_found = get_tld(str(url))
	#if (domain_name == domain_found):
		#print ("========================================Match found=====================================")
		#flag_found_in_list = True
	#Top URL's fetched on google search of title + web_url
	