import urllib2, urllib
import re
from bs4 import BeautifulSoup

#####################################
##    Word of the Day Function     ##
#####################################

def getWordData():
    url = '2700chess.com'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        playerHTML = soup.find_all("span", {"class" : "hidden searched"})[0]
        player = playerHTML.get_text()
        ratingHTML = soup.find_all("td", {"class" : "live_standard_rating"})[0].strong
        rating = ratingHTML.get_text()

        body = player + ": " + rating
        
    except Exception, e:
        print str(e)
        return "Could not find top chess player info."

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'This will get the current highest rated chess player.'
    return s

## return proper format
special = makeSpecial()

def eval():
    return getWordData()