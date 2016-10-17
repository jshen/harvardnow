import urllib2, urllib
import re
from bs4 import BeautifulSoup

# FAUST AND FURIOUS
### asdfhaksl;hdf FAUST laheiotapwhe
### 1. xxxx
### 2. xxxx
### Type fAUST 2002 3
months = ['JANUARY' : '01', 'JAN' : '01', 'FEBRUARY' : '02', 'FEB' : '02', 'MARCH' : '03', 'MAR' : '03', 'APRIL' : '04', 'APR' : '04', 'MAY' : '05', 'JUNE' : '06', 'JUN' : '06', 'JULY' : '07', 'JUL' : '07', 'AUGUST' : '08', 'AUG' : '08', 'SEPTEMBER' : '09', 'SEPT' : '09', 'OCTOBER' : '10', 'OCT' : '10', 'NOVEMBER' : '11', 'NOV' : '11', 'DECEMBER' : '12', 'DEC' : '12']
def getFaustData(input):#### FAUST [arg] --> FAUST[arg] --> [arg]  2002 September 2002
	mainurl = 'http://www.harvard.edu/president/speeches'
	errmsg = "To explore President Faust's speeches, use the format 'faust', 'faust year' or 'faust month year'."
	spcmsg = "To view a specific speech, use the format 'faust #x', 'faust year #x', or 'faust month year #x'."
	list = true
    elements = input.upper.split('#')
    inputs = elements[0].split(' ')
    args = len(inputs)
    month = ''
    elid=0
    if inputs[0] != "FAUST":
    	return errmsg
    if len(elements) == 2:
    	list = false
    	try:
    		elid = int(elements[1])
    	except Exception:
    		return spcmsg
    if len(inputs) == 2:
    	try:
    		int(inputs[1])
    		mainurl = mainurl + '/'+inputs[1]
    	except Exception:
    		return errmsg
    if len(inputs) == 3:
    	try:
    		int(inputs[2])
    		mainurl = mainurl + '/'+inputs[2]
    		month = months[inputs[1]]
    		else:
    			return errmsg
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(mainurl,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')
    try:
    	allcards = soup.find_all(class_='card')
    	cards = []
    	if month == '':
    		cards = allcards
    	else
    		cards = [card for card in allcards if card.find_all('time')[0]['datetime'].split('-')[1]==month]
    	body = ""
    	if list:
	    	1/len(cards)
	    	for i in range(len(cards)):
	    		body = body + "#" + (i+1) + ": " + cards[i].find_all(class_='card__title')[0].text[1:] + ", " + cars[i].find_all('time')[0].text + "\n"
    	else:
    		card = cards[elid]
    		body += card.find_all(class_='card__title')[0].text[1:] + "\n"
    		body += card.find_all('time')[0].text + "\n"
    		body += "Location: " + card.find_all(class_='card__content__heading') + "\n"
    		thisurl = "http://www.harvard.edu" + card.find_all('a')[0]['href'] 
    		body += "Read: " + thisurl + "\n"
    		thisreq = urllib2.Request(thisurl, headers=hdr)
    		thiswebsite = urllib2.urlopen(thisreq)
    		thissoup = BeautifulSoup(thiswebsite.read(), 'html.parser')
    		audio = thissoup.find_all(class_='audio-container')
    		if len(audio)>0:
    			body += "Listen: " + audio[0].find_all('iframe')[0]['src']
    except Exception, e:
        print str(e)
        return "Could not find any speeches in the given timeframe."

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    return getFaustData("FAUST")

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getFaustData(input)
