from flask import Blueprint, jsonify, request
from ReadWriteOps import *

productsBP = Blueprint("products", __name__)

fileName = "ClientProduct API\\JSON\\Product.json"

@productsBP.get("/")
def getProducts():
    products = readFile(fileName)
    return jsonify(products)

@productsBP.get("/<int:id>")
def getSpecificProduct(id):
    for product in readFile(fileName):
        if product["id"] == id:
            return product, 200
    return {"error": "The following product wasn't found!"}, 404

def findNextId():
    return max(product["id"] for product in readFile(fileName)) + 1

@productsBP.post("/")
def postProduct():
    if request.is_json:
        product = request.get_json()
        product["id"] = findNextId()
        readFile(fileName).append(product)
        writeFile(readFile(fileName))
        return product, 201
    return {"error": "Request must be a JSON file!"}, 415

@productsBP.put("/<int:id>")
def putProduct(id):
    if request.is_json:
        newProduct = request.get_json()
        for product in file:
            if product["id"] == id:
                for attribute in newProduct:
                    product[attribute] = newProduct[attribute]
                    writeFile(readFile(fileName), fileName)
                return product, 200
    return {"error": "Request must be a JSON file!"}

@productsBP.put("/<int:id>")
@productsBP.patch("/<int:id>")
def patchProduct(id):
    if request.is_json:
        newProduct = request.get_json()
        for product in readFile(fileName):
            if product["id"] == id:
                for attribute in newProduct:
                    product[attribute] = newProduct[attribute]
                    writeFile(readFile(fileName), fileName)
                return product, 200
    return {"error": "Request must be a JSON file!"}

@productsBP.delete("/<int:id>")
def deleteProduct(id):
    for product in readFile(fileName):
        if product["id"] == id:
            readFile(fileName).remove(product)
            writeFile(readFile(fileName), fileName)
            return {}, 200
    return {"error": "The following country was not found!"}, 404