from flask import Flask, abort, request
from data import me, mock_catalog
from config import db
from bson import ObjectId

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



def fix_id(obj):
    obj["_id"] = str(obj["_id"])


@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)


@app.post("/api/catalog")
def save_product():
    data = request.get_json()
    db.products.insert_one(data)
    fix_id(data)
    return json.dumps(data)


@app.get("/api/catalog/count")
def get_count():
    total = db.products.count_documents({})
    return json.dumps(total)



@app.get("/api/category/<cat>")
def prods_by_category(cat):
    cursor = db.products.find({"category" : cat})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)


    return json.dumps(results)



@app.get("/api/product/<id>")
def prods_by_id(id):
    _id=ObjectId(id)    
    prod = db.products.find_one({"_id" : _id})
    if prod is None:
        return abort(404, "Invalid id")

    fix_id(prod)
    return json.dumps(prod)
        
    



@app.get("/api/product/search/<text>")
def search_prods(text):
    cursor = db.products.find({"title" : {"$regex" : text, "$options": "i" }})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)

    return json.dumps(results)    


@app.get("/api/categories")
def get_categories():
    cursor = db.products.distinct("category")

    return json.dumps(list(cursor))   






@app.get("/api/total")
def get_total():
    total = 0
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)
    for prod in results:
        total += prod["price"]
    return json.dumps(total)






@app.get("/api/cheaper/<price>")
def get_cheaper(price):
    price = float(price)
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_id(prod)
        results.append(prod)
    for prod in results:
        if prod["price"] <= price:
            results.append(prod)

    return json.dumps(results)


# challenge# find and return the cheapest 
# product# create a cheapest = mock_catalog[0]
# # for loop to travel the list# get every prod from the list
# # if the price of prod is lower than the price of cheapest
# # then update cheapest to be the prod (cheapest = prod)


app.run(debug=True)