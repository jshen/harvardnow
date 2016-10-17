import urllib2, urllib
from bs4 import BeautifulSoup
from random import randint

#############################
##    Events Function      ##
#############################

def getEventsData(input):

    url = 'http://www.thebostoncalendar.com/'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:

        events = soup.find_all("li", {"class": "event"})
        event = events[randint(0, len(events) - 1)]
        body = "Why don't you try out " + event.find("div", {"class": "info"}).h3.a.contents + " (" +  event.find("a", {"itemprop": "url"})["href"]

    except Exception, e:
        print str(e)
        return "Could not find any events for you."

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To return a random Boston event, use the format \'event\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getEventsData(input)
