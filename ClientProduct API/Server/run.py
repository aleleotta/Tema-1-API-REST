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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)