import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Election Function     ##
#############################

def getElectionData(input):
    url = 'http://www.google.com/search?q='
    url += '+'.join(input)
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)

    try:
        website = urllib2.urlopen(req)
        soup = BeautifulSoup(website.read(), 'html.parser')

        card = soup.find(id='ires').find_all(class_='g')[0]

        label = card.h3.text + '\n' if card.h3 is not None else ''

        overview = card.img.attrs['title'] + '\n' if card.img is not None and card.img.has_attr('title') else ''
        tempInFarenheit = 'Temp: ' + card.find_all(class_='wob_t')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='wob_t')) > 0 else ''
        humidity = card.find_all(text=re.compile('Humidity'))[0] + '\n' if len(card.find_all(text=re.compile('Humidity'))) > 0 else ''
        wind = card.find_all(text=re.compile('Wind'))[0].parent.text if len(card.find_all(text=re.compile('Wind'))) > 0 else ''

        body = label
        body += overview
        body += tempInFarenheit
        body += humidity
        body += wind
    except Exception, e:
        print str(e)
        return "Could not find weather data. Are you sure you gave a proper city name?"

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the weather for a particular city, use the format \'weather city\'.' # put 
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getWeatherData(input)
