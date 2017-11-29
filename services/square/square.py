import urllib2, urllib
from bs4 import BeautifulSoup

###################################
##    Square Events Function     ##
###################################

def getEventData(input):
    url = 'http://www.harvardsquare.com/events/'
    if 'today' in input:
        url += 'today'
    elif 'week' in input:
        url += 'week'
    else:
        return "Please follow the format provided."

    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    events = soup.find(id='block-system-main').find(class_='view-content')
    events = events.text.encode('utf-8')

    return events

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the events for today or this week, use the format \'square today\' or \'square week\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getEventData(input)
