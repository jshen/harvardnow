from flask import Flask, request, redirect
import twilio.twiml
import LaundryScrape, shuttle

app = Flask(__name__)

box = [
    {'service': 'L', 'roomid':'136259', 'machinetype':'washer', 'label': 'Weld Washers', 'tags': ['WELD','LAUNDRY','WASHERS','WASHER']},
    {'service': 'L', 'roomid':'136259', 'machinetype':'dryer', 'label': 'Weld Dryer', 'tags': ['WELD','LAUNDRY','DRYERS','DRYER']},
    {'service': 'S-S', 'stopid':'4070614' , 'label': 'Quad Shuttle', 'tags':['QUAD','SHUTTLE']},
    {'service': 'S-R', 'routeid':'4007650' , 'label': 'Allston Campus Express', 'tags':['ALLSTON','SHUTTLE']}
]

def filter(tag,cmds=box):
    return [cmd for cmd in cmds if tag in cmd['tags']]

def eval(cmd):
    if cmd['service'] == 'L':
        return cmd['label']+'\n'+LaundryScrape.machines_to_string(LaundryScrape.getMachines(cmd['roomid'],cmd['machinetype']))
    elif cmd['service'] == 'S-S':
        return cmd['label']+'\n'+shuttle.arrivalsStopToString(shuttle.arrivalsAtStopID(cmd['stopid']))
    elif cmd['service'] == 'S-R':
        return cmd['label']+'\n'+shuttle.arrivalsRouteToString(shuttle.arrivalsAtRouteId(cmd['routeid']))
    
@app.route("/", methods=['GET', 'POST'])
def response():
    resp = twilio.twiml.Response()
    incoming = request.values.get('Body',None)
    body = ""

    words = set(incoming.upper().split(" "))
    print words
    started = False
    results = box
    for word in words:
        r = filter(word,results)
        if r == []:
            break
        else:
            started = True
            results = r
    if len(results)>5:
        body = "Sorry, that's too many requests."
    elif not started:
        body = "Sorry, I don't know what that is."
    else:
        body = "\n".join(['\n'+eval(cmd) for cmd in results])

    
    # mtype = "washer"
    # if ("dryer" in words or "dryers" in words) and ("washer" not in words and "washers" not in words):
    #     mtype = "dryer"

    # lost = False
    # found = False
    # for word in words:
    #     print word
    #     machines = LaundryScrape.getMachines(word,mtype)
    #     print machines
    #     if type(machines) is str:
    #         message = machines.split('|')
    #         messagetype = message.pop(0)
    #         if messagetype == "MULTIPLE" and not found:
    #             lost = True
    #             body+= "There are multiple laundry rooms in "+message.pop(0)
    #             body+= "\nTry one of these: \n"
    #             for room in message:
    #                 body+= room+"\n"
    #     else:
    #         if not found:
    #             body = ""
    #             found = True
    #         body+= word.upper()+" "+mtype.upper()+"S:\n"
    #         body+=LaundryScrape.machines_to_string(machines)
            
    # if not (lost or found):
    #     if "laundry" in incoming.lower():
    #         body = LaundryScrape.room_names()
    #     else :
    #         body = "Sorry, I don't know what that is."

    resp.message(body)
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)

