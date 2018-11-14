import urllib2, urllib
from bs4 import BeautifulSoup
import data

#############################
##    HKS Cafe Menu Function     ##
#############################

def getMenu(meal):
	menu = []
	url = 'http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp?type=56&meal='
	## Depending on the meal type, get different meal
	if meal == 'Lunch':
		url += '0'
	else if meal == 'Dinner':
		url += '1'
	else:
		return "Please enter a valid meal type."

	hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)

    try:
		website = urllib2.urlopen(req)
		soup = BeautifulSoup(website.read(), 'html.parser')
		selections = soup.find_all("div", {"class" : "item_wrap"})
		for selection in selections:
			menu.append(selection.a.get_text())
	except Exception, e:
		pring str(e)
		return "Could not find menu. Please make sure you entered a valid meal type."	

	return menu

def menu_to_string(food):
	s = ''
	for selection in menu:
		s += selection + '\n'
	return s

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'Use \'Lunch\' or \'Dinner\' to indicate which menu you want.'
    return s

# Return proper format to use for getting menu
special = makeSpecial()

def eval(cmd):
	return cmd['label']+'\n'+menu_to_string(getMenu(cmd['meal']))

