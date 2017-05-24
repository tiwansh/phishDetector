import requests, re
from tld import get_tld
from bs4 import BeautifulSoup
 

def crawlMatch(searchQuery, originalUrl):
    print "------Inside crawler-----"
    print "Search Query : " + str(searchQuery)
    dummy = 0
    urlFoundList = []
    try:
        tld_originalUrl = get_tld(originalUrl)
    except:
        return False
    tld_originalUrl = str(tld_originalUrl)
    #print "TLD in crawler is : " 
    #print type(tld_originalUrl)
    url = 'http://www.google.com/search' 
    payload = { 'q' : searchQuery, 'start' : '0' }
    my_headers = { 'User-agent' : 'Mozilla/11.0' }
    r = requests.get( url, params = payload, headers = my_headers )
    print r.text
    soup = BeautifulSoup( r.text, 'html.parser' )
    h3tags = soup.find_all( 'h3', class_='r' )
    #print h3tags
    print "Here"
    for h3 in h3tags:
        print "use"
        try:
            urlFound = re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1)
            print str(urlFound) + "isis"
            urlFoundList.append(str(urlFound))
        except:
            continue
    #print "Here I print : "
    #print urlFoundList
    for urls in urlFoundList:
        try:
            tld_urlFound = get_tld(urls)
            tld_urlFound = str(tld_urlFound)
            #print "Found ka type : "
            #print type(tld_urlFound)
            #print type(tld_urlFound) + " " + type(tld_originalUrl)
            if tld_urlFound == tld_originalUrl:
                print "--------Crawler match--------"
                return True
        except:
            continue
    print "--------Crawler no match------"
    return False