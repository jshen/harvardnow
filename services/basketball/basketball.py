import urllib2, urllib
from bs4 import BeautifulSoup
import data

special = "Please type the 3-letter acronym of your basketball team in capitals, for example:"
special += "\nGSW\nNYK\nMIN"

def getstats(team):
    url += 'http://www.basketball-reference.com/teams/%s/2016.html' % team
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    return "hi"

def eval(cmd):
    return getstats(cmd['team'])

#cmd['label']+'\n'+machines_to_string(getMachines(cmd['roomid'],cmd['machinetype']))
