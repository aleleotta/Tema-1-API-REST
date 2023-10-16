import requests
url = "http://localhost:5050/countries/2"
response = requests.delete(url)
print("Status code: ", response.status_code)
if response.status_code == 200:
    print("The following country has been deleted.")
else:
    print("The following country wasn't found or deleted.")