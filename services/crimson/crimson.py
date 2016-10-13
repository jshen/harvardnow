## To test this method, I'm temporarily importing these modules.  
import urllib2
from bs4 import BeautifulSoup

HOME_URL = "https://www.thecrimson.com/"

# Temporary special string 
special = "Enter 'crimson' to get the top 5 articles. 📖"

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

def eval(cmd):
	# TODO: parse cmd and return top articles string
	pass

d = getTopArticles()

print "\n\n".join(map(lambda e: "{}: {}".format(e[0], e[1]), d))





