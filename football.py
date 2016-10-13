import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Football Function    ##
#############################

def getFootballSchedule(input):
    url = 'http://www.gocrimson.com/sports/fball/2016-17/schedule'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        card = soup.find(id='ires').find_all(class_='g')[0]

        label = card.h3.text + '\n' if card.h3 is not None else ''

        overview = card.img.attrs['title'] + '\n' if card.img is not None and card.img.has_attr('title') else ''
        date = card.find_all(class_='date')[0].parent.text if len(card.find_all(class_='date')) > 0 else ''
        team = card.find_all(class_='opponent')[0].parent.text if len(card.find_all(class_='opponent')) > 0 else ''
        

        body = label
        body += date
        body += team
        
    except Exception, e:
        print str(e)
        return "Could not find a game. Are you sure you gave the proper date?"

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the team that Harvard plays in a week, input \'Date of game\'.'
    return s

## return proper format to use for getting team
special = makeSpecial()

def eval(input):
    return getFootballSchedule(input)
