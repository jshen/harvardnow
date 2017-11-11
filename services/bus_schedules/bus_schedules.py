import urllib2, urllib
from bs4 import BeautifulSoup
import data

def getTimes(busid, direction):
    url = ('https://mbta.com/schedules/{}/schedule?direction_id={}&origin=place-harsq#origin').format(busid, direction)
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    times = []
    data_rows = soup.find_all('div','realtime-content')
    times.extend(data_rows[0].string)
    times.extend(data_rows[1].string)
    times.extend(data_rows[2].string)
    return 'Times: ' + times[0] + ', ' + times[1] + ', ' + times[2]


def eval(cmd):
    return getTimes(cmd['busid'], cmd['direction'])

special = "Text a bus number and the service will send the times for the next few stops"
