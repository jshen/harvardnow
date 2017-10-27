import urllib2
import datetime
from bs4 import BeautifulSoup


#####################################
##    Club Hub Events Function     ##
#####################################

def getEvents():
    events = []
    url = 'https://h.clubhub.live/'

    website = urllib2.urlopen(urllib2.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    ))
    soup = BeautifulSoup(website.read(), 'html.parser')
    event_divs = soup.select(".event")

    for event_div in event_divs:
        if not event_div:
            continue
        event = {
            'name': event_div['data-name'],
            'host': event_div['data-host'],
            'starts': int(event_div['data-start'])
        }

        now = int(datetime.datetime.now().strftime("%s"))
        if event['starts'] > now + 24 * 60 * 60:
            continue

        events.append(event)

    return events


############################
##       Top-Level        ##
############################

def eval(cmd):
    events = getEvents()
    return "Events in the next 24 hours:\n" + \
           "\n".join([
               "{}: {} ({})".format(
                   datetime.datetime.fromtimestamp(event['starts']).strftime("%a %-I:%M%p"),
                   event['name'],
                   event['host']
               )
               for event in events]) + "\n" + \
           "(Read more on Club Hub: https://h.clubhub.live)\n\n"
