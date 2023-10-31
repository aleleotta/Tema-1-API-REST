from flask import *
from app.clients.routes import clientsBP
from app.products.routes import productsBP

app = Flask(__name__)

app.register_blueprint(clientsBP, url_prefix="/clients")
app.register_blueprint(productsBP, url_prefix="/clients")

fileName1 = "ClientProduct API\\JSON\\Client.json"
fileName2 = "ClientProduct API\\JSON\\Product.json"

def readFile1():
    file = open(fileName1, "r")
    clients = json.load(file)
    file.close()
    return clients

def readFile2():
    file = open(fileName2, "r")
    products = json.load(file)
    file.close()
    return products

@app.route("/")
def index():
    return "<h1 style=\"font-family: 'Arial', 'Verdana', sans-serif;\">Welcome!</h1>"

@app.get("/clients")
def getClients():
    return jsonify(file1)

@app.get("/products")
def getProducts():
    return jsonify(file2)

@app.get("/clients/<int:id>")
def getSpecificClient(id):
    for client in file1:
        if client["id"] == id:
            return client, 200
    return {"error": "The following client wasn't found!"}, 404

@app.get("/products/<int:id>")
def getSpecificProduct(id):
    for product in file2:
        if product["id"] == id:
            return product, 200
    return {"error": "The following product wasn't found!"}, 404

def findNextId1():
    return max(client["id"] for client in file1) + 1

def findNextId2():
    return max(product["id"] for product in file2) + 1

@app.post("/clients")
def postClient():
    if request.is_json:
        client = request.get_json()
        client["id"] = findNextId1()
        file1.append(client)
        writeFile1(file1)
        return client, 201
    return {"error": "Request must be a JSON file!"}, 415

@app.post("/products")
def postProduct():
    if request.is_json:
        product = request.get_json()
        product["id"] = findNextId2()
        file2.append(product)
        writeFile2(file2)
        return product, 201
    return {"error": "Request must be a JSON file!"}, 415

@app.put("/clients/<int:id>")
def putClient(id):
    if request.is_json:
        newClient = request.get_json()
        for client in file1:
            if client["id"] == id:
                for attribute in newClient:
                    client[attribute] = newClient[attribute]
                    writeFile1(file1)
                return client, 200
    return {"error": "Request must be a JSON file!"}

@app.put("/products/<int:id>")
def putProduct(id):
    if request.is_json:
        newProduct = request.get_json()
        for product in file2:
            if product["id"] == id:
                for attribute in newProduct:
                    product[attribute] = newProduct[attribute]
                    writeFile1(file1)
                return product, 200
    return {"error": "Request must be a JSON file!"}

@app.put("/clients/<int:id>")
@app.patch("/clients/<int:id>")
def patchClient(id):
    if request.is_json:
        newClient = request.get_json()
        for client in file1:
            if client["id"] == id:
                for attribute in newClient:
                    client[attribute] = newClient[attribute]
                    writeFile1(file1)
                return client, 200
    return {"error": "Request must be a JSON file!"}

@app.put("/products/<int:id>")
@app.patch("/products/<int:id>")
def patchProduct(id):
    if request.is_json:
        newProduct = request.get_json()
        for product in file2:
            if product["id"] == id:
                for attribute in newProduct:
                    product[attribute] = newProduct[attribute]
                    writeFile1(file1)
                return product, 200
    return {"error": "Request must be a JSON file!"}

@app.delete("/clients/<int:id>")
def deleteClient(id):
    for client in file1:
        if client["id"] == id:
            file1.remove(client)
            writeFile1(file1)
            return {}, 200
    return {"error": "The following country was not found!"}, 404

@app.delete("/products/<int:id>")
def deleteProduct(id):
    for product in file2:
        if product["id"] == id:
            file2.remove(product)
            writeFile2(file2)
            return {}, 200
    return {"error": "The following country was not found!"}, 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)