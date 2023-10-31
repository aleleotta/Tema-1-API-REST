from flask import *
from run import writeFile1

fileName = "ClientProduct API\\JSON\\Client.json"
clientsBP = Blueprint("clients", __name__)

@clientsBP.get("/clients")
def getClients():
    return jsonify(fileName)

@clientsBP.get("/clients/<int:id>")
def getSpecificClient(id):
    for client in fileName:
        if client["id"] == id:
            return client, 200
    return {"error": "The following client wasn't found!"}, 404

def findNextId1():
    return max(client["id"] for client in fileName) + 1

@clientsBP.post("/clients")
def postClient():
    if request.is_json:
        client = request.get_json()
        client["id"] = findNextId1()
        fileName.append(client)
        writeFile1(fileName)
        return client, 201
    return {"error": "Request must be a JSON file!"}, 415

@clientsBP.put("/clients/<int:id>")
def putClient(id):
    if request.is_json:
        newClient = request.get_json()
        for client in fileName:
            if client["id"] == id:
                for attribute in newClient:
                    client[attribute] = newClient[attribute]
                    writeFile1(fileName)
                return client, 200
    return {"error": "Request must be a JSON file!"}

@clientsBP.put("/clients/<int:id>")
@clientsBP.patch("/clients/<int:id>")
def patchClient(id):
    if request.is_json:
        newClient = request.get_json()
        for client in fileName:
            if client["id"] == id:
                for attribute in newClient:
                    client[attribute] = newClient[attribute]
                    writeFile1(fileName)
                return client, 200
    return {"error": "Request must be a JSON file!"}

@clientsBP.delete("/clients/<int:id>")
def deleteClient(id):
    for client in fileName:
        if client["id"] == id:
            fileName.remove(client)
            writeFile1(fileName)
            return {}, 200
    return {"error": "The following country was not found!"}, 404