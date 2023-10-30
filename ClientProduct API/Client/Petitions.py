import requests

url = "http://localhost:5050/"
clientsFile = "ClientProduct API\\JSON\\Client.json"
productsFile = "ClientProduct API\\JSON\\Product.json"

def GET():
    global url
    url = "http://localhost:5050/clients"
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print("The JSON file couldn't be read or found.")
    url = "http://localhost:5050/products"
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json())
        url = "http://localhost:5050/"
    else:
        print("The JSON file couldn't be read or found.")
        url = "http://localhost:5050/"

def GET1():
    global url
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
                if id <= 0:
                    print("Please introduce an ID greater than 0.")
            except:
                print("You must introduce an integer!")
        url = url + "clients/" + str(id)
        response = requests.get(url)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json())
        else:
            print("The JSON file couldn't be read or found.")
    elif type == 2:
        while id <= 0:
            try:
                id = int(input("Introduce the ID of the product: "))
                if id <= 0:
                    print("Please introduce an ID greater than 0.")
            except:
                print("You must introduce an integer!")
        url = url + "products/" + str(id)
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json())
        url = "http://localhost:5050/"
    else:
        print("The JSON file couldn't be read or found.")
        url = "http://localhost:5050/"

def POST():
    global url
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
        clients = requests.get(url)
        dni = ""
        while len(dni) != 9:
            try:
                dni = input("Introduce DNI: ")
                if len(dni) != 9:
                    print("You must introduce the DNI with 9 digits.")
            except:
                print("Please introduce a valid DNI!")
        found = False
        i = 1
        for client in clients:
            i = i + 1
            if client["dni"] == dni:
                found = True
                break
        if found == False:
            name = 0
            while name == "":
                try:
                    name = input("Introduce name: ")
                    if name == "":
                        print("Please do not leave the name empty.")
                except:
                    print("Please introduce a valid name!")
            lastName = 0
            while lastName == "":
                try:
                    lastName = input("Introduce last name: ")
                    if lastName == "":
                        print("Please do not leave the last name empty.")
                except:
                    print("Please introduce a valid last name!")
            phoneNumber = 0
            while len(phoneNumber) != 10:
                try:
                    phoneNumber = int(input("Introduce phone number: "))
                    if len(phoneNumber) != 10:
                        print("Please introduce a phone number that has 10 digits.")
                except:
                    print("Please introduce a valid phone number!")
            email = ""
            while email == "":
                try:
                    email = input("Introduce email: ")
                    if email == "":
                        print("Please do not leave the email empty.")
                except:
                    print("Please introduce a valid email!")
            client = {'id': i, 'dni': dni, 'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'email': email}
            response = requests.post(url, json=client)
            print("Status code: ", response.status_code)
            if response.status_code == 201:
                print(response.json())
                print("The client has been posted.")
                url = "http://localhost:5050/"
            else:
                print("The client was unable to get posted.")
                url = "http://localhost:5050/"
        else:
            print("The product already exixts within the JSON file.")
            url = "http://localhost:5050/"
    elif type == 2:
        url = url + "products/"
        products = requests.get(url)
        name = input("Introduce name: ")
        description = input("Introduce description: ")
        price = float(input("Introduce price: "))
        clientID = int(input("Introduce client ID: "))
        found = False
        i = 1
        for product in products:
            i = i + 1
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
                url = "http://localhost:5050/"
            else:
                print("The product was unable to get posted.")
                url = "http://localhost:5050/"
        else:
            print("The product already exixts within the JSON file.")
            url = "http://localhost:5050/"

def PUT():
    global url
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
        while id <= 0:
            try:
                id = int(input("Which client would you like to update: "))
                if id <= 0:
                    print("You must introduce an ID greater than 0.")
            except:
                print("You must introduce an integer!")
        url = url + str(id)
        clients = requests.get(baseUrl)
        found = False
        for client in clients:
            if client["id"] == id:
                found = True
                break
        name = 0
        while name == "":
            try:
                name = input("Introduce name: ")
                if name == "":
                    print("Please do not leave the name empty.")
            except:
                print("Please introduce a valid name!")
        lastName = 0
        while lastName == "":
            try:
                lastName = input("Introduce last name: ")
                if lastName == "":
                    print("Please do not leave the last name empty.")
            except:
                print("Please introduce a valid last name!")
        phoneNumber = 0
        while len(phoneNumber) != 10:
            try:
                phoneNumber = int(input("Introduce phone number: "))
                if len(phoneNumber) != 10:
                    print("Please introduce a phone number that has 10 digits.")
            except:
                print("Please introduce a valid phone number!")
        email = ""
        while email == "":
            try:
                email = input("Introduce email: ")
                if email == "":
                    print("Please do not leave the email empty.")
            except:
                print("Please introduce a valid email!")
        client = {'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'email': email}
        response = requests.put(url, json=client)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
            url = "http://localhost:5050/"
        else:
            print("The client couldn't get updated or was not found.")
            url = "http://localhost:5050/"
    elif type == 2:
        baseUrl = url + "products/"
        while id <= 0:
            try:
                id = int(input("Which product would you like to update: "))
                if id <= 0:
                    print("You must introduce an ID greater than 0.")
            except:
                print("You must introduce an integer!")
        url = url + str(id)
        products = requests.get(baseUrl)
        found = False
        for product in products:
            if product["id"] == id:
                found = True
                break
        description = ""
        while description == "":
            try:
                description = input("Introduce description: ")
                if description == "":
                    print("Please do not leave the description empty.")
            except:
                print("Please introduce a valid description!")
        price = 0
        while price <= 0: 
            try:
                price = float(input("Introduce price: "))
                if price <= 0:
                    print("Please introduce a price greater than 0.")
            except:
                print("Please introduce a valid price!")
        clientID = 0
        while clientID <= 0:
            try:
                clientID = int(input("Introduce client ID: "))
                if clientID <= 0:
                    print("Please introduce a client ID greater than 0.")
            except:
                print("Please introduce a valid client ID!")
        product = {'description': description, 'price': price, 'clientID': clientID}
        response = requests.put(url, json=product)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
            url = "http://localhost:5050/"
        else:
            print("The product couldn't get updated or was not found.")
            url = "http://localhost:5050/"

def PATCH():
    global url
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
        while id <= 0:
            try:
                id = int(input("Which client would you like to update: "))
                if id <= 0:
                    print("You must introduce an ID greater than 0.")
            except:
                print("You must introduce an integer!")
        url = url + str(id)
        clients = requests.get(baseUrl)
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
            name = 0
            while name == "":
                try:
                    name = input("Introduce name: ")
                    if name == "":
                        print("Please do not leave the name empty.")
                except:
                    print("Please introduce a valid name!")
            client = {'name': name}
        elif attribute == 2:
            lastName = 0
            while lastName == "":
                try:
                    lastName = input("Introduce last name: ")
                    if lastName == "":
                        print("Please do not leave the last name empty.")
                except:
                    print("Please introduce a valid last name!")
            client = {'lastName': lastName}
        elif attribute == 3:
            phoneNumber = 0
            while len(phoneNumber) != 10:
                try:
                    phoneNumber = int(input("Introduce phone number: "))
                    if len(phoneNumber) != 10:
                        print("Please introduce a phone number that has 10 digits.")
                except:
                    print("Please introduce a valid phone number!")
            client = {'phoneNumber': phoneNumber}
        elif attribute == 4:
            email = ""
            while email == "":
                try:
                    email = input("Introduce email: ")
                    if email == "":
                        print("Please do not leave the email empty.")
                except:
                    print("Please introduce a valid email!")
            client = {'email': email}
        response = requests.patch(url, json=client)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
            url = "http://localhost:5050/"
        else:
            print("The client couldn't get updated or was not found.")
            url = "http://localhost:5050/"
    elif type == 2:
        baseUrl = url + "products/"
        id = int(input("Which product would you like to update: "))
        url = url + str(id)
        products = requests.get(baseUrl)
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
            description = ""
            while description == "":
                try:
                    description = input("Introduce description: ")
                    if description == "":
                        print("Please do not leave the description empty.")
                except:
                    print("Please introduce a valid description!")
            product = {'description': description}
        elif attribute == 2:
            price = 0
            while price <= 0: 
                try:
                    price = float(input("Introduce price: "))
                    if price <= 0:
                        print("Please introduce a price greater than 0.")
                except:
                    print("Please introduce a valid price!")
            product = {'price': price}
        elif attribute == 3:
            clientID = 0
            while clientID <= 0:
                try:
                    clientID = int(input("Introduce client ID: "))
                    if clientID <= 0:
                        print("Please introduce a client ID greater than 0.")
                except:
                    print("Please introduce a valid client ID!")
            product = {'clientID': clientID}
        response = requests.patch(url, json=product)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json)
            print("The product has been updated.")
            url = "http://localhost:5050/"
        else:
            print("The product couldn't get updated or was not found.")
            url = "http://localhost:5050/"

def DELETE():
    global url
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
            url = "http://localhost:5050/"
        else:
            print("The client wasn't found.")
            url = "http://localhost:5050/"
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
            url = "http://localhost:5050/"
        else:
            print("The product wasn't found.")
            url = "http://localhost:5050/"