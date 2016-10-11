import urllib2, urllib
from bs4 import BeautifulSoup

#############################
##    Harambe Function     ##
#############################

# Scrapes the current top link from the harambe subreddit
# https://www.reddit.com/r/harambe
def getHarambePost():
    base_url = 'https://www.reddit.com'
    subreddit_url = base_url + '/r/harambe'

    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(subreddit_url, headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        top_post = soup.find_all('a', class_='title')[0]
        link = top_post.get('href')
        if link[:4] != 'http':
            link = base_url + link

    except Exception, e:
        print str(e)
        return "Could not scrape harambe subreddit :("

    return link

def makeEvalString():
    gorilla = \
"""\
      ."`".
  .-./ _=_ \.-.
 {  (,(oYo),) }}
 {{ |   "   |} }
 { { \(---)/  }}
 {{  }'-=-'{ } }
 { { }._:_.{  }}
 {{  } -:- { } }
 {_{ }`===`{  _}
((((\)     (/))))\
"""
    return gorilla + '\n\n' + getHarambePost()

def makeSpecial():
    return 'Get the top post from /r/harambe.'

############################
##       Top-Level        ##
############################

special = makeSpecial()

def eval():
    return makeEvalString()
