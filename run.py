
from flask import Flask, request, redirect
import twilio.twiml
import LaundryScrape

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def response():
    resp = twilio.twiml.Response()
    incoming = request.values.get('Body',None)
    body = ""

    words = incoming.lower().split(" ")
    for word in words:
        print word
        mtype = "washer"
        if ("dryer" in words or "dryers" in words) and ("washer" not in words and "washers" not in words):
            mtype = "dryer"
        machines = LaundryScrape.getMachines(word,mtype)
        print machines
        if machines != "Invalid room name":
            body = mtype.upper()+"S:\n"
            body+=LaundryScrape.machines_to_string(machines)
            resp.message(body)
            return str(resp)
    

    if "laundry" in incoming.lower() :
        body = LaundryScrape.room_names()
    else :
        body = incoming

    resp.message(body)
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)

