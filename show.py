import requests



request = requests.get('http://127.0.0.1:8000/random/8456421')
print(request.json())