import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Turkey Function     ##
#############################

def getTurkeyData(input):
    url = 'http://www.google.com/search?q=turkey'
    url += '&tbm=nws'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        card = soup.find(id='ires').find_all(class_='g')[0]

        label = card.h3.text + '\n' if card.h3 is not None else ''

        overview = card.img.attrs['title'] + '\n' if card.img is not None and card.img.has_attr('title') else ''
        source = 'Source: ' + card.find_all(class_='_tQb _IId')[0].text.encode('unicode-escape')
        timeago = 'Time ago: ' + card.find_all(class_='f nsa _uQb')[0].text.encode('unicode-escape')
        blurb = 'Time ago: ' + card.find_all(class_='st')[0].text.encode('unicode-escape')

        body = label
        body += overview
        body += source
        body += timeago
        body += blurb
    except Exception, e:
        print str(e)
        return "Could not find data about Turkey!"

    return body


def eval(input):
    return getTurkeyData(input)
