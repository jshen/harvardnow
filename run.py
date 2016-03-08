
from flask import Flask, request, redirect
import twilio.twiml
import LaundryScrape
import shuttle

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def response():
    resp = twilio.twiml.Response()
    incoming = request.values.get('Body',None)
    body = ""

    words = set(incoming.lower().split(" "))


    if ("demo" in words):
        body = '''Thanks for using Harvard Now!
        You can get laundry information by sending the name of your dorm follwed by either washer or dryer
        e.g. Weld washer'''
        resp.message(body)
        return str(resp)    

    mtype = "washer"
    if ("dryer" in words or "dryers" in words) and ("washer" not in words and "washers" not in words):
        mtype = "dryer"

    lost = False
    found = False
    for word in words:
        print word
        machines = LaundryScrape.getMachines(word,mtype)
        print machines
        if type(machines) is str:
            message = machines.split('|')
            messagetype = message.pop(0)
            if messagetype == "MULTIPLE" and not found:
                lost = True
                body+= "There are multiple laundry rooms in "+message.pop(0)
                body+= "\nTry one of these: \n"
                for room in message:
                    body+= room+"\n"
        else:
            if not found:
                body = ""
                found = True
            body+= word.upper()+" "+mtype.upper()+"S:\n"
            body+=LaundryScrape.machines_to_string(machines)
            
    if not (lost or found):
        if "laundry" in incoming.lower():
            body = LaundryScrape.room_names()

    stop_names = []
    for stop in shuttle.stops:
        stop_names.append(stop['name'])

    stops = [s for s in words if s in stop_names]

    if not stops == []:
        for stop in stops:
            arrivals = shuttle.arrivalsAtStopName(stop)
            for arrival in arrivals:
                body += "Route: " + arrival['route'] + " ETA: " + arrival['time_left']

    resp.message(body)
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)

