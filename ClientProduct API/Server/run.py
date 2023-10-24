from flask import *

app = Flask(__name__)

fileName1 = "JSON//Client.json"
fileName2 = "JSON//Product.json"

def readFile(fileName):
    pass

def writeFile(fileName):
    pass

@app.route("/")
def index():
    return "<h1><b>Welcome!</b></h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)