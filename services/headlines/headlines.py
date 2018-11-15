import urllib2, urllib
from bs4 import BeautifulSoup

def headlines(url_string):
    # String containing all headlines from main page
    headlines = ''

    # Parse all headlines
    website = urllib2.urlopen(url_string)
    soup = BeautifulSoup(website.read(), 'html.parser')
    headline_tags = soup.find_all('a', href=True)

    # Add all headlines
    for tag in headline_tags:
        headlines += tag.get_text() + '\n'

    return headlines

def makeSpecial():
    s = 'To get the headlines from a particular publication, use the format \'headlines publication\'.'
    return s

## Default
special = makeSpecial()

def eval(cmd):
    return "Today's headlines from The " + cmd['publication'] + ':\n' + headlines(cmd['url'])
