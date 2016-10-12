import urllib2, urllib
import re
from bs4 import BeautifulSoup
import datetime
import re

#############################
##     Event Function      ##
#############################

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
    'June': 6, 'July': 7, "August": 8, 'September': 9, 'October': 10,
    'November': 11, 'December': 12}

def getEvents(input):
    url = 'http://www.harvard.edu/events'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    ## get current date
    today = datetime.date.today()

    try:
        cards = soup.find_all(class_ = 'card-callout-media__text')[:-1]
        body = "Events:\n\n"
        for card in cards:
            title = card.find(class_ = 'card--event__link').string.encode(
                "utf-8")
            time = card.find_all('p')[0].string.encode("utf-8")
            location = card.find_all('p')[1].string.encode("utf-8")
            link = card.find_all('a')[0].get('href').encode("utf-8")

            title = title.replace('\n','')
            time = time.replace('\n','')
            location = location.replace('\n','')

            month = time.replace(',', '').split(" ")[1]
            day = time.replace(',', '').split(" ")[2]

            if(months[month] == today.month and (int(day) == today.day
                or int(day) == today.day+1)):
                body += title + '\n'
                body += 'Time: ' + time + '\n'
                body += 'Location: ' + location + '\n'
                body += 'More Information: ' + link + '\n'

    except Exception, e:
        print str(e)
        return "Failed to retrieve any events"

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = """To get today\'s events at Harvard, use the format \'events\'. To get
    events for another day this week, use the format \'events mm\\dd """
    return s

## return proper format to use for getting events
special = makeSpecial()

def eval(input):
    return getEvents(input)
