import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Stock Function     ##
#############################

def getStockData(input):
    url = 'https://finance.google.com/finance?q='
    url += input
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        card = soup.find("div", {"id":"price-panel"}).find("span").find("span").string

        card = '$' + card

        return card

     except Exception, e:
         print str(e)
         return "Could not find stock data. Are you sure you gave a proper stock symbol?"

    #return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the stock, type in the stock symbol.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getStockData(input)
