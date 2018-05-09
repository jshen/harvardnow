import urllib2, urllib
from bs4 import BeautifulSoup

special = "Gives events in the square using harvardsquare.com"

def getEvents():
	website = urllib2.urlopen('')
    soup = BeautifulSoup(website.read(), 'html.parser')
    return soup.find(id='block-system-main').find(class_='view-content').text.encode('utf-8')

def eval(cmd):
    return getEvents()
