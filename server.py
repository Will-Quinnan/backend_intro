from flask import Flask
from data import me

import json

app = Flask(__name__) #similar to new task in JS


@app.get("/")
def home():
    return "Hello Wolrd"


@app.get("/about")
def about():
    return "Will Quinnan"


@app.get("/contact/me")
def contact_me():
    return "wmplqnjr@gmail.com"



############################################
############### API -> JSON ################
############################################



@app.get("/api/developer")
def developer():
    return json.dumps(me) #parse into json string


@app.get("/api/developer/address")
def address():
    address = me["address"]
    # return address["street"] + " #" + str(address["number"]) + ", " + address["city"] + ", " + address["zipcode"]
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'


app.run(debug=True)