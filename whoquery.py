import whois

url = raw_input("Enter url : ")
w = whois.whois(url)
#print (w.expiration_date)

#print (w.text)
print (w)
print w.updated_data
print w.state

#9453011714