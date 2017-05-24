import request



url = 'http://www.google.com/search'
payload = {'q' : 'makman', 'start' : '0'}
my_headers = {'User-agent' : 'Mozilla/11.0'}
r = requests.get(url, params = payload, headers = my_headers)
print(r.text.encode('utf-8')) 