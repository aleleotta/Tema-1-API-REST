from flask import *

fileName = "ClientProduct API\\JSON\\Product.json"
productsBP = Blueprint("products", __name__)

def readFile():
    file = open(fileName, "r")
    products = json.load(file)
    file.close()
    return products

file = readFile()

def writeFile(products):
    file = open(fileName, "w")
    json.dump(products, file)
    file.close()

@productsBP.get("/products")
def getProducts():
    return jsonify(fileName)

@productsBP.get("/products/<int:id>")
def getSpecificProduct(id):
    for product in fileName:
        if product["id"] == id:
            return product, 200
    return {"error": "The following product wasn't found!"}, 404

def findNextId():
    return max(product["id"] for product in fileName) + 1

@productsBP.post("/products")
def postProduct():
    if request.is_json:
        product = request.get_json()
        product["id"] = findNextId()
        fileName.append(product)
        writeFile2(fileName)
        return product, 201
    return {"error": "Request must be a JSON file!"}, 415

@productsBP.put("/products/<int:id>")
def putProduct(id):
    if request.is_json:
        newProduct = request.get_json()
        for product in fileName:
            if product["id"] == id:
                for attribute in newProduct:
                    product[attribute] = newProduct[attribute]
                    writeFile2(fileName)
                return product, 200
    return {"error": "Request must be a JSON file!"}

@productsBP.put("/products/<int:id>")
@productsBP.patch("/products/<int:id>")
def patchProduct(id):
    if request.is_json:
        newProduct = request.get_json()
        for product in fileName:
            if product["id"] == id:
                for attribute in newProduct:
                    product[attribute] = newProduct[attribute]
                    writeFile2(fileName)
                return product, 200
    return {"error": "Request must be a JSON file!"}

@productsBP.delete("/products/<int:id>")
def deleteProduct(id):
    for product in fileName:
        if product["id"] == id:
            fileName.remove(product)
            writeFile2(fileName)
            return {}, 200
    return {"error": "The following country was not found!"}, 404