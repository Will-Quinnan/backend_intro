from flask import Flask, abort
from data import me, mock_catalog

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





@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)



@app.get("/api/catalog/count")
def get_count():
    count = len(mock_catalog)
    return json.dumps(count)



@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results = []
    for prod in mock_catalog:
        if prod["category"] == cat:
            results.append(prod)


    return json.dumps(results)        



@app.get("/api/product/<id>")
def prods_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod) 
        
        
    return abort(404, "Invalid id")



@app.get("/api/product/search/<text>")
def search_prods(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)


    return json.dumps(results)    


@app.get("/api/categories")
def get_categories():
    results = []
    for prod in mock_catalog:
        cat = prod["category"]
        if not cat in results:
            results.append(cat)


    return json.dumps(results)   






@app.get("/api/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]
    return json.dumps(total)






@app.get("/api/cheaper/<price>")
def get_cheaper(price):
    price = float(price)
    results = []
    for prod in mock_catalog:
        if prod["price"] <= price:
            results.append(prod)

    return json.dumps(results)


app.run(debug=True)