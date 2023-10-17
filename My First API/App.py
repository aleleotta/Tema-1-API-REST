from flask import *

app = Flask(__name__)

fileName = "My First API\\Countries.json"

def readFile():
    file = open(fileName, "r")
    countries = json.load(file)
    file.close()
    return countries

file = readFile()

def writeFile(countries):
    file = open(fileName, "w")
    json.dump(countries, file)
    file.close()

@app.route("/")
def index():
    return "<h1><i>Hello everyone! :D</i></h1><br><br><br><h3><b>Feel free to do whatever you want on this page.</b></h3>"

@app.get("/countries")
def getCountries():
    return jsonify(file)

@app.get("/countries/<int:id>")
def getCountry(id):
    for country in file:
        if country["id"] == id:
            return country, 200
    return {"error": "The following country was not found!"}, 404

def findNextId():
    return max(country["id"] for country in readFile()) + 1

@app.post("/countries")
def addCountry():
    if request.is_json:
        country = request.get_json()
        country["id"] = findNextId()
        file.append(country)
        writeFile(file)
        return country, 201
    return {"error": "Request must be a JSON file!"}, 415

@app.put("/countries/<int:id>")
def modifyCountry(id):
    if request.is_json:
        newCountry = request.get_json()
        for country in file:
            if country["id"] == id:
                for attribute in newCountry:
                    country[attribute] = newCountry[attribute]
                    writeFile(file)
                return country, 200
    return {"error": "Request must be a JSON file!"}

@app.put("/countries/<int:id>")
@app.patch("/countries/<int:id>")
def modifyCountryAtt(id):
    if request.is_json:
        newCountry = request.get_json()
        for country in file:
            if country["id"] == id:
                for attribute in newCountry:
                    country[attribute] = newCountry[attribute]
                    writeFile(file)
                return country, 200
    return {"error": "Request must be a JSON file!"}

@app.delete("/countries/<int:id>")
def deleteCountry(id):
    for country in countries:
        if country["id"] == id:
            countries.remove(country)
            return {}, 200
    return {"error": "The following country was not found!"}, 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)