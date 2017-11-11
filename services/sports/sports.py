import urllib2
from bs4 import BeautifulSoup

def getSportsGames(input):
    url = 'http://www.gocrimson.com/landing/index'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    five_events = []

    upcoming = soup.find_all('div', class_='event-box upcoming clearfix')

    for i in range(5):
        five_events.append(upcoming[i].find('div', class_='sport').text + " on "
                            + upcoming[i].find('div', class_='date clearfix')['title'] + " at "
                            + upcoming[i].find('div', class_='status').text)

    return getSportsGames

def makeSpecial():
    s = 'To get the next five upcoming sports game type \'Upcoming Sports Games\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getSportsGames(input)
