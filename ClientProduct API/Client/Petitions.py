import requests
import json

url = "http://localhost:5050/"
clientsFile = "ClientProduct API\\JSON\\Client.json"
productsFile = "ClientProduct API\\JSON\\Product.json"

def GET():
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json)
    else:
        print("The JSON file couldn't be read or found.")

def GET1():
    type = 0
    while type != 1 or type != 2:
        try:
            type = int(input("Would you like to search for a client or a product? 1) Client 2) Product"))
        except:
            print("You must introduce an integer!")
    id = 0
    if type == 1:
        while id <= 0:
            try:
                id = int(input("Introduce the ID of the client: "))
                url = url + "clients/" + str(id)
            except:
                print("You must introduce an integer!")
    elif type == 2:
        while id <= 0:
            try:
                id = int(input("Introduce the ID of the product: "))
                url = url + "products/" + str(id)
            except:
                print("You must introduce an integer!")
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json)
    else:
        print("The JSON file couldn't be read or found.")

def POST():
    type = 0
    while type != 1 or type != 2:
        try:
            type = int(input("Would you like to introduce a client or a product? 1) Client 2) Product"))
        except:
            print("You must introduce an integer!")
    if type == 1:
        url = url + "clients/"
        dni = input("Introduce DNI: ")
        name = input("Intoroduce name: ")
        lastName = input("Introduce last name: ")
        phoneNumber = int(input("Introduce phone number: "))
        email = input("Introduce email: ")
        clients = json.loads(clientsFile)
        found = False
        i = 0
        for client in clients:
            if client["dni"] == dni:
                found = True
                i = i + 1
        if found == False:
            client = {'id': i, 'dni': dni, 'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'email': email}
        else:
            print("The product already exixts within the JSON file.")
    elif type == 2:
        url = url + "products/"
        name = input("Introduce name: ")
        description = input("Introduce description: ")
        price = float(input("Introduce price: "))
        clientID = int(input("Introduce client ID: "))
        products = json.loads(productsFile)
        found = False
        i = 0
        for product in products:
            if products["name"] == name:
                found = True
                i = i + 1
        if found == False:
            product = {'id': i, 'name': name, 'description': description, 'price': price, 'clientID': clientID}
        else:
            print("The product already exixts within the JSON file.")


def PUT():
    pass

def PATCH():
    pass

def DELETE():
    pass