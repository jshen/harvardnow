import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Weather Function     ##
#############################

def getMBTAData(cmd):
    for pg in cmd['pg']:
        url = 'http://www.mbtainfo.com/'
        url += pg
        hdr = {'User-Agent': 'Chrome'}
        req = urllib2.Request(url,headers=hdr)
        website = urllib2.urlopen(req)
        soup = BeautifulSoup(website.read(), 'html.parser')

        try:
            #print(soup)
            times = soup.find("a", class_="minor").find_next_siblings()
            del times[len(times) - 1]

            body = []

            for element in times:
                for string in element.strings:
                    body.append(string.replace(u'\u2014', '-'))

            body = "\n".join(filter(lambda x: len(x) > 1, body))

            for i in xrange(1, len(body) - 1):
                print i
                if not unicode(body[i])[0].isdigit():
                    body[i - 1] = u'\n'
                    body[i + 1]

            for line in body:
                print line

        except Exception, e:
            print str(e)
            return "Could not find T data. Are you sure you gave a proper line and station name?"

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the shuttle for a particular line, use the format \'MBTA line station\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(cmd):
    return getMBTAData(cmd)

if __name__ == "__main__":
    getMBTAData({"pg": ["red/RHAR"]})
