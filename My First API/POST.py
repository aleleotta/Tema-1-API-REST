import requests
url = "http://localhost:5050/countries"
dictionary = {"name": "Spain", "capital": "Madrid", "area": 5000}
response = requests.post(url, json=dictionary)
print("Code status: ", response.status_code)
print(response.json())
