import requests, threading
from datetime import datetime, timedelta

AGENCY = "52"
KEY = 'op8wGpiS5Emsh5KZtdo1Mn5hHWNpp1hVi8FjsnUgr0kn5fejO8'
HEADERS = {
    'X-Mashape-Key': KEY,
    'Accept': 'Accept: application/json'
}

##########################
##   Helper Functions   ##
##########################

def get(endpt,agency=AGENCY,key=KEY,headers=HEADERS,params={}):
    params['agencies'] = agency
    page = "https://transloc-api-1-2.p.mashape.com/%s.json"%endpt
    return requests.get(page,headers=headers,params=params).json()

## stop: {name: <name>, stop_id: <stop_id>, routes: [<route_id0>,<route_id1>,...]}
## route: {name: <name>, route_id: <route_id0>, stops: [<stop_id0>,<stop_id1>,...]}
stops = [] 
routes = []

def setupStops():
    for stop in get('stops')['data']:
        stops.append({
            "name"    : stop['name'],
            "stop_id" : stop['stop_id'],
            "routes"  : stop['routes']
        })
def setupRoutes():
    for route in get('routes')['data'][AGENCY]:
        routes.append({
            "name"    : route['long_name'],
            "route_id" : route['route_id'],
            "stops"  : route['stops']
        })
def setup():
    setupStops()
    setupRoutes()
setup()

def routeIDToName(routeID):
    return [r for r in routes if r['route_id'] == routeID][0]['name']

def stopNameToID(stopName):
    return [r for r in stops if r['name'] == stopName][0]['stop_id']

## ignores time zone
def stringToTime(s):
    fmt = '%Y-%m-%dT%H%M%S'
    return datetime.strptime(s.replace(':','')[:-5],fmt)
def deltaToString(d):
    s = ''
    if d.days>1: s+= '%d days, '%(d.days)
    sec = d.seconds
    if sec >= 3600:
        s+= '%d hours, '%(sec/3600)
        sec = sec%3600
    if sec >= 60:
        s+= '%d minutes, '%(sec/60)
        sec = sec%60
    s+= '%d seconds, '%sec
    return s[:-2]    
def time_left(arrivalstr):
    delta = stringToTime(arrivalstr) - datetime.now()
    return deltaToString(delta)
        
def arrivalsAtStopID(stopID):
    data = get('arrival-estimates',params={'stops':stopID})['data']
    if len(data) < 1:
        return []
    else:
        data = data[0]['arrivals']
    arrivals = []
    for arrival in data:
        arrivals.append({
            'route': routeIDToName(arrival['route_id']),
            'time_left':time_left(arrival['arrival_at'])
        })
    return arrivals

#############################
##   Top-level Functions   ##
#############################
    
def arrivalsAtStopName(stopName):
    return arrivalsAtStopID(stopNameToID(stopName))
