from datetime import datetime, timedelta
import api

#############################
##          Setup          ##
#############################

## stop: {name: <name>, stop_id: <stop_id>, routes: [<route_id0>,<route_id1>,...]}
## route: {name: <name>, route_id: <route_id0>, stops: [<stop_id0>,<stop_id1>,...]}
stops, routes = [], []
def setupStops():
    for stop in api.get('stops')['data']:
        stops.append({
            "name"    : stop['name'],
            "stop_id" : stop['stop_id'],
            "routes"  : stop['routes']
        })

def setupRoutes():
    for route in api.get('routes')['data'][api.AGENCY]:
        routes.append({
            "name"    : route['long_name'],
            "route_id" : route['route_id'],
            "stops"  : route['stops']
        })

def setup():
    setupStops()
    setupRoutes()

setup()

##############################
##    Shuttle Functions     ##
##############################    

def routeIDToName(routeID):
    return [r for r in routes if r['route_id'] == routeID][0]['name']

def stopNameToID(stopName):
    return [r for r in stops if r['name'] == stopName][0]['stop_id']

def stopIDToName(stopID):
    return [s for s in stops if s['stop_id'] == stopID][0]['name']

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
    data = api.get('arrival-estimates',params={'stops':stopID})['data']
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
        
def arrivalsAtStopName(stopName):
    return arrivalsAtStopID(stopNameToID(stopName))

def arrivalsStopToString(arrs):
    if arrs == []:
        return "No shuttles running at this stop."
    return '\n'.join([arr['route']+': '+arr['time_left'] for arr in arrs])
    
def arrivalsAtRouteId(routeID):
    data = api.get('arrival-estimates',params={'routes':routeID})['data']
    if len(data) < 1:
        return []
    arrivals = []
    for estarr in data:
        arr = estarr['arrivals'][0]
        arrivals.append({
            'stop': stopIDToName(estarr['stop_id']),
            'time_left': time_left(arr['arrival_at'])
        })
    return arrivals

def arrivalsRouteToString(arrs):
    if arrs == []:
        return "This route is currently inactive."
    return '\n'.join([arr['stop']+': '+arr['time_left'] for arr in arrs])
    
def makeSpecial():
    s = "Shuttle Stops: \n"
    s+= '\n'.join([stop['name'] for stop in stops])
    s += "\nShuttle Routes: \n"
    s += '\n'.join([route['name'] for route in routes])
    return s

#############################
##        Top-Level        ##
#############################

## list of valid shuttles
special = makeSpecial()

def eval(cmd):
    if cmd['endpoint'] == 'stop':
        ## arriving routes at this stop
        return cmd['label']+'\n'+arrivalsStopToString(arrivalsAtStopID(cmd['stopid']))
    elif cmd['endpoint'] == 'route':
        ## the route's stops 
        return cmd['label']+'\n'+arrivalsRouteToString(arrivalsAtRouteId(cmd['routeid']))
