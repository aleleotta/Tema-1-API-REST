import requests

url = "http://localhost:5050/"
clientsFile = "ClientProduct API\\JSON\\Client.json"
productsFile = "ClientProduct API\\JSON\\Product.json"

type = 0
while type != 1 and type != 2:
    try:
        type = int(input("Would you like to update a client or a product? 1) Client 2) Product\n"))
        if type != 1 and type != 2:
            print("Please introduce a valid option!")
    except:
        print("You must introduce an integer!")
if type == 1:
    baseUrl = url + "clients/"
    id = 0
    while id <= 0:
        try:
            id = int(input("Which client ID would you like to update: "))
            if id <= 0:
                print("You must introduce an ID greater than 0.")
        except:
            print("You must introduce an integer!")
    url = baseUrl + str(id)
    clients = requests.get(baseUrl)
    clientsJson = clients.json()
    found = False
    dni = ""
    for client in clientsJson:
        if client['id'] == id:
            dni = client['dni']
            found = True
            break
    if found == True:
        name = ""
        while name == "":
            try:
                name = input("Introduce name: ")
                if name == "":
                    print("Please do not leave the name empty.")
            except:
                print("Please introduce a valid name!")
        lastName = ""
        while lastName == "":
            try:
                lastName = input("Introduce last name: ")
                if lastName == "":
                    print("Please do not leave the last name empty.")
            except:
                print("Please introduce a valid last name!")
        phoneNumber = 0
        while len(str(phoneNumber)) == 10:
            try:
                phoneNumber = int(input("Introduce phone number: "))
                if len(phoneNumber) == 10:
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
        client = {'id': id, 'dni': dni, 'name': name, 'lastName': lastName, 'phoneNumber': phoneNumber, 'email': email}
        response = requests.put(url, json=client)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json())
            print("The product has been updated.")
            url = "http://localhost:5050/"
        else:
            print("The client couldn't get updated or was not found.")
            url = "http://localhost:5050/"
    else:
        print("The client wasn't found.")
elif type == 2:
    baseUrl = url + "products/"
    id = 0
    while id <= 0:
        try:
            id = int(input("Which product ID would you like to update: "))
            if id <= 0:
                print("You must introduce an ID greater than 0.")
        except:
            print("You must introduce an integer!")
    url = baseUrl + str(id)
    products = requests.get(baseUrl)
    productsJson = products.json()
    found = False
    name = ""
    for product in productsJson:
        if product['id'] == id:
            name = product['name']
            found = True
            break
    if found == True:
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
        product = {'id': id, 'name': name, 'description': description, 'price': price, 'clientID': clientID}
        response = requests.put(url, json=product)
        print("Status code: ", response.status_code)
        if response.status_code == 200:
            print(response.json())
            print("The product has been updated.")
            url = "http://localhost:5050/"
        else:
            print("The product couldn't get updated or was not found.")
            url = "http://localhost:5050/"
    else:
        print("The product wasn't found.")