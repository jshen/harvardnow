import urllib2, urllib
import re
from random import randint
from bs4 import BeautifulSoup

#########################################
##  Election Data Gathering Function   ##
#########################################
def getElectionData(state, race, district):
    state = state.lower()
    if not isState(state):
        return randomCapitalize(state + " is not a state.")
    
    if race == 'house':
        race = 'district-' + str(district).zfill(2)
 
    state = state.replace(" ", "-")
    url = 'https://www.politico.com/election-results/2018/' + state + '/'
    hdr = {'User-Agent': 'Chrome'}
    req = urllib2.Request(url,headers=hdr)
    website = urllib2.urlopen(req)
    soup = BeautifulSoup(website.read(), 'html.parser')

    try:
        section = soup.find("section", {"name" : race})
        results_table = section.find_all("td", {"class" : "candidate"})
        for i in range(len(results_table)):
            results_table[i] = results_table[i].get_text()
            results_table[i] = results_table[i].strip()
            
        try:     
            results_table.remove("Other") 
        except:
            pass

        results_table = [x.replace("*", " (Incumbent)") for x in results_table]
        winner = results_table[0]
        losers = results_table[1:]
        loserstring = ", ".join(losers)
        body = "Winner: " + winner + "\n" + "Loser(s): " + loserstring
        

    except Exception, e:
        print str(e)
        return "Could not find data."

    return body

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'This will get the word of the day.'
    return s

## return proper format
special = makeSpecial()

def isState(state):
    states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware',
            'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
            'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana',
            'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina',
            'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina',
            'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington',
            'west virginia', 'wisconsin', 'wyoming']
    return state in states

def eval(input):
    length = len(input)

    state = None
    race = None
    district = None
    
    if(length >= 1):
        state = input[0]
    if(length >= 2):
        race = input[1]  
    if(length >= 3):
        district = str(input[2])   
        
    print(state + ", " + race + ", " + str(district))
    
    if not state:
        return "Please specify a state."
    
    if district:
        return getElectionData(state, race, district) if (race == "house") else "Please specify a district if looking for house"
    elif race:
        return getElectionData(state, race, None)
    else:
        return "Please specify a race."
 
        
    
def randomCapitalize(string):
    s = ""
    for i in string:
        num = randint(0,1)
        if num == 1:
            s += i.upper()
        else:
            s += i
    return s


print(eval(["mexico", "house", 2]))