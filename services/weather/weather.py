import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Weather Function     ##
#############################

def getWeatherData(input):
    url = 'http://www.google.com/search?q='
    url += '+'.join(input)
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    card = soup.find(id='ires').find_all(class_='g')[0]

    label = card.h3.text

    overview = card.img.attrs['title']
    tempInFarenheit = card.find_all(class_='wob_t')[0].text.encode('unicode-escape').replace(r'\xb0','')
    humidity = card.find_all(text=re.compile('Humidity'))[0]
    wind = card.find_all(text=re.compile('Wind'))[0].parent.text

    body = label + '\n'
    body += 'Temp: ' + tempInFarenheit + '\n'
    body += humidity + '\n'
    body += wind

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the weather for a particular city, use the format \'weather city\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getWeatherData(input)
