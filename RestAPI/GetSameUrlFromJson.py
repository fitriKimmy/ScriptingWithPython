# Find out if there are any duplicate urls in photo field from response json

import requests

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)

# get list photos
list_photo = []
for photo in response.json():
    list_photo.append(photo['url'])

# Get lenth of the all photo
print(len(list_photo))

# Get the only duplicate data by using Set
print(len(set(list_photo)))
