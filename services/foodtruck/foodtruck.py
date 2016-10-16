##############################################################
##    Elizabeth Yeoh-Wang, Andrew Tran, and William Wang    ##
##############################################################

import urllib2, urllib 
from bs4 import BeautifulSoup
import datetime

# get today's date and the date a week from today
today = datetime.datetime.now()
week = today + datetime.timedelta(days=7)

# format string for foodtruck schedule url
today_string = today.strftime("%Y%m%d")
week_string = week.strftime("%Y%m%d")

#############################
##    Foodtruck Function   ##
#############################    

def getFoodtruck(user_input):
    
    # url to foodtruck schedule
    url = 'https://calendar.google.com/calendar/htmlembed?&mode=AGENDA&wkst=1&src=0pa55cqrvtpcalggvn5mr0kpio@group.calendar.google.com&ctz=America/New_York&dates=' 
    url += (today_string + '/' + week_string) 

    # open url
    website = urllib2.urlopen(url)
    
    # parse html
    soup = BeautifulSoup(website.read(), 'html.parser')

    # return requested foodtruck schedule 
    output = ""
    if (user_input == "today"):
        day = soup.find(class_='date-section')
        output = str_from_day(day)
    elif (user_input == "tomorrow"):
        day = soup.find(class_='date-section').next_sibling.next_sibling
        output = str_from_day(day)
    elif (user_input == "week"):
        day = soup.find(class_='date-section')
        output = (str_from_day(day) + '\n')
        for i in range(0, 6):
            day = day.next_sibling.next_sibling
            output += (str_from_day(day) + '\n')
    return output    

# return the events for a specific day
def str_from_day(day):
    cur_date = day.find(class_='date').text

    events = day.find(class_='events')
    event = events.find(class_='event')

    str = cur_date
    while (event.next_sibling != None):
        str += ('\n' + event.find(class_='event-time').text + ' - ' + event.find('span', class_='event-summary').text)
        event = event.next_sibling.next_sibling
    str += ('\n' + event.find(class_='event-time').text + ' - ' + event.find('span', class_='event-summary').text + '\n')
    return str

# return usage guide
def makeSpecial():
    return 'Enter \"foodtrucks [today/tomorrow/week]\"'

############################
##       Top-Level        ##
############################

# return usage guide
special = makeSpecial()

# return list of foodtrucks
def eval(cmd):
    return getFoodtruck(cmd['user_input'])