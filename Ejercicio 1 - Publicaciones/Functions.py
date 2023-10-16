import requests

#url = "https://jsonplaceholder.typicode.com/"

def list():
    print("List:")
    print("\t1) Show all posts")
    print("\t2) Show a specific post")
    print("\t3) Add a new post")
    print("\t4) Mofidy all attributes of a specific post")
    print("\t5) Modify specific attribute of a specific post")
    print("\t6) Delete a post")
    print("\t0) Exit program")

"""Functions"""
def showAll():
    GET()
    
def show(id):
    id = int(input("Introduce the ID: "))
    GET1(id)
    
def add():
    userId = int(input("Introduce a user ID: "))
    id = int(input("Introduce an ID: "))
    title = input("Introduce a title: ")
    body = input("Introduce a whole text: ")
    POST(userId, id, title, body)
    
def modifyAll():
    print("Introduce the data of the post below to modify.")
    userId = int(input("User ID: "))
    id = int(input("ID: "))
    title = input("Title: ")
    body = input("Body: ")
    PUT(userId, id, title, body)
    
def modify():
    id = int(input("Introduce the ID of the instance to modify: "))
    attributeType = int(input("What attribute do you want to modify? 1) User ID 2) ID 3) Title 4) Body"))
    if attributeType == 1:
        attribute = int(input("UserID: "))
    if attributeType == 2:
        attribute = int(input("ID: "))
    if attributeType == 3:
        attribute = input("Title: ")
    if attributeType == 4:
        attribute = input("Body: ")
    PATCH(id, attributeType, attribute)
    
def delete():
    id = int(input("Introduce the ID of the post that you would like to delete: "))
    DELETE(id)
    
"""Requests"""
def GET():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status code: ", response.status_code)
    dictIsFilled = False
    if response.status_code == 200:
        print(response.json())
    else:
        print("The URL is not valid.") 

def GET1(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id)
    url = url + chosenId
    response = requests.get(url)
    print("Status code: ", response.status_code)
    print(response.json())
    
def POST(userId1, id1, title1, body1):
    url = "https://jsonplaceholder.typicode.com/posts"
    post = {'userId': userId1, 'id': id1, 'title': title1, 'body': body1}
    response = requests.post(url, json=post)
    print("Status code: ", response.status_code)
    if response.status_code == 201:
        print(response.json())
    else:
        print("The post couldn't get uploaded.")
    
def PUT(userId1, id1, title1, body1):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id1)
    url = url + chosenId
    update = {'userId': userId1, 'id': id1, 'title': title1, 'body': body1}
    response = requests.put(url, json=update)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print("The post couldn't get updated.")
    
def PATCH(id1, attributeType, attribute):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id1)
    url = url + chosenId
    if attributeType == 1:
        update = {'userId': attribute}
    if attributeType == 2:
        update = {'id': attribute}
    if attributeType == 3:
        update = {'title': attribute}
    if attributeType == 4:
        update = {'body': attribute}
    response = requests.patch(url, json=update)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print("The post couldn't get updated.")
    
def DELETE(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    chosenId = "/" + str(id)
    url = url + chosenId
    response = requests.delete(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json())
    else:
        print("The post couldn't get deleted.")