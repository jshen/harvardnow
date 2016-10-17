import urllib2, urllib
from bs4 import BeautifulSoup
import data

#############################
##    Laundry Function     ##
#############################    

def getSEEASEvents():
    url = 'http://www.seas.harvard.edu/events'
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')

    # final string to be returned to user
    final_string = ""

    # find all events on seas website
    all_events = soup.find_all('div', class_="views-row")

    # number of events to display to user
    num_events = 3 

    for index, event in enumerate(all_events):
        # display desired number of events
        if index > num_events - 1:
            break 

        # extract important information from events
        try:
            event_title = event.find("div", {"class": "evtitle"}).a.text
            final_string += "Event: " + event_title + "\n"
        except:
            final_string += ""

        try:
            event_speaker = event.find("div", {"class": "evspeaker"}).text
            final_string += "Speaker: " + event_speaker + "\n"
        except:
            final_string += ""

        try:
            date_day = event.find("span", {"class": "event_day"}).find("span", {"class": "date-display-single"}).text
            date_dow = event.find("span", {"class": "event_dow"}).find("span", {"class": "date-display-single"}).text
            final_string += "Date: " + str(date_day) + " " + str(date_dow) + "\n"
        except:
            final_string += ""

        try:
            event_loc = event.find("div", {"class": "evdate"}).text #.split("</span")[1]
            final_string += "Time: " + event_loc + "\n"
        except:
            final_string += ""

        final_string += "\n"

    # return str(all_events)

    return final_string
    # washer_div = soup.find(id=machinetype)
    
    # machine = washer_div.next_sibling
    # if machinetype == 'washer':
    #     while 'id' not in machine.attrs or machine['id'] != 'dryer':
    #         machines.append({'lr': roomid,
    #          'id': machine.a['id'],
    #          'name': `(machine.a.text)`.split('\\xa0')[0][2:],
    #          'time': machine.a.p.text})
    #         machine = machine.next_sibling
    # else:
    #     while machine and machine.name == 'li':
    #         machines.append({'lr': roomid,
    #          'id': machine.a['id'],
    #          'name': `(machine.a.text)`.split('\\xa0')[0][2:],
    #          'time': machine.a.p.text})
    #         machine = machine.next_sibling
    # return machines
############################
##       Top-Level        ##
############################

## return list of valid laundry rooms
# special = makeSpecial()

def eval(cmd):
    return getSEEASEvents() #cmd['label']+'\n'+ "Woohoo" machines_to_string(getMachines(cmd['roomid'],cmd['machinetype']))
