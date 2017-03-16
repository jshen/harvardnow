import urllib2, urllib
from bs4 import BeautifulSoup
from bs4 import element
import datetime

############################
##    Sports Function     ##
############################
'''
    Given month and day (and assuming current year), returns a formatted 
    string containing information about all Harvard Varsity sport events 
    on that day.

    Possible next steps:
    1. Use URL abbreviations of teamnames to filter by team
        a) e.g. "mlax" for men's lacrosse
    2. Define default behavior for no date
        a) next home game?
        b) events this weekend?
        c) if given team, score of last game/time of next game?
'''

# return a list of games -- each game contains info about one event
def getGames(date):
    try:
        month, day, year = date.split('/')
        games = []
        url = 'http://www.gocrimson.com/composite?'
        url += 'y={:04d}&m={:02d}'.format(int(year), int(month))
        website = urllib2.urlopen(url)
        soup = BeautifulSoup(website.read(), 'html.parser')

        # extract info from all events on the given date
        daydiv = soup.find('div', class_='cal-date', text=str(day))
        for event in daydiv.find_next_siblings():
            game = extract_event_info(event)
            if game:
                games.append(game)
        return games
    except Exception, e:
        print str(e)
        return "Could not find varsity sports data. Are you sure you sent a valid date?"

# given an event, extract info
def extract_event_info(event):
    event_cls = event.get('class')
    game = {}
    if event_cls and 'cal-event' in event_cls:
        game = {'team': '', 'comp': '', 'opp': '', 'loc': '', 'stat': '',
                'res' : '', 'ls'  : '', 'v'  : '', 'bx' : '', 
                't'   : '', 'dr'  : '', 'rc' : '', 'pr' : ''}

        if 'cal-event-home' in event_cls:
            game['loc'] = 'Home'

        # find all available event info
        for info in event.children:
            if type(info) is not element.Tag:
                continue
            clss = info.get('class')
            if not clss:
                continue

            # team name
            if 'cal-sport' in clss:
                game['team'] = info.text.strip()
            # opponent and/or location
            elif 'teams' in clss:
                comp = info.find('span', class_='va')
                if comp:
                    game['comp'] = unicode(comp.next_sibling).strip()
                else:
                    comp = info.find('div', class_='team-name')
                    if comp:
                            game['comp'] = comp.text.strip()
            elif 'cal-opponent' in clss:
                opp = info.find('span', class_='va')
                if opp:
                    game['opp'] = unicode(opp.next_sibling).strip()
                else:
                    opp = info.find('div', class_='team-name')
                    if opp:
                            game['opp'] = opp.text.strip()
                loc = info.find('div', class_='cal-neutral-site')
                if loc:
                    game['loc'] = loc.text.replace('@', '').strip()
            # time of game or status
            elif 'cal-status' in clss:
                game['stat'] = info.text.strip()
            # game result
            elif 'cal-result' in clss:
                game['res'] = info.text.strip()
            # links to more info
            elif 'cal-links' in clss:
                for child in info.find_all('a', title='$l.key'):
                    txt = child.text.strip().lower()
                    link = child.get('href')
                    if link[0] == '/':
                        link = 'http://www.gocrimson.com' + link
                    if txt in game:
                        game[txt] = link
    return game

def games_to_string(games):
    s = ''
    for game in games:
        s += '\n' + game['team'] + '\n'
        if game['comp']:
            s += game['comp'] + '\n'
            if game['loc']:
                s += '@ {}\n'.format(game['loc'])
        if game['opp']:
            s += 'VS ' + game['opp'] + '\n'
            if game['loc'] == 'Home':
                s += game['loc'] + '\n'
            elif game['loc']:
                s += '@ {}\n'.format(game['loc'])
            else:
                s += 'Away\n'
        if game['stat']:
            s += game['stat']
            if game['res']:
                s += ', {}\n'.format(game['res'])
            else:
                s += '\n'
    return s

def makeSpecial():
    s = 'Send "sports <month>/<day>/<year>" to get information about that date\'s varsity sport events.\n'
    return s
    
############################
##       Top-Level        ##
############################

## return list of valid team names
special = makeSpecial()

def eval(inp):
    return 'Varsity Sport Events on ' + inp + '\n' + games_to_string(getGames(inp))
