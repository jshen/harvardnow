
from flask import Flask, request, redirect
import twilio.twiml
import LaundryScrape

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def response():
    resp = twilio.twiml.Response()
    incoming = request.values.get('Body',None)
    body = ""

    if "laundry" in incoming :
        body = `LaundryScrape.getMachines("WELD HALL", "washer")`
    else :
        body = incoming

    resp.message(body)
    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)

