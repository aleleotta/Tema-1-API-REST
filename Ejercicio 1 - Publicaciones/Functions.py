import requests

#url = "https://jsonplaceholder.typicode.com/"
dictionary = {}

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
    
#def modify()
    
#def modify(id, attribute)
    
#def delete(id)
    
"""Requests"""
def GET():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status code: ", response.status_code)
    print(response.json())

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
    if response.status_code == 201:
        dictionary.update(post)
        print("Status code: ", response.status_code)
        print(response.json())
    else:
        print("The post couldn't get uploaded.")
    
def PUT(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    print("Status code: ", response.status_code)
    print(response.json())
    
def PATCH(id, attribute):
    url = "https://jsonplaceholder.typicode.com/posts"
    print("Status code: ", response.status_code)
    print(response.json())
    
def DELETE(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    print("Status code: ", response.status_code)
    print(response.json())