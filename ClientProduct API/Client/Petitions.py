import requests
import json

url = "http://localhost:5050/"
clientsFile = "ClientProduct API\\JSON\\Client.json"
productsFile = "ClientProduct API\\JSON\\Product.json"

def GET():
    response = requests.get(url).json()
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json)
    else:
        print("The JSON file couldn't be read or found.")

def GET1():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Would you like to search for a client or a product? 1) Client 2) Product"))
            if type != 1 and type != 2:
                print("Please introduce a valid option!")
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
    response = requests.get(url).json()
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json)
    else:
        print("The JSON file couldn't be read or found.")

def POST():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Would you like to introduce a client or a product? 1) Client 2) Product"))
            if type != 1 and type != 2:
                print("Please introduce a valid option!")
        except:
            print("You must introduce an integer!")
    if type == 1:
        url = url + "clients/"
        clients = requests.get(url).json()
        dni = input("Introduce DNI: ")
        name = input("Introduce name: ")
        lastName = input("Introduce last name: ")
        phoneNumber = int(input("Introduce phone number: "))
        email = input("Introduce email: ")
        found = False
        i = len(clients) + 1
        for client in clients:
            if client["dni"] == dni:
                found = True
                break
        if found == False:
            client = {'id': i, 'dni': dni, 'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'email': email}
            response = requests.post(url, json=client)
            print("Status code: ", response.status_code)
            if response.status_code == 201:
                print(response.json())
                print("The client has been posted.")
            else:
                print("The client was unable to get posted.")
        else:
            print("The product already exixts within the JSON file.")
    elif type == 2:
        url = url + "products/"
        products = requests.get(url).json()
        name = input("Introduce name: ")
        description = input("Introduce description: ")
        price = float(input("Introduce price: "))
        clientID = int(input("Introduce client ID: "))
        found = False
        i = len(products) + 1
        for product in products:
            if product["name"] == name:
                found = True
                break
        if found == False:
            product = {'id': i, 'name': name, 'description': description, 'price': price, 'clientID': clientID}
            response = requests.post(url, json=product)
            print("Status code: ", response.status_code)
            if response.status_code == 201:
                print(response.json())
                print("The product has been posted.")
            else:
                print("The product was unable to get posted.")
        else:
            print("The product already exixts within the JSON file.")

def PUT():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Would you like to update a client or a product? 1) Client 2) Product"))
            if type != 1 and type != 2:
                print("Please introduce a valid option!")
        except:
            print("You must introduce an integer!")
    if type == 1:
        baseUrl = url + "clients/"
        id = int(input("Which client would you like to update: "))
        url = url + str(id)
        clients = requests.get(baseUrl).json()
        found = False
        for client in clients:
            if client["id"] == id:
                found = True
                break
        name = input("Introduce name: ")
        lastName = input("Introduce last name: ")
        phoneNumber = int(input("Introduce phone number: "))
        email = input("Introduce email: ")
        client = {'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'email': email}
        response = requests.put(url, json=client)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
        else:
            print("The client couldn't get updated or was not found.")
    elif type == 2:
        baseUrl = url + "products/"
        id = int(input("Which product would you like to update: "))
        url = url + str(id)
        products = requests.get(baseUrl).json()
        found = False
        for product in products:
            if product["id"] == id:
                found = True
                break
        description = input("Introduce description: ")
        price = float(input("Introduce price: "))
        clientID = int(input("Introduce client ID: "))
        product = {'description': description, 'price': price, 'clientID': clientID}
        response = requests.put(url, json=product)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
        else:
            print("The product couldn't get updated or was not found.")

def PATCH():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Would you like to update a client or a product? 1) Client 2) Product"))
            if type != 1 and type != 2:
                print("Please introduce a valid option!")
        except:
            print("You must introduce an integer!")
    if type == 1:
        baseUrl = url + "clients/"
        id = int(input("Which client would you like to update: "))
        url = url + str(id)
        clients = requests.get(baseUrl).json()
        found = False
        for client in clients:
            if client["id"] == id:
                found = True
                break
        attribute = 0
        while attribute != 1 and attribute != 2 and attribute != 3 and attribute != 4:
            try:
                attribute = int(input("Which attribute would you like to update? 1) Name 2) Last name 3) Phone number 4) Email"))
                if attribute != 1 and attribute != 2 and attribute != 3 and attribute != 4:
                    print("Please introduce a valid option!")
            except:
                print("You must introduce an integer!")
        if attribute == 1:
            name = input("Introduce name: ")
            client = {'name': name}
        elif attribute == 2:
            lastName = input("Introduce last name: ")
            client = {'lastName': lastName}
        elif attribute == 3:
            phoneNumber = int(input("Introduce phone number: "))
            client = {'phoneNumber': phoneNumber}
        elif attribute == 4:
            email = input("Introduce email: ")
            client = {'email': email}
        response = requests.patch(url, json=client)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
        else:
            print("The client couldn't get updated or was not found.")
    elif type == 2:
        baseUrl = url + "products/"
        id = int(input("Which product would you like to update: "))
        url = url + str(id)
        products = requests.get(baseUrl).json()
        found = False
        for product in products:
            if product["id"] == id:
                found = True
                break
        while attribute != 1 and attribute != 2 and attribute != 3:
            try:
                attribute = int(input("Which attribute would you like to update? 1) Description 2) Price 3) Client ID"))
                if attribute != 1 and attribute != 2 and attribute != 3:
                    print("Please introduce a valid option!")
            except:
                print("You must introduce an integer!")
        if attribute == 1:
            description = input("Introduce description: ")
            product = {'description': description}
        elif attribute == 2:
            price = float(input("Introduce price: "))
            product = {'price': price}
        elif attribute == 3:
            clientID = int(input("Introduce client ID: "))
            product = {'clientID': clientID}
        response = requests.patch(url, json=product)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
        else:
            print("The product couldn't get updated or was not found.")

def DELETE():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Would you like to delete a client or a product? 1) Client 2) Product"))
            if type != 1 and type != 2:
                print("Please introduce a valid option!")
        except:
            print("You must introduce an integer!")
    if type == 1:
        url = url + "clients/"
        id = 0
        while id <= 0:
            try:
                id = int(input("Introduce the ID of the client you would like to delete: "))
                if id <= 0:
                    print("Please introduce a valid ID.")
            except:
                print("You must introduce an integer!")
        url = url + str(id)
        response = requests.delete(url)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print("The client was successfully deleted.")
        else:
            print("The client wasn't found.")
    elif type == 2:
        url = url + "products/"
        id = 0
        while id <= 0:
            try:
                id = int(input("Introduce the ID of the product you would like to delete: "))
                if id <= 0:
                    print("Please introduce a valid ID.")
            except:
                print("You must introduce an integer!")
        url = url + str(id)
        response = requests.delete(url)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print("The product was successfully deleted.")
        else:
            print("The product wasn't found.")