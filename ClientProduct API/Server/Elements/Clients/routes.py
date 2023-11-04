from flask import Blueprint, jsonify, json, request
from ReadWriteOps import *

clientsBP = Blueprint("clients", __name__)

fileName = "ClientProduct API\\JSON\\Client.json"

@clientsBP.get("/")
def getClients():
    clients = readFile(fileName)
    return jsonify(clients)

@clientsBP.get("/<int:id>")
def getSpecificClient(id):
    for client in readFile(fileName):
        if client["id"] == id:
            return client, 200
    return {"error": "The following client wasn't found!"}, 404

def findNextId():
    return max(client["id"] for client in readFile(fileName)) + 1

@clientsBP.post("/")
def postClient():
    if request.is_json:
        client = request.get_json()
        client["id"] = findNextId()
        readFile(fileName).append(client)
        writeFile(readFile(fileName), fileName)
        return client, 201
    return {"error": "Request must be a JSON file!"}, 415

@clientsBP.put("/<int:id>")
def putClient(id):
    if request.is_json:
        newClient = request.get_json()
        for client in readFile(fileName):
            if client["id"] == id:
                for attribute in newClient:
                    client[attribute] = newClient[attribute]
                    writeFile(readFile(fileName), fileName)
                return client, 200
    return {"error": "Request must be a JSON file!"}

@clientsBP.put("/<int:id>")
@clientsBP.patch("/<int:id>")
def patchClient(id):
    if request.is_json:
        newClient = request.get_json()
        for client in readFile(fileName):
            if client["id"] == id:
                for attribute in newClient:
                    client[attribute] = newClient[attribute]
                    writeFile(readFile(fileName), fileName)
                return client, 200
    return {"error": "Request must be a JSON file!"}

@clientsBP.delete("/<int:id>")
def deleteClient(id):
    for client in readFile(fileName):
        if client["id"] == id:
            readFile(fileName).remove(client)
            writeFile(readFile(fileName), fileName)
            return {}, 200
    return {"error": "The following country was not found!"}, 404