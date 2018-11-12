import urllib2, urllib
import re
from bs4 import BeautifulSoup

#####################################
##       Next Holiday Function     ##
#####################################

def getNextHoliday():
    url = 'http://www.holidayscalendar.com'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        table = soup.findAll('tbody')
        holiday = table[1].td.a.get_text()

    except Exception, e:
        print str(e)
        return "Could not find next holiday data."

    return holiday

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'This will get the next holiday.'
    return s

## return proper format
special = makeSpecial()

def eval():
    return getNextHoliday()
