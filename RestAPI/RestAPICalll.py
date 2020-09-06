import requests

# GET METHOD
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
print (response.json())

# POST METHOD
jsonPayload = {'albumId': 1, 'title': 'TestTitle', 'url': 'nothing.com', 'thumbnailUrl': 'nothing.com'}
response = requests.post(url,jsonPayload)
response.json()

# PUT METHOD
url = 'https://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url,json=jsonPayload)
response.json()

# DELETE METHOD
response = requests.delete(url)
response.json()