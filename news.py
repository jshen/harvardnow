import urllib2, urllib
from bs4 import BeautifulSoup

#############################
##    Crimson Function     ##
#############################  

def getNews():
	result = ''
	url = 'https://www.thecrimson.com/'
	website = urllib2.urlopen(url)
	soup = BeautifulSoup(website.read(), 'html.parser')

	article = soup.find(id='primary-first-top')

	title = article.a.text

	return(title)

def makeSpecial(): 
	s = 'Just type the word news to get the latest crimson headline.'

special = makeSpecial()
