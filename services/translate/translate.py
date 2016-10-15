import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Translate Function     ##
#############################

def getTranslateData(input):
    url = 'http://www.google.com/search?q='
    url += '+'.join(input)
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')
    try:
        card = soup.find(id='ires')
        something = card.find_all(attrs={'class': 'ts'})[0]
        body = something.find_all(attrs={'class' : 'r'})[0].find_all(attrs={'class' : 'nobr'})[1].text
    except Exception, e:
        print str(e)
        return "Could not find translation. Are you sure you used the correct syntax? (translate <string/word> to <language>)"
    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To translate a sentence/word, use the format \'translate <string/word> to <language>\'.'
    return s

special = makeSpecial()

def eval(input):
    return getTranslateData(input)
