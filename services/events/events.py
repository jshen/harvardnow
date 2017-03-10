# HCS Bootcamp #2 - HarvardNow
# Philippe Noel, Daniel Chen, Jeff Balkanski

import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##     Events Function     ##
#############################

def getEventsData():
    # get url and initiate parsing
    url = 'http://www.harvard.edu/events'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url, headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        # get all the cards on the slideshow of the website
        cards = soup.find_all(class_ ='card-callout-media__text')
        body = 'Upcoming events:\n\n'

        # get all the cards and their respective information
        for card in cards:
            title = card.find(class_ = 'card--event__link').string.encode("utf-8")
            date = card.find_all('p')[0].string.encode("utf-8")
            location = card.find_all('p')[1].string.encode("utf-8")

            # replace the extra breaks by spaces for readability
            title = title.replace('\n', '')
            date = date.replace('\n', '')
            location = location.replace('\n', '')

            # add everything to the body
            body += title + '\n'
            body += date + '\n'
            body += location + '\n\n'

    # handles exception for no events found
    except Exception, e:
        print str(e)
        return "Could not find events data."

    # render success
    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get events scheduled at Harvard, use the format \'events\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getEventsData()
