from bs4 import BeautifulSoup
import urllib2


def get_link_and_alt_text():
	url = "https://www.instagram.com/deankhurana/"
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), 'html.parser')
	data = soup.find(class_= '_8mlbc _vbtk2 _t5r8b')
	link = data.get('href')
	alt_text = data.find('img').get('alt')

	return link + "\n" + alt_text

def makeSpecial():
	s = "Here's the latest instagram post from Dean Khurana! \n"
	s += get_link_and_alt_text()
	return s
	
#toplevel

special = makeSpecial()

def eval():
	return special