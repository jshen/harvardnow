import urllib2, urllib
from bs4 import BeautifulSoup

def headlines(url_string):
    # String containing all headlines from main page
    headlines = ''

    # Set up headline parser
    website = urllib2.urlopen(url_string)
    soup = BeautifulSoup(website.read(), 'html.parser')
    headline_tag = soup.find('a', href=True)

    # Add first headline
    headline = headline_tag.get_text()
    headlines += headline + '\n'

    # Iterate through all headlines
    next_h = headline.next_sibling
    while next_h != None:
        headlines += next_h + '\n'
        nexth = headline.next_sibling

    return headlines

def makeSpecial():
    s = 'To get the headlines from a particular publication, use the format \'headlines publication\'.'
    return s

## Default
special = makeSpecial()

def eval(cmd):
    return "Today's headlines from The " + cmd['publication'] + ':\n' + headlines(cmd['url'])
