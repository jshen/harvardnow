import urllib2, urllib
import re
from bs4 import BeautifulSoup

#####################################
##    Crimson Headlines Function   ##
#####################################

def getHeadlines():
    url = 'https://www.thecrimson.com/'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')
    msg = "The 5 most read Crimson articles:\n"

    try:
        headlines = soup.find("div", {"id": "most-read-box"})
        for li in headlines.find_all('li'):
            link = li.find('a')
            msg += link.get_text()+ " " + "https://www.thecrimson.com" + link['href']+ " "
    
        
    except Exception, e:
        print str(e)
        return "Could not find headline data."

    return msg

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'This will get the top Crimson headlines.'
    return s

## return proper format
special = makeSpecial()

def eval():
    return getHeadlines()
