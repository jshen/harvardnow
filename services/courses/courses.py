import urllib2
from bs4 import BeautifulSoup

#############################
##    Course Function     ##
#############################    

def getCourseInfo(input):
    url = 'https://courses.harvard.edu/search?'
    url += 'sort=score%20desc%2Ccourse_title%20asc&start=0&rows=25'
    url += '&q=%s' % input
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        instructors = soup.find(id='srl_instructor').text.encode('unicode-escape')
        desc = soup.find(id='srl_description').text.encode('unicode-escape')
        credits = soup.find_all('p')[2].text.encode('unicode-escape')
        location = soup.find_all('p')[3].text.encode('unicode-escape')

        body = 'Instructors: ' + instructors + '\n'
        body += desc + '\n'
        body += credits + '\n'
        body += location + '\n'

    except Exception, e:
        print str(e)
        return "Could not find course data. Are you sure you gave a proper course name?"

    return body


def makeSpecial():
    s = 'To get the info for a particular course, use the format \'courses course\'.'
    return s
    
############################
##       Top-Level        ##
############################

## return list of valid laundry rooms
special = makeSpecial()

def eval(input):
    return getCourseInfo(input)
