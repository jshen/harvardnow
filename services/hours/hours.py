import urllib2, urllib
import re
from bs4 import BeautifulSoup

library = {'baker', 'cabot', 'fung', 'grossman', 'kennedy', 'law', 'yenching', 'houghton', 'lamont', 'loeb', 'widener}

libraries = {'baker': 'BAK', 'cabot': 'CAB', 'fung': 'FUN', 'grossman': 'GRO', 'kennedy': 'KSG', 'law': 'LAW', 'yenching': 'HYL', 'houghton': 'HOU', 'lamont' : 'LAM', 'loeb': 'DES', 'widener': 'WID'}

dhalls = {'adams': 'Row-Column-8', 'annenberg': 'Row-Column-9', 'cabot': 'Row-Column-10', 'currier': 'Row-Column-11', 'dunster': 'Row-Column-12', 'eliot': 'Row-Column-13', 'hillel': 'Row-Column-14', 'kirkland': 'Row-Column-13', 'leverett': 'Row-Column-15', 'lowell': 'Row-Column-16', 'mather': 'Row-Column-10', 'pfoho': 'Row-Column-17', 'pforzheimer': 'Row-Column-17', 'quincy': 'Row-Column-18', 'winthrop': 'Row-Column-19', 'flyby': 'Row-Column-20', 'fly by': 'Row-Column-20', 'fly-by': 'Row-Column-20'}

buildings = {'hemenway', 'mac', 'malkin', 'malkin athletic center', 'mail', 'mail center', 'dorm crew'}

cafes = {'barker': 'views-row-1', 'bauer': 'views-row-2', 'queen\'s head': 'views-row-3', 'cqh': 'views-row-3', 'cambridge queen\'s head': 'views-row-3', 'pub': 'views-row-3', 'cambridge queen\'s head pub': 'views-row-3', 'chauhaus': 'views-row-4', 'cgis': 'views-row-5', 'cronkhite': 'views-row-6', 'dudley': 'views-row-7', 'hks': 'views-row-8', 'kennedy': 'views-row-8', 'hls pub': 'views-row-9', 'lamont': 'views-row-10', 'lamont cafe': 'views-row-10', 'lise': 'views-row-11', 'northwest': 'views-row-12', 'observatory': 'views-row-13', 'sebastian\'s': 'views-row-14', 'sebastians': 'views-row-15'}

#############################
##     Hours Functions     ##
#############################

def getLibHours(input):
    url = 'http://library.harvard.edu/find-library'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')
    
    try:
        libId = libraries[input.lower()]
        card = soup.find(id='CAB')
        
        hours = 'Hours: ' + card.find_all(class_='hr-text')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='hr-text')) > 0 else ''
        
        body += hours
    except Exception, e:
        print str(e)
        return "Could not find library hours. Are you sure you gave a proper library name?"
    
    return body

#def getDiningHours(input):
#    url = 'https://dining.harvard.edu/campus-dining/undergraduate-dining/hours-interhouse-restrictions'
#    hdr = {'User-Agent': 'Chrome'}
#    req = urllib2.Request(url,headers=hdr)
#    website = urllib2.urlopen(req)
#    soup = BeautifulSoup(website.read(), 'html.parser')
#
#    try:
#        dhallClass = dhalls[input.lower()]
#        card = soup.find(id=dhallClass)
#        
#        hours = 'Hours: ' + card.find_all(class_='house-text para-style-override-5')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='house-text para-style-override-5')) > 0 else ''
#
#        body += hours
#    except Exception, e:
#        print str(e)
#        return "Could not find dining hall hours. Are you sure you gave a proper dhall name?"
#
#    return body
#
#def getCafeHours(input):
#    url = 'https://dining.harvard.edu/cafes'
#    hdr = {'User-Agent': 'Chrome'}
#    req = urllib2.Request(url,headers=hdr)
#    website = urllib2.urlopen(req)
#    soup = BeautifulSoup(website.read(), 'html.parser')
#    
#    try:
#        cafeClass = cafes[input.lower()]
#        card = soup.find(id=cafeClass)
#        
#        hours = 'Hours: ' + card.find(class_='field-item even')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='field-item even')) > 0 else ''
#        
#        body += hours
#    except Exception, e:
#        print str(e)
#        return "Could not find cafe hours. Are you sure you gave a proper cafe name?"
#    
#    return body
#
#def getBuildingHours(input):
#    url = 'http://www.google.com/search?q='
#    url += '+'.join(input)
#    hdr = {'User-Agent': 'Chrome'}
#    req = urllib2.Request(url,headers=hdr)
#    website = urllib2.urlopen(req)
#    soup = BeautifulSoup(website.read(), 'html.parser')
#    
#    try:
#        card = soup.find(id='rhs_block').find_all(class_='_RBg')[0]
#        hours = 'Hours: ' + card.find_all(class_='_X0c')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(card.find_all(class_='_X0c')) > 0 else ''
#        body = hours
#    
#    except Exception, e:
#        print str(e)
#        return "Could not find building/gym hours. Are you sure you gave a proper building/gym name?"
#    
#    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the hours for a particular location, use the format \'hours location\'.'
    return s

## return proper format to use for getting hours
special = makeSpecial()

def eval(input):
    return getLibHours(input)
