import urllib2, urllib
import re
from bs4 import BeautifulSoup

###############################
 #############################
  #  Coupon Function Fluff  #
 #############################
###############################

def getCoupons(input):
    # establishes the location at Harvard (Agassiz House I think)
    url = 'https://www.groupon.com/browse/boston?lat=42.3800977&lng=-71.11662860000001&locality=Cambridge&administrative_area=MA&neighborhood=Agassiz&address=Agassiz%2C+Cambridge%2C+MA&query='
    # inserts our input as a query
    url += ''.join(input)
    # adds the rest of the query
    url += ''.join('&locale=en_US')
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
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
        return "Could not find coupons. Are you sure you gave a proper type of food?"

    return body











###############################
#####Coupon Function Core######
###############################

def makeSpecial():
    s = 'To get the coupons for a particular city, use the format \'coupon city foodstyle\'.'
    return s

## return proper format to use for getting coupons
special = makeSpecial()

def eval(input):
    return getCoupons(input)

