import urllib2
import requests

url = raw_input("Enter Url : ")

r = requests.head(url, allow_redirects = True)

print r.status_code
print r.url