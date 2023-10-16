import requests
url = "http://localhost:5050/countries/1"
response = requests.get(url)
print("Status code: ", response.status_code)
if response.status_code == 200:
    print(response.json)
else:
    print("The country with the following ID was not found.")