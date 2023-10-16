import requests

#url = "https://jsonplaceholder.typicode.com/"

def list(): #List of functions
    print("List:")
    print("\t1) Show all posts")
    print("\t2) Show a specific post")
    print("\t3) Add a new post")
    print("\t4) Mofidy all attributes of a specific post")
    print("\t5) Modify specific attribute of a specific post")
    print("\t6) Delete a post")
    print("\t0) Exit program")

"""Functions"""
def showAll(): #Shows all posts.
    GET()
    
def show(id): #Asks for ID to get a single post from the JSON file.
    id = int(input("Introduce the ID: "))
    GET1(id)
    
def add(): #Adds a new post into the JSON file.
    userId = int(input("Introduce a user ID: "))
    id = int(input("Introduce an ID: "))
    title = input("Introduce a title: ")
    body = input("Introduce a whole text: ")
    POST(userId, id, title, body)
    
def modifyAll(): #Modifies all attributes of a single post through PUT.
    print("Introduce the ID of the data you want to modify: ")
    id = int(input("ID: "))
    print("Introduce the data of the post below to modify.")
    title = input("Title: ")
    body = input("Body: ")
    PUT(id, title, body)
    
def modify(): #Modifies a single attribute in a single post.
    id = int(input("Introduce the ID of the instance to modify: "))
    attributeType = int(input("What attribute do you want to modify? 1) Title 2) Body")) #Parameter for PATCH function to indicate attribute to modify.
    if attributeType == 1:
        attribute = input("Title: ")
    if attributeType == 2:
        attribute = input("Body: ")
    PATCH(id, attributeType, attribute)
    
def delete(): #Removes a post from the JSON file by asking for post ID.
    id = int(input("Introduce the ID of the post that you would like to delete: "))
    DELETE(id)
    
"""Requests"""
def GET():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200: #Checking for correct code, if not the same code than it displays an error message.
        print(response.json())
    else:
        print("The URL is not valid.") 

def GET1(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id) #Updates current path to indicate which post the id is referring to.
    url = url + chosenId
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200: #Checking for correct code, if not the same code than it displays an error message.
        print(response.json())
    else:
        print("The URL is not valid.") 
    
def POST(userId1, id1, title1, body1):
    url = "https://jsonplaceholder.typicode.com/posts"
    post = {'userId': userId1, 'id': id1, 'title': title1, 'body': body1}
    response = requests.post(url, json=post)
    print("Status code: ", response.status_code)
    if response.status_code == 201: #Checking for correct code, if not the same code than it displays an error message.
        print(response.json())
    else:
        print("The post couldn't get uploaded.")
    
def PUT(id1, title1, body1):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id1) #Updates current path to indicate which post the id is referring to.
    url = url + chosenId
    update = {'title': title1, 'body': body1}
    response = requests.put(url, json=update)
    print("Status code: ", response.status_code)
    if response.status_code == 200: #Checking for correct code, if not the same code than it displays an error message.
        print(response.json())
    else:
        print("The post couldn't get updated.")
    
def PATCH(id1, attributeType, attribute):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id1) #Updates current path to indicate which post the id is referring to.
    url = url + chosenId
    if attributeType == 1:
        update = {'title': attribute}
    if attributeType == 2:
        update = {'body': attribute}
    response = requests.patch(url, json=update)
    print("Status code: ", response.status_code)
    if response.status_code == 200: #Checking for correct code, if not the same code than it displays an error message.
        print(response.json())
    else:
        print("The post couldn't get updated.")
    
def DELETE(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id) #Updates current path to indicate which post the id is referring to.
    url = url + chosenId
    response = requests.delete(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200: #Checking for correct code, if not the same code than it displays an error message.
        print(response.json())
    else:
        print("The post couldn't get deleted.")