from datetime import datetime, timedelta
import api

stops, routes = [], []
special = "test demo"

def init():
	for route in api.get('routes')['data'][api.AGENCY]:
		#print(route['long_name'])
		routes.append({
	        "name"    : route['long_name'],
	        "route_id" : route['route_id'],
	        "stops"  : route['stops']
	    })
	for stop in api.get('stops')['data']:
		stops.append({
	        "name"    : stop['name'],
	        "stop_id" : stop['stop_id'],
	        "routes"  : stop['routes']
	    })

def stringToTime(s):
    fmt = '%Y-%m-%dT%H%M%S'
    return datetime.strptime(s.replace(':','')[:-5],fmt)

def findRoutesWithStop(stop):
	foundRoutes = []
	for route in routes:
		if stop in route["stops"]:
			foundRoutes.append(route)
	return foundRoutes

def nameToID(name):
	id = 0
	lower = name.lower()
	if (lower.find("quad") != -1 or lower.find("cabot") != -1 or lower.find("phoho") != -1 or lower.find("pforzheimer") != -1 or lower.find("currier") != -1 or lower.find("soch") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Quad").next()
	elif (lower.find("mass") != -1 or lower.find("ave") != -1 or lower.find("and garden") != -1 or lower.find("& garden") != -1) :
		id = (item["stop_id"] for item in stops if item["name"] == "Mass Ave & Garden St").next()
	elif (lower.find("memorial") != -1 or lower.find("hall") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Memorial Hall").next()
	elif (lower.find("lamont") != -1 and lower.find("gate") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Lamont Library Gate").next()
	elif (lower.find("lamont") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Lamont Library").next()
	elif (lower.find("widener") != -1 or lower.find("gate") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Widener Gate").next()
	elif (lower.find("inn") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Inn at Harvard").next()
	elif (lower.find("winthrop") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Winthrop House").next()
	elif (lower.find("mather") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Mather House").next()
	elif (lower.find("maxwell") != -1 or lower.find("dworkin") != -1 or lower.find("md") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Maxwell Dworkin").next()
	elif (lower.find("square") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Harvard Square").next()
	elif (lower.find("stadium") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Stadium").next()
	elif (lower.find("hbs") != -1 or lower.find ("business") != -1 or lower.find("innovation") != -1 or lower.find("lab") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "HiLab-HBS").next()
	elif (lower.find("soldier") != -1 or lower.find("field") != -1 or lower.find("park") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Soldiers Field Park").next()
	else:
		id = 0

	return id






init()
beginning = "widener"
end = "cabot"

beginningStop = (item for item in stops if item["stop_id"] == nameToID(beginning)).next()
endStop = (item for item in stops if item["stop_id"] == nameToID(end)).next()

routesWithBeginning = findRoutesWithStop(nameToID(beginning))
routesWithEnd = findRoutesWithStop(nameToID(end))
validRoutes = []
for startRoute in routesWithBeginning:
	for endRoute in routesWithEnd:
		if startRoute["name"] == endRoute["name"]:
			validRoutes.append(startRoute)

routeArrivals = []

for route in validRoutes:
	data = api.get('arrival-estimates',params={'routes':route["route_id"]})['data']
	for estarr in data:
		for arr in estarr['arrivals']:
			routeArrivals.append({
				'route': route["name"],
				'stop': (stop["name"] for stop in stops if stop["stop_id"] == estarr['stop_id']).next(),
				'time': stringToTime(arr['arrival_at']),
				'vehicle_id': arr['vehicle_id']
			})

vehicle_id = 0;
departureTime = datetime.max

print ("all arrivals")

arrivalTime = datetime.max

for departure in routeArrivals:
	print (departure)
	if departure["time"] < departureTime and departure["stop"] == beginningStop["name"]:
		valid = 0
		for arrival in routeArrivals:
			if arrival["stop"] == endStop["name"] and arrival["time"] > departure["time"] and departure["vehicle_id"] == arrival["vehicle_id"]:
				valid = 1
				if arrival["time"] < arrivalTime:
					arrivalTime = arrival["time"]
		if valid == 1: 
			departureTime = departure["time"]
			vehicle_id = departure["vehicle_id"]

print("\n\nbest departure")
print("Vehicle ID: " + vehicle_id)
print("Departure Time: " + departureTime.strftime("%-I:%M%p"))
print("Arrival Time: " + arrivalTime.strftime("%-I:%M%p"))

"""
nameToID("")
nameToID("quad")
nameToID("phoho")
nameToID("ave")
nameToID("mass ave")
nameToID("soldier")
nameToID("square")
nameToID("winthrop")
nameToID("lamont")
nameToID("lamont gate")
nameToID("lamont library")
nameToID("Mass Ave & gaden st.")
nameToID("md")
nameToID("Maxwell dw")
"""




