import requests
api_url = "https://jsonplaceholder.tipycode.com/todos/150"
response = requests.get(url)
print("Status code: ", response.status_code)
print(response.json())