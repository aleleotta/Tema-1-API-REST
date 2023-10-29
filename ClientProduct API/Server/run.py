from flask import *
import json

app = Flask(__name__)

fileName1 = "JSON//Client.json"
fileName2 = "JSON//Product.json"

def readFile1(fileName1):
    file = open(fileName1, "r")
    clients = json.load(file)
    file.close()
    return clients

def readFile2(fileName2):
    file = open(fileName2, "r")
    products = json.load(file)
    file.close()
    return products

def writeFile1(clients):
    file = open(fileName1, "w")
    json.dump(clients, file)
    file.close()

def writeFile2(products):
    file = open(fileName2, "w")
    json.dump(products, file)
    file.close()

@app.route("/")
def index():
    return "<h1><b>Welcome!</b></h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)