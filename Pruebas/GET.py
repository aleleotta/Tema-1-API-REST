import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)
print("Status code: ", response.status_code)
print(response.json())