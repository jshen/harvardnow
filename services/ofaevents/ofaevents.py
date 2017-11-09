import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##     Events Function     ##
#############################

special = "To get events for today, use the format \'events\'"

def getEventData():
    url = 'https://ofa.fas.harvard.edu/calendar/upcoming'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url, headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:

        #find 10 events
        allEventText = ""
        eventDateSpan = soup.find_all(class_='event-start')
        allEvents = soup.find_all(class_='node-header')
        for i in range(0,10):
            # find 10 dates
            eventMonth = eventDateSpan[i*2].find_all_next(class_='event-start-month')[0]
            eventMonth =  str(eventMonth)[str(eventMonth).index('>')+1:str(eventMonth).index("</")]
            eventYear = eventDateSpan[i*2].find_all_next(class_='event-year')[0]
            eventYear =  str(eventYear)[str(eventYear).index('>')+1:str(eventYear).index("</")]
            eventDay = eventDateSpan[i*2].find_all_next(class_='event-start-day')[0]
            eventDay =  str(eventDay)[str(eventDay).index('>')+1:str(eventDay).index("</")]

            #print eventMonth + " " + eventDay + " " + eventYear

            #find Title
            title = allEvents[i].find_all_next(class_='node-title')[0]
            title = title.find('a')
            title = str(title)[str(title).index('>')+1:str(title).index("</")]
            allEventText += (eventMonth + " " + eventDay + " " + eventYear + ": " + title + "\n")





    except Exception, e:
        print str(e)
        return "you a bitch"

    return allEventText

def eval(cmd):
    return getEventData