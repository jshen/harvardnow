import urllib.request, urllib, urllib.error
import re
from bs4 import BeautifulSoup

#############################
##    News Function     ##
#############################

def getNewsData(input):
    url = 'http://www.google.com/search?q='
    url += '+'.join(input) + '+news'
    hdr = {'User-Agent': 'Mozilla 5.0'}
    req = urllib.request.Request(url,headers=hdr)

    website = urllib.request.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    headline1 = soup.find_all('div', style="margin-top:5px")
    headline2 = soup.find_all('div', style="margin-top:4px")

    headlines = headline1 + headline2
    results = []
    for headline in headlines:
        text = str(headline).split("</a>")
        results.append(headline.text)
    string = "".join(results)
    print (string)

getNewsData()

    except Exception, e:
        print str(e)
        return "Could not find news data. Are you sure you gave a proper city name?"

    return "".join(results)

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the news for a particular city, use the format \'news city\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getNewsData(input)
