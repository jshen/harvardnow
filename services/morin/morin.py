import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##       David Morin       ##
##  Office Hours Function  ##
#############################    

def getHours(dayofweek):
    url = 'http://www.people.fas.harvard.edu/~djmorin/office_hours.htm'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    ohResult = ''

    try:
        ohTable = soup.find('table', {'id': 'AutoNumber1'})
        
        for ohRow in ohTable.find_all('tr'):
            ohCols = ohRow.findAll('td')
            if ohCols[0].find('font').text == dayofweek:
                ohResult = ohCols[1].text
                break

        ohTitle = soup.find('p').find('b').find('font').text

    except Exception, e:
        print str(e)
    
    if ohResult == '':
        return "Could not find office hour data. Are you sure you gave a proper day of week?"

    body = ohTitle + '\n' + dayofweek + ': ' + ohResult

    return body

def makeSpecial():
    s = "Gets David Morin's office hours."
    return s
    
############################
##       Top-Level        ##
############################

## return description of function
special = makeSpecial()

def eval(cmd):
    return getHours(cmd['dayofweek'])