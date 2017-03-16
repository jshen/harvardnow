import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Television Function     ##
#############################

def getTelevisionData(input):
    url = 'http://www.google.com/search?q='
    url += '+'.join(input)
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        card = soup.find(id='uid_0').find_all(class_='_Sxk')[0]

        date = 'Date: ' + card.find_all(class_='_Xkm')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='_Xkm')) > 0 else ''
        channel = 'Channel: ' + card.find_all(class_='_zlm')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='_zlm')) > 0 else ''
        
        episode_information = card.find_all(class_='_Alm _Klm')

        season = 'Season: ' + episode_information[0] if len(card.find_all(class_='_Alm _Klm')) > 0 else ''
        episode = 'Episode: ' + episode_information[1] if len(card.find_all(class_='_Alm _Klm')) > 0 else ''

        body = date
        body += channel
        body += season
        body += episode

    except Exception, e:
        print str(e)
        return "Could not find the next broadcast time for this show. Are you sure this show is still airing?"

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the next broadcast time for a television program, use the format \'program name tv show\'.'
    return s

## return proper format to use for getting television
special = makeSpecial()

def eval(input):
    return getTelevisionData(input)
