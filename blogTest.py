import blog

url = raw_input("Enter url : ")

if blog.isBlogSite(url):
	print "Blog!"
else:
	print "Not blog!"