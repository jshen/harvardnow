## To test this method, I'm temporarily importing these modules.  
import urllib2
from bs4 import BeautifulSoup

from api import API

SEARCH_URL_OLD = "https://www.thecrimson.com/search/?cx=013815813102981840311%3Aaw6l9tjs1a0&cof=FORID%3A10&ie=UTF-8&q="
SEARCH_URL = "https://www.google.com/search?hl=en&as_q=REPLACE&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=&as_qdr=all&as_sitesearch=thecrimson.com&as_occt=any&safe=images&as_filetype=&as_rights="
HOME_URL = "https://www.thecrimson.com/"
# Temporary special string 
special = "In order to receive a list of links to the top 5 crimson articles returned by searching the crimson for a string, use the command \'crimson [search]\'."

# Get top articles
# Returns a dictionary mapping article name to link
def getTopArticles():
	url = HOME_URL
	website = urllib2.urlopen(url)
	soup = BeautifulSoup(website.read(), 'html.parser')
	shell = soup.find("div", id="most-read-box")
	mostRead = shell.find_all("li", class_ = "article-listitem")

	topArticles = []

	for i in mostRead:
		title = i.find("div", class_ ="article-listitem-text").text.strip()
		# avoiding doubling the backslash 
		link = HOME_URL[:-1] + i.find("a")["href"].strip()

		topArticles.append((title,link))

	return topArticles

# One interesting thing is that when we run this search on the url, it sorts them by relevance.
# There's a selector we might want to think about changing to sort by date
#incomplete
def searchCrimson(search):
	# replacing whitespace in their search with a plus sign
	search = search.replace(" ", "+")
	url = SEARCH_URL
	url.replace("REPLACE", search)
	print(url)
	website = urllib2.urlopen(url)
	soup = BeautifulSoup(website.read(), 'html.parser')
	print(soup.prettify())
	resultTest = soup.findAll("div")
	results = soup.findAll("div", class_="gsc-webResult gsc-result")
	for i in resultTest:
		i.prettify()

	print results

	for i in results: i.prettify()
	# print(soup.prettify())


def eval(cmd):
	pass

# searchCrimson("HUDS")
d = getTopArticles()
# print(d)

print "\n\n".join(map(lambda e: "{}: {}".format(e[0], e[1]), d))

#for i in getTopArticles():
#	print(i.prettify())



