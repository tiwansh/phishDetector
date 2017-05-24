import urllib2
import urllib
import simplejson

testThis = raw_input("Enter the URL to test: ")

PhishTankURL = "http://checkurl.phishtank.com/checkurl/"
PhishTParm = {"url": testThis,
                  "format": "json",
                  "app_key": " ** Enter PhishTank App Key ** "}
data_PT = urllib.urlencode(PhishTParm)
request_PT = urllib2.Request(PhishTankURL, data_PT)
response_PT = urllib2.urlopen(request_PT)
json_PT = response_PT.read()
response_PT_dict = simplejson.loads(json_PT)

responseThingMeta = response_PT_dict.get("meta")
PhishTankStatus = responseThingMeta.get("status")

if PhishTankStatus == "error":
    PhishTankResult = response_PT_dict.get("errortext")
else:
    PhishTankResult = response_PT_dict.get("results")
    PhishTankResult = PhishTankResult.get("in_database")

print PhishTankResult


    