import urllib2, urllib
from bs4 import BeautifulSoup
import data

#############################
##  Library Hour Function  ##
#############################    

url = 'http://library.harvard.edu/all-library-hours'
website = urllib2.urlopen(url)
soup = BeautifulSoup(website.read(), 'html.parser')
library_content = soup.find(input)
hours_content = library_content.find_all('span')
day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def getLibrary(input):
    if data1.library[input] != None:
        return 1
    else
        print "Try entering full library name.\n"
        return None

def getHours(input):
    if getLibrary(input) != None:
        counter = 0
        for i in hours_content:
            print "Opening and closing time for " + day_list[counter] + "this week: " + i.getText() + "\n"
            counter++

    
############################
##       Top-Level        ##
############################

def eval(input):
    getHours(input)
