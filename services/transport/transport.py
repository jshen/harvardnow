from datetime import datetime, timedelta
import api

stops, routes = [], []

def init():
	try:
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
		special = makeSpecial()
		return 0;
	except Exception, e:
		return 1;

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
	if (lower.find("quad") != -1 or lower.find("cabot") != -1 or lower.find("pfoho") != -1 or lower.find("pforzheimer") != -1 or lower.find("currier") != -1 or lower.find("soch") != -1):
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
		id = (item["stop_id"] for item in stops if item["name"] == "i-Lab (Temporary)").next()
	elif (lower.find("soldier") != -1 or lower.find("park") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Soldiers Field Park (Temporary)").next()
	elif (lower.find("peabody") != -1 or lower.find("terrace") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Peabody Terrace").next()
	elif (lower.find("barry") != -1 or lower.find("corner") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Barry's Corner").next()
	elif (lower.find("jordan") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Jordan Field").next()
	elif (lower.find("dewolf") != -1 or lower.find("mill") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "DeWolfe St. at Mill St. Area").next()
	elif (lower.find("mason") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Garden St. at Mason St.").next()
	elif (lower.find("175") != -1 or lower.find("north") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "175 North Harvard").next()
	elif (lower.find("law") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Law School").next()
	elif (lower.find("kennedy") != -1 or lower.find("government") != -1):
		id = (item["stop_id"] for item in stops if item["name"] == "Kennedy (Temporary Stop)").next();
	else:
		id = 0

	return id


def eval(input):
	if (init() == 1):
		return "Unable to reach server. Please try again later."

	try:
		beginning = input.split("to", 1)[0]
		end = input.split("to", 1)[1]
	except Exception, e:
		return "Invalid command - usage is \"transport \'stop\' to \'stop\'\""

	try:
		beginningStop = (item for item in stops if item["stop_id"] == nameToID(beginning)).next()
		endStop = (item for item in stops if item["stop_id"] == nameToID(end)).next()
	except Exception, e:
		t = ""
		t += "Location not recognized - usage is \"transport \'stop\' to \'stop\'\"\n"
		t += "Valid stops are:\n"
		for stop in stops:
			t += stop['name']
			t += "\n"
		return t

	if (beginningStop == endStop):
		return "Destination must be different than origin."

	if (beginningStop == 0 or endStop == 0):
		x = ""
		x += "Location not recognized - usage is \"transport \'stop\' to \'stop\'\"\n"
		x += "Valid stops are:\n"
		for stop in stops:
			x += stop['name']
		return x

	try:
		routesWithBeginning = findRoutesWithStop(nameToID(beginning))
		routesWithEnd = findRoutesWithStop(nameToID(end))
		validRoutes = []
		for startRoute in routesWithBeginning:
			for endRoute in routesWithEnd:
				if startRoute["name"] == endRoute["name"]:
					validRoutes.append(startRoute)

		if (validRoutes == []):
			return "No routes run between those locations at this time."

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

		if (routeArrivals == []):
			return "No routes run between those locations at this time."

		vehicle_id = 0;
		departureTime = datetime.max
		arrivalTime = datetime.max
		bestRoute = routeArrivals[0]

		#necessary to catch when the shuttle decides
		#to not stop at every location on its route
		routeFound = 0;

		for arrival in routeArrivals:
			if arrival["time"] < arrivalTime and arrival["stop"] == endStop["name"]:
				for departure in routeArrivals:
					if departure["stop"] == beginningStop["name"] and departure["time"] < arrival["time"] and departure["vehicle_id"] == arrival["vehicle_id"]:
						if departure["time"] < departureTime:
							routeFound = 1; 
							bestRoute = arrival;
							departureTime = departure["time"]
							arrivalTime = arrival["time"]
							vehicle_id = departure["vehicle_id"]

		if (routeFound == 0):
			return "No routes run between those locations at this time."

		departureTimeString = departureTime.strftime("%-I:%M%p")
		arrivalTimeString = arrivalTime.strftime("%-I:%M%p")

		returnString = "Take " + bestRoute["route"] + " departing " + beginningStop["name"] + " at " + departureTimeString + " arriving at " + endStop["name"] + " at " + arrivalTimeString
		return returnString
	except Exception, e:
		return "No routes run between those locations at this time."

def makeSpecial():
	s = "Usage is \"transport \'stop\' to \'stop\'\""
	for stop in stops:
		s += stop['name']
		s += "\n"
	return s

special = makeSpecial()