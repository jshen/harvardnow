import run, LaundryScrape, shuttle

f = open('output.txt', 'w')
option = 2
if (option == 1):

	for room, roomid in LaundryScrape.rooms.iteritems():
		lst = room.split(" ")
		lst.extend(["LAUNDRY", "WASHERS", "WASHER"])
		s1 = str(lst)
		f.write("{'service': 'L', 'roomid':'" + roomid +"', 'machinetype':'washer', 'label': '" + room + " Washers', 'tags': " + s1 +"},\n")
		lst = room.split(" ")
		lst.extend(["LAUNDRY", "DRYER", "DRYERS"])
		s2 = str(lst)
		f.write("{'service': 'L', 'roomid':'" + roomid +"', 'machinetype':'dryer', 'label': '" + room + " Dryers', 'tags': " + s1 +"},\n")
elif (option == 2):
	
	for stop in shuttle.stops:
		lst = stop['name'].upper().split(" ")
		lst.extend(["SHUTTLE", "STOP"])
		f.write("{'service': 'S-S', 'stopid': '" + stop['stop_id'] + "' , 'label': '"+ stop['name'] +" Shuttle Stop', 'tags':"+ str(lst) +"},\n")

