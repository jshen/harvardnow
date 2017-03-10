import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Weather Function     ##
#############################

def getMovieData(input):
    url = 'http://www.google.com/search?q=movies'
    url += '+'+input
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')
    
    try:
        card = soup.find_all(class_ = 'fl _yxj')
        body = ""
        for i in card:
            body += i.contents[0] + "\n"
    except Exception, e:
        print str(e)
        return "Could not find movies data. Are you sure you gave a proper zipcode?"

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the movies for a particular zipcode, use the format \'movies zipcode\'.'
    return s

## return proper format to use for getting movies
special = makeSpecial()

def eval(input):
    return getMovieData(input)
