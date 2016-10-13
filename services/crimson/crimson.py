SEARCH_URL = "https://www.thecrimson.com/search/?cx=013815813102981840311%3Aaw6l9tjs1a0&cof=FORID%3A10&ie=UTF-8&q="
HOME_URL = "https://www.thecrimson.com/"
# Temporary special string 
special = "In order to receive a list of links to the top 5 crimson articles returned by searching the crimson for a string, use the command \'crimson [search]\'."


## To test this method, I'm temporarily importing these modules.  
import urllib2
from bs4 import BeautifulSoup

# Get top articles
# Returns a dictionary mapping article name to link
def getTopArticles():
	url = HOME_URL
	website = urllib2.urlopen(url)
	soup = BeautifulSoup(website.read(), 'html.parser')
	shell = soup.find("div", id="most-read-box")
	mostRead = shell.find_all("li", class_ = "article-listitem")
	d = {}
	for i in mostRead:
		title = i.find("div", class_ ="article-listitem-text").text.strip()
		# avoiding doubling the backslash 
		link = HOME_URL[:-1] + i.find("a")["href"].strip()
		d[title] = link
	return d

# One interesting thing is that when we run this search on the url, it sorts them by relevance.
# There's a selector we might want to think about changing to sort by date
#incomplete
def searchCrimson(search):
	# replacing whitespace in their search with a plus sign
	search = search.replace(" ", "+")
	url = SEARCH_URL
	url += search
	print(url)
	website = urllib2.urlopen(url)
	soup = BeautifulSoup(website.read(), 'html.parser')
	print(soup.prettify())


def eval(cmd):
	pass

d = getTopArticles()
print(d.values())
#for i in getTopArticles():
#	print(i.prettify())



