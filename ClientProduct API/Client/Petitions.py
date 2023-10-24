import requests

url = "http://localhost:5050/"

def GET():
    response = requests.get(url)
    print("Status code: ", response.status_code)
    if response.status_code == 200:
        print(response.json)
    else:
        print("The JSON file couldn't be read.")

def GET1():
    pass

def POST():
    pass

def PUT():
    pass

def PATCH():
    pass

def DELETE():
    pass