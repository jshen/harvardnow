import datetime
import urllib
import urllib2
from bs4 import BeautifulSoup




def getTruckData(input):
    dt = datetime.date.today()
    date = dt.strftime('%m-%d-%Y')


    url = 'http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp?date={}&type=30&meal=1'.format(date)
    print date
    #url += '+'.join(i)
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        for div in soup.find_all('div', class_='item_wrap'):
            food = div.find('a').contents[0]
            print food
        #food = menu.find_all('span', class_="item_wrap")

        #label = day.h3.text + '\n' if day.h3 is not None else ''

        #overview = day.img.attrs['title'] + '\n' if day.img is not None and day.img.has_attr('title') else ''
        #trucks = 'Name: ' + day.find_all(class_='event-title')[0].text.encode('unicode-escape').replace(r'\xb0','') + '\n' if len(day.find_all(class_='event-title')) > 0 else ''
        body = food

    except Exception, e:
        print str(e)
        return "Could not find data. Try again"
    print body
    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To see the food trucks available today, use the format \'food trucks\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getTruckData(input)

if __name__ == "__main__":
    getTruckData("")
