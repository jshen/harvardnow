import urllib2, urllib
import re
from bs4 import BeautifulSoup

#############################
##    Weather Function     ##
#############################

def getMBTAData(cmd):
    overall_body = []

    # iterate through all station requests
    for pg in cmd['pg']:
        url = 'http://www.mbtainfo.com/'
        url += pg
        hdr = {'User-Agent': 'Chrome'}
        req = urllib2.Request(url,headers=hdr)
        website = urllib2.urlopen(req)
        soup = BeautifulSoup(website.read(), 'html.parser')

        try:
            # get elements from a.minor until div.ads
            times = soup.find("a", class_="minor").find_next_siblings()
            # delete all elements after last ul
            for i, x in enumerate(reversed(times)):
                if x.name == 'ul':
                    times = times[:-i]
                    break

            # define generator function for generating the proper string from each html element
            def gen_body():
                for element in times:
                    for string in element.strings:
                        yield string.replace(u'\u2014', '-')

            body = gen_body()

            # add new lines before any header lines
            for b in filter(lambda x: len(x) > 1, body):
                if not (unicode(b)[0].isdigit() or b.startswith("Arriving")):
                    overall_body.append("")
                overall_body.append(b)

        except Exception, e:
            print str(e)
            return "Could not find T data. Are you sure you gave a proper line and station name? Additionally, "
            "this service only works for red, blue, orange, and green lines."

    # return all the train information stings joined as one
    return "\n".join(overall_body[1:])

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the shuttle for a particular line, use the format \'MBTA line station\'.'
    return s

# return proper format to use for getting train information
special = makeSpecial()

def eval(cmd):
    return getMBTAData(cmd)

# pass mock values if running from terminal
if __name__ == "__main__":
    print(getMBTAData({"pg": ["red/RHAR", "green/haecl", "blue/BWON"]}))
