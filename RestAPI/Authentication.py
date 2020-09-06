# Get user detail from github
import requests

url = 'https://api.github.com/user'
response = requests.get(url, auth = ('djw-test','password1'))
# or you can use authorization with token 
response = requests.get(url, headers={'Authorization':'Bearer xxxxx'})

my_json = response.json()

# To get all list key
for key in my_json.keys():
    print (key)

# to get value specific
print(my_json['email'])


