import re
from bs4 import BeautifulSoup
import urllib

#############################
##    Patriots Function     ##
#############################

def getPatsData(input):

	r = urllib.urlopen('http://www.nfl.com/liveupdate/scorestrip/ss.xml').read()
	soup = BeautifulSoup(r, 'lxml')

	for g in soup.find_all('g'):
		if g['h'] == 'NE' or g['v'] == 'NE':
			print 'Last Game Score: '
			print g['h'] + ': ' + g['hs'] + ' - ' + g['v'] + ': ' + g['vs']
			if(g['v'] == 'NE' and g['vs'] > g['hs']):
				print 'PATS WIN!!!!'
			elif(g['h'] == 'NE' and g['hs'] > g['vs']):
				print 'PATS WIN!!!!'
			else:
				print 'Don\'t worry about it champ. Brady is still the GOAT'

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the Patriots latest game score, type \'pats\''
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    return getPatsData(input)