import requests as requests


request = {
    'id': '1',
    'rating': 40
}

response = requests.post('http://localhost:8080/rate/', json=request)

actual = response.json()

print(actual)
