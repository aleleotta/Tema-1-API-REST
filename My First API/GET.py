import requests
url = "http://localhost:5050/countries"
response = requests.get(url)
print("Status code: ", response.status_code)
if response.status_code == 200:
    print(response.json)
else:
    print("Attempt to get all countries failed!")