import urllib2, urllib
from bs4 import BeautifulSoup

#############################
##    Laundry Function     ##
#############################    

def getRecent():
    url = 'https://www.thecrimson.com'
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')
    news_div = soup.find(id="most-read-box")
    articles = news_div.findAll('li', {'class':'article-listitem'})
    data = []
    for a in articles:
        link = url + a.find('a')['href']
        title = a.find('div', {'class':'article-listitem-text'}).contents[0]
        data.append({'title':title, 'link':link})
    return data
    
def news_to_string(news):
    s = ''
    for a in news:
        s += a['title'] + a['link'] + '\n'
    return s

def makeSpecial():
    s = "News Options: \n"
    s += "Recent \n"
    return s
    
############################
##       Top-Level        ##
############################

## return list of valid laundry rooms
special = makeSpecial()

def eval(cmd):
    return 'News:'+'\n'+news_to_string(getRecent())

print special
print news_to_string(getRecent())
