from flask import jsonify, json

def readFile(fileName):
    file = open(fileName, "r") # Reads current JSON file.
    clients = json.load(file) # Loads JSON file.
    file.close() #Closes the current JSON file.
    return clients #Returns JSON to variable for later use.

def writeFile(jsonVar, fileName):
    file = open(fileName, "w") # Creates new file.
    json.dump(jsonVar, file) # Overwrites file.
    file.close() #Closes the overwritten JSON file.