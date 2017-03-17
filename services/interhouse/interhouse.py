try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from bs4 import BeautifulSoup
import data

def getInfo(house, meal):
   message = ''
   url = 'https://dining.harvard.edu/campus-dining/undergraduate-dining/hours-interhouse-restrictions'
   website = urllib2.urlopen(url)
   soup = BeautifulSoup(website.read(), 'html.parser')
   col = 0
   row = 0
   if meal == 'breakfast':
       col = 1
   if meal == 'lunch':
       col = 2
   if meal == 'dinner':
       col = 3
   if meal == 'brain break':
       col = 4

   if house == 'adams':
       row = 1
   if house == 'annenberg':
       row = 2
   if house == 'cabot':
       row = 3
   if house == 'dunster':
       row = 4
   if house == 'eliot':
       row = 5
   if house == 'kirkland':
       row = 7
   if house == 'leverett':
       row = 8
   if house == 'lowell':
       row = 9
   if house == 'mather':
       row = 10
   if house == 'pforzheimer':
       row = 11
   if house == 'quincy':
       row = 12
   if house == 'winthrop':
       row = 12

   rows = soup.find_all('tr')

   r = rows.next_sibling
   count = 0
   while (count < row):
       r = r.next_sibling

   cols = r.find_all('td')
   c = cols.next_sibling
   count = 0
   while (count < col):
       c = cols.next_sibling

   content = c.find_all('p')
   for con in content:
       message += c.text
       message += " "

   return message


def makeSpecial():
    s = 'To get the interhouse dining hours for a specific house, use the format \'house meal\'.'
    return s


############################
##       Top-Level        ##
############################

## return list of valid laundry rooms
special = makeSpecial()

def eval(cmd):
    return cmd['house'] + cmd['meal'] + getInfo(cmd['house'], cmd['meal'])