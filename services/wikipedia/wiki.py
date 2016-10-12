import urllib2, urllib
import re
import sys
from bs4 import BeautifulSoup


def getWiki(input):
    url = 'https://en.wikipedia.org/wiki/'
    page = input.replace(" ", "_")
    url += ''.join(page)
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        for tag in soup.find_all('b'):
            tag.replaceWith('')
        body = soup.findAll("p")[0].get_text()
        if body == "Wikipedia does not have an article with this exact name." or body.endswith(" may refer to:"):
            print("\nCould not find wiki information.\n")
        else:
            print("\n" + body + "\n")
            
    except Exception, e:
        print str(e)
        print("\nCould not find wiki information.\n")

def makeSpecial():
    s = 'To search for a wiki article, use the format \'wiki search_item\'.'
    return s

special = makeSpecial()

def eval(input):
    return getWiki(input)
