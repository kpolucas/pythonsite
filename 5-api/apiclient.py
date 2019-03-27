import requests
import json

url = 'https://official-joke-api.appspot.com/random_joke'
resp = requests.get(url)
if resp.status_code != 200:
    raise Exception('mal ahi')

data = resp.json()
print(data['setup'])
print(data['punchline'])
