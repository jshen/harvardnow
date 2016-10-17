import urllib2, urllib
import re
from bs4 import BeautifulSoup

# FAUST AND FURIOUS
months = {'JANUARY' : '01', 'JAN' : '01', 'FEBRUARY' : '02', 'FEB' : '02', 'MARCH' : '03', 'MAR' : '03', 'APRIL' : '04', 'APR' : '04', 'MAY' : '05', 'JUNE' : '06', 'JUN' : '06', 'JULY' : '07', 'JUL' : '07', 'AUGUST' : '08', 'AUG' : '08', 'SEPTEMBER' : '09', 'SEPT' : '09', 'OCTOBER' : '10', 'OCT' : '10', 'NOVEMBER' : '11', 'NOV' : '11', 'DECEMBER' : '12', 'DEC' : '12'}
def getFaustData(input):
	mainurl = 'http://www.harvard.edu/president/speeches'
	errmsg = "To explore President Faust's speeches, use the format 'faust', 'faust year' or 'faust month year'."
	spcmsg = "To view a specific speech, use the format 'faust #x', 'faust year #x', or 'faust month year #x'."
	args = " ".join([x for x in input])
	list = (len(args.split('#'))==1)
	elid = 0
	month = ''
	year = ''
	try:
		for i in input:
			if i.upper() == "FAUST":
				input.remove(i)
				break
		if not list:
			for i in input:
				if i[0] == '#':
					elid=int(i[1:])
					input.remove(i)
					break
		if len(input)==1:
			i = input.pop()
			int(i)
			year = "/" + i
		if len(input)==2:
			for i in input:
				if i.upper() not in months.keys():
					int(i)

					year  = '/' + i
				else:
					month = months[i.upper()]
	except Exception, e:
		print str(e)
		return errmsg
	mainurl += year
	hdr = {'User-Agent': 'Chrome'}
	req = urllib2.Request(mainurl,headers=hdr)
	website = urllib2.urlopen(req)
	soup = BeautifulSoup(website.read(), 'html.parser')
	try:
		allcards = soup.find_all(class_='card')
		cards = []
		if month == '':
			cards = allcards
		else:
			cards = [card for card in allcards if card.find_all('time')[0]['datetime'].split('-')[1]==month]
		body = ""
		if list:
			1/len(cards)
			length = len(cards)
			if len(cards)>7:
				body += "Showing most recent seven speeches in timeframe:\n"
				length = 7
			for i in range(length):
				body = body + "#" + str(i+1) + ": " + cards[i].find_all(class_='card__title')[0].text[1:] + ", " + cards[i].find_all('time')[0].text + "\n"
			body += spcmsg
		else:
			card = cards[elid-1]
			body += card.find_all(class_='card__title')[0].text[1:] + "\n"
			body += card.find_all('time')[0].text + "\n"
			body += "Venue: " + card.find_all(class_='card__content__heading')[0].text[1:] + "\n"
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
		return "No speech found in given timeframe."

	return body

############################
##       Top-Level    	  ##
############################

def makeSpecial():
	return getFaustData({"FAUST"})

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
	return getFaustData(input)
