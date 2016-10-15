import urllib2, urllib
from bs4 import BeautifulSoup
import data

special = "Please type the 3-letter acronym of your basketball team in capitals, for example:"
special += "\nGSW\nNYK\nMIN"

# Retrieves info about basketball team from basketball-reference.com
def getstats(team):
    url += 'http://www.basketball-reference.com/teams/%s/2016.html' % team
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    info = soup.find(id="info")
    if info == None:
    	return "an error occurred"
    else:
    	return info.get_text()

def eval(cmd):
    return getstats(cmd['team'])
