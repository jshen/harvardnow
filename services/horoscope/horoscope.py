from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import urllib, urllib2, json


#############################
##          Setup          ##
#############################
signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
base_url = 'http://horoscope-api.herokuapp.com/horoscope/today/'

##############################
##    Horoscope Functions     ##
##############################

# get the horoscope of sign using api: https://github.com/tapasweni-pathak/Horoscope-API
def getHoroscope(sign):
    url = base_url + sign.lower()
    website = urllib2.urlopen(url)
    data = json.loads(website.read())

    # bug in the api always adds a "[' " to the front of the horoscope
    horoscope = data['horoscope'].replace('[\' ', '')

    response = "Today's horoscope for %s:\n\n%s" % (sign.title(), horoscope)
    return response


# used to gather the list of the signs for makeSpecial
def makeSignList():
    s = ''
    for sign in signs:
        s += "%s\n" % (sign.title())
    return s


def makeSpecial():
    response = 'Usage: horoscope [sign]\n\nList of available signs:\n'
    sign_list = makeSignList()
    response += sign_list
    return response


#############################
##        Top-Level        ##
#############################

## list of valid signs
special = makeSpecial()

def eval(cmd):
    sign = cmd['sign'].lower()
    if sign in signs:
        return getHoroscope(sign)
    else:
        return "Incorrect sign! Available signs are:\n%s" % (makeSignList())

# testing code
if __name__ == '__main__':
    print ''
    print getHoroscope('CaNcEr')
    print ''
    print eval({'sign': 'pisces'})
