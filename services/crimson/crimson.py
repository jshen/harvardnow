import urllib2, urllib
from bs4 import BeautifulSoup
import data

#############################
##    Crimson Function     ##
#############################

def getHeadlines():
	headlines = []
	website = urllib2.urlopen('http://www.thecrimson.com')
	soup = BeautifulSoup(website.read(), 'html.parser')
	headline_divs = soup.find_all("div", {"class" : "article-content"})
	
	# return at most 7 headlines/articles
	while len(headline_divs) > 7:
		del headline_divs[-1]
	for headline_div in headline_divs:
		headline_words = headline_div.a.string
		headline_link = "http://www.thecrimson.com" + headline_div.a['href']
		s = headline_words + ": " + headline_link
		headlines.append(s)

	return headlines


############################
##       Top-Level        ##
############################

def makeSpecial():
	s = "Crimson headlines today:\n"
	headlines = getHeadlines()
	s += '\n'.join([headline for headline in headlines])
	return s

## return headlines
special = makeSpecial()

def eval():
	return makeSpecial();