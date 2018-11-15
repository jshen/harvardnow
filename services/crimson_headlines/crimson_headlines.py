import urllib2, urllib
from bs4 import BeautifulSoup

#######################################
##    Crimson Headlines Function     ##
#######################################

def getCrimsonNews():
    initial = 'https://www.thecrimson.com/'
    website = urllib2.urlopen(initial)
    soup = BeautifulSoup(website.read(), 'html.parser')
    first_headline = soup.find(id='primary-first-top')

    result = article.a.text
    return result

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = "Latest Crimson Headline:\n"
    headline = getCrimsonNews()
    s += headline
    return s

## return headline
special = makeSpecial()

def eval():
    return getCrimsonNews()
