import requests
url = "http://localhost:5050/countries/1"
dictionary = {"name": "Spain", "capital": "Madrid", "area": 5000}
response = requests.put(url, json=dictionary)
print("Code status: ", response.status_code)
if response.status_code == 200:
    print(response.json())
else:
    print("The following country wasn't found or updated.")