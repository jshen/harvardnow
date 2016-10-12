import urllib2, urllib
from bs4 import BeautifulSoup

#############################
##    Reddit Function      ##
#############################

def getRedditPost(subreddit, rank):
    base_url = 'https://reddit.com'
    url = base_url
    if subreddit != 'front':
        url = url + '/r/' + subreddit

    try:
        rank = int(rank)
    except Exception, e:
        print str(e)
        return '<rank> must be an integer.'

    if rank < 1:
        return '<rank> must be an integer greater than 0.'

    hdr = {'User-Agent': 'Chrome'}

    try:
        req = urllib2.Request(url, headers=hdr)
        website = urllib2.urlopen(req)
        soup = BeautifulSoup(website.read(), 'html.parser')
    except Exception, e:
        print str(e)
        return 'Could not find subreddit /r/' + subreddit + '.'

    try:
        post = soup.find(id='siteTable').find_all('a', class_='title')[rank - 1]
        link = post.get('href')
        if link[:4] != 'http':
            link = base_url + link
    except Exception, e:
        print str(e)
        return 'Could not scrape post from ' url + '.'

    return link

def makeSpecial():
    s = 'To get the post for a particular subreddit, use the format \'reddit <subreddit> <rank>\'.\n' + \
        'For posts on the front page, specify the subreddit as \'front\'.'
    return s

############################
##       Top-Level        ##
############################

special = makeSpecial()

def eval(input):
    try:
        keywords = input.split()
    except Exception, e:
        print str(e)
        return 'Use the format \'reddit <subreddit> <rank>\'.'

    return getRedditPost(keywords[0], keywords[1])
