import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Weather Function     ##
#############################

def getHolidays(input):
    try: 
        inputText = ''.join(input).lower()
        for i in ["yesterday", "today", "tomorrow"]:
            if i in inputText:
                day = i
                break
        else:
            return "That's not a valid number"
    except ValueError:
        return "That's not a choice" 
    body = "Holidays {}:\n".format(i)
    url = 'https://www.checkiday.com'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')
    try: 
        if (day == "today"):
            card = soup.find(id="portion4")    
        elif (day == "tomorrow"):
            card = soup.find(id="portion6")
        elif (day == "yesterday"):
            card = soup.find(id="portion2")

        days = card.find_all("a") 
        for holiday in days:
            if "Day" in holiday.text:
                body += holiday.text + "\n"
    except Exception, e:
        print str(e)
        return "Could not get fun fact"
    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'Get holidays day (yesterday, today, tomorrow) \'holidays day\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getHolidays(input)


