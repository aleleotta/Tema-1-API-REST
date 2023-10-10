import requests
url = "https://jsonplaceholder.typicode.com/todos"
todo = {'userId' : 2, 'title': 'Hacer tarea prueba', 'completed': False}
response = requests.post(url)
print(response.json())
print('Codigo de estado: ', response.status_code)