import urllib2, urllib
from dateutil.parser import parse
from bs4 import BeautifulSoup

def parseInput(date):
    url = 'http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp'
    url_lunch = url + "?type=30&meal=1"
    url_dinner = url + "?type=30&meal=2"
    try:
        date = parse(date)
        url_lunch += date.strftime("&date=%m-%d-%Y")
    except:
        pass
    out = "Lunch:"
    for item in getEntrees(url_lunch):
        out += "\n" + item
    out += "\n\nDinner:"
    for item in getEntrees(url_dinner):
        out += "\n" + item
    return out
    
def getEntrees(url):
    menu = []
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    categories = soup.find_all("tr", "category")
    for category in categories:
        category_name = category.find("td")
        if category_name.text == "ENTREES":
            indicator = True
            while indicator:
                category = category.next_sibling
                item = category.find("a")
                if item == -1:
                    pass
                elif item is not None:
                    menu.append(item.text.strip())
                else:
                    indicator = False
    return menu
    
############################
##       Top-Level        ##
############################

def eval(input):
    return parseInput(input)
